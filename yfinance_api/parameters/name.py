from flask import Blueprint, request,render_template, redirect, url_for,flash
from jinja2 import TemplateNotFound
from parameters.db_info import price
from parameters.db_info import db
import json
import requests

name_mod =Blueprint('name',__name__,template_folder='templates')

@name_mod.route('/name', methods=['GET','POST'])
def name():
    try:
        arr=[]
        company = request.form["company"]
        key = "WTDKN2UOHE4QNOW3"
        API_URL = "https://www.alphavantage.co/query"
        data = {
            "function": "SYMBOL_SEARCH",
            "keywords": company,
            "apikey": key}
        response = requests.get(API_URL, params=data)
        output = json.loads(response.text)
        for key, value in output.items():
            for v in value:
                print(v['2. name'])
                arr.append(v['1. symbol'] + ":" + v['2. name'])
            flash("Top 10 matches of search - {}".format(company))
            return render_template('search_result.html', output=arr)
    except TemplateNotFound:
        abort(404)


