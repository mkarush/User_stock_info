from flask import Blueprint, request,render_template, redirect, url_for,flash
from jinja2 import TemplateNotFound
from paramters.db_info import price
from paramters.db_info import db
from paramters.api_call import get_values


name_mod =Blueprint('name',__name__,template_folder='templates')

@name_mod.route('/name', methods=['GET','POST'])
def name():
    try:
        arr = []
        search = True
        company = request.form["company"]
        key = request.form["api_key"]
        output = get_values(company, key, search)
        for key, value in output.items():
            for v in value:
                arr.append(v['1. symbol'] + ":" + v['2. name'])
        flash("Top 10 matches of search - {}".format(company))
        return render_template('search_result.html', output=arr)
    except TemplateNotFound:
        abort(404)