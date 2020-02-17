from flask import Blueprint, render_template, redirect, url_for
from jinja2 import TemplateNotFound
from parameters.db_info import price

mod =Blueprint('view',__name__,template_folder='templates')

@mod.route('/view')
def view():
    try:
        return render_template('view.html',price = price.query.all())
    except TemplateNotFound:
        abort(404)
