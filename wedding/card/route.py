from flask import Flask, Blueprint, request, make_response, jsonify
from sqlalchemy.sql.expression import func
from .card import Cards
from ..functions import valid_param
from .. import db

bp = Blueprint('route', __name__, url_prefix = '/api')

@bp.route('/cards')
def getallphoto():
    limit = request.args.get('limit', 8)
    offset = request.args.get('offset', 0)

    try:
        offset = int(offset)
        limit = int(limit)
        if 0 == limit:
            return jsonify({'error': True, 'message': 'limit 不行是 0'}), 400
    except ValueError:
        return jsonify({'error': True, 'message': 'limt & offset need to be integer'}), 400

    cards = Cards.query.order_by(Cards.id.desc()).limit(limit + 1).offset(offset)
    result = []
    has_more = False

    for index, card in enumerate(cards):
        if index == (limit):
            has_more = True
            break;

        result.append(card.to_dict())

    return jsonify({'data': result, 'has_more': has_more})

# 抽獎, 依 limit 決定抽幾個
@bp.route('/card', methods = ['GET'])
def randomCard():
    limit = request.args.get('limit', 0)

    try:
        limit = int(limit)
        if limit <= 0:
            return jsonify({'error': True, 'message': '參數不正確'}), 400
    except ValueError:
        return jsonify({'error': True, 'message': '參數不正確'}), 400

    cards = Cards.query.filter_by(status=0).order_by(func.rand()).limit(limit).all()

    result = []
    for card in cards:
        # 更新 status
        card.status = 1
        db.session.commit()

        result.append(card.to_dict())

    return jsonify({'data': result})
