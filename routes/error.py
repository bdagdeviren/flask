from flask import Blueprint, Response, render_template

error_page = Blueprint('error_page', __name__,
                       template_folder='templates')


@error_page.app_errorhandler(404)
def page_error(e):
    return render_template('error/404/index.html'), 404
