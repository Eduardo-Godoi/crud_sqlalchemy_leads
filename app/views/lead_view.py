from app.services.routes_services import (delete_lead, register_lead, show_all,
                                          update_visits)
from flask import Blueprint, request

bp = Blueprint('lead', __name__, url_prefix='/lead')


@bp.post('')
def create():
    data = request.get_json()
    output, status_code = register_lead(data)
    return output, status_code


@bp.get('')
def get_all():
    output, status_code = show_all()
    return output, status_code


@bp.patch('')
def update():
    data = request.get_json()
    output, status_code = update_visits(data)
    return output, status_code


@bp.delete('')
def delete():
    data = request.get_json()
    output, status_code = delete_lead(data)
    return output, status_code
