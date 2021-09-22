import re
from datetime import datetime

from app.configs.database import db
from app.models.lead_model import Lead
from flask import current_app, jsonify, request
from sqlalchemy import desc
from sqlalchemy.orm.exc import UnmappedInstanceError


def register_lead(data) -> tuple:
    data = request.get_json()

    if type(validate_phone(data['phone'])) == tuple:
        return validate_phone(data['phone'])

    new_lead = Lead(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        creation_date=datetime.now(),
        last_visit=datetime.now(),
    )

    session = current_app.db.session
    session.add(new_lead)
    session.commit()

    return jsonify(new_lead), 201


def validate_phone(phone) -> tuple:
    try:
        pattern = "([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})-([0-9]{4})"
        re.fullmatch(pattern, phone).group()
    except AttributeError:
        msg = {'erro': 'Telefone Invalido formato aceito (99)12345-6789'}
        return msg, 400


def show_all() -> tuple:
    query = Lead.query.order_by(desc(Lead.visits)).all()
    return jsonify(query), 200


def update_visits(data) -> tuple:
    try:
        lead = Lead()
        query = lead.query.filter_by(email=data['email']).first()

        sum_visits = query.__dict__['visits'] + 1
        data = {'visits': sum_visits, 'last_visit': datetime.now()}

        for key, value in data.items():
            setattr(query, key, value)

        db.session.add(query)
        db.session.commit()

        return '', 204

    except AttributeError:
        return {'erro': 'Nenhum dado encontrado!'}, 404


def delete_lead(data) -> tuple:
    try:
        query = Lead.query.filter_by(email=data['email']).first()

        db.session.delete(query)
        db.session.commit()

        return '', 204

    except UnmappedInstanceError:
        return {'erro': 'Nenhum dado encontrado!'}, 404
