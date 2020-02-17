from flask import Blueprint, request,render_template, redirect, url_for,flash
from jinja2 import TemplateNotFound
from parameters.db_info import price
from parameters.db_info import db
import yfinance as yf

update_mod =Blueprint('update',__name__,template_folder='templates')

@update_mod.route('/update', methods=['GET'])
def update():
    try:
        if request.method == "GET":
            query = price.query.all()
            for value in query:
                p = price.query.filter_by(name=value.name).all()
                for sub_value in p:
                    out_put = yf.Ticker(subvalue)
                    value.value = out_put.info['bid']
                    db.session.commit()
            flash("List of all the values user added")
            return redirect(url_for('view.view'))
    except TemplateNotFound:
        abort(404)