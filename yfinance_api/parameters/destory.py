from flask import Blueprint, request,render_template, redirect, url_for,flash
from jinja2 import TemplateNotFound
from parameters.db_info import price
from parameters.db_info import db


del_mod =Blueprint('destory',__name__,template_folder='templates')

@del_mod.route('/destory', methods=['GET', 'POST'])
def destory():
    cache={}
    size=0
    try:
        if request.method == "POST":
            query = price.query.all()
            for value in query:
                cache[value.name]=size
                size+=1
            company = request.form["name"]
            if company not in cache:
                flash("{} name not there in following list:".format(company))
                return redirect(url_for('view.view'))
            else:
                user = price.query.filter_by(name=company).first()
                db.session.delete(user)
                db.session.commit()
                del cache[company]
                flash("{} Deleted from the list and check the new list:".format(company))
                return redirect(url_for('view.view'))
    except TemplateNotFound:
        abort(404)