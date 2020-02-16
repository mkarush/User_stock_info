from flask import Blueprint, render_template,request,render_template,redirect, url_for, flash
from jinja2 import TemplateNotFound
from paramters.db_info import price
from paramters.db_info import db
from paramters.api_call import get_values


add_mod =Blueprint('add_stock',__name__,template_folder='templates')


@add_mod.route('/add_stock', methods=['GET', 'POST'])
def addstock():
    try:
        cache={}
        search = False
        company = request.form["stock_name"]
        api_key = request.form["api_key"]
        if request.method == "POST":
            query = price.query.all()
            for value in query:
                cache[value.name] = value.key
            if company in cache:
                flash("{} DATA ALREADY IN TABLE".format(company))
                return redirect(url_for('view.view'))
            else:
                json_data = get_values(company, api_key, search)
                for k, v in json_data.items():
                    output = float(v["05. price"])
                    cache[company] = api_key
                    name = price(name=company, value=output, key=api_key)
                    db.session.add(name)
                    db.session.commit()
                    flash("{} added to the list:".format(company))
                    return redirect(url_for('view.view'))
    except TemplateNotFound:
        abort(404)
