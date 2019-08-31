from flask import Flask, Blueprint, request, make_response, jsonify
from sqlalchemy.sql.expression import func
from .card import Cards
from .functions import valid_param
from .. import db

bp = Blueprint('route', __name__, url_prefix = '/api')

@bp.route('/cards')
def getallphoto():
    cards = Cards.query.order_by(Cards.id.desc()).all()
    result = []
    for card in cards:
        result.append(card.to_dict())
    return jsonify(result)
