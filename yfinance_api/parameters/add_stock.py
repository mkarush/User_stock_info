from flask import Blueprint, render_template,request,render_template,redirect, url_for, flash
from jinja2 import TemplateNotFound
from parameters.db_info import price
from parameters.db_info import db
import yfinance as yf

add_mod =Blueprint('add_stock',__name__,template_folder='templates')

@add_mod.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    try:
        size=0
        cache={}
        company = request.form["stock_name"]
        if request.method == "POST":
            query = price.query.all()
            for value in query:
                cache[value.name]=size
                size=+1
            if company in cache:
                flash("{} DATA ALREADY IN TABLE".format(company))
                return redirect(url_for('view.view'))
            else:
                out_put = yf.Ticker(company)
                output = out_put.info['bid']
                name = price(name=company, value=output)
                db.session.add(name)
                db.session.commit()
                flash("{} added to the list:".format(company))
                return redirect(url_for('view.view'))
    except TemplateNotFound:
        abort(404)
