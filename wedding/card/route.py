from flask import Flask, Blueprint, request, make_response, jsonify
from sqlalchemy.sql.expression import func
from google.cloud import storage
from .card import Cards
from ..functions import valid_param, upload_file
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

@bp.route('/cards', methods = ['POST'])
def store():
    image = request.files.get('image')
    if image is None:
        return jsonify({'error': True, 'message': '請上傳照片'}), 400

    form = request.form
    if not valid_param(form, ['message', 'name']):
        return jsonify({'error': True, 'message': '參數不完整'}), 400

    try:
        file_path = upload_file(image)
        print(file_path)
    except TypeError as error:
        return jsonify({'error': True, 'message': format(error)}), 400
    except:
        return jsonify({'error': True, 'message': '檔案上傳失敗'}), 500

    card = Cards(name = form['name'], message = form['message'], image = file_path)
    try:
        db.session.add(card)
        db.session.commit()
    except:
        return jsonify({'error': True, 'message': '留言失敗'}), 500

    return jsonify({'error': False, 'data': card.to_dict()})

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
