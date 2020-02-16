from flask import Blueprint, request,render_template, redirect, url_for,flash
from jinja2 import TemplateNotFound
from paramters.db_info import price
from paramters.db_info import db
from paramters.api_call import get_values


update_mod =Blueprint('update',__name__,template_folder='templates')

@update_mod.route('/update', methods=['GET'])
def update():
    try:
        search = False
        query = price.query.all()
        for value in query:
            p = price.query.filter_by(name=value.name).all()
            for sub_value in p:
                json_data = get_values(sub_value.name, sub_value.key, search)
                for k, v in json_data.items():
                    value.value = float(v["05. price"])
                    db.session.commit()
        flash("List of all the values user added")
        return redirect(url_for('view.view'))
    except TemplateNotFound:
        abort(404)