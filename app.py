from flask import Flask
from routes.dashboard import dashboard_page
from routes.index import index_page
from routes.error import error_page


application = Flask(__name__)
application.register_blueprint(dashboard_page, url_prefix='/dashboard')
application.register_blueprint(index_page, url_prefix='/')
application.register_blueprint(error_page)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='9090', debug=True, threaded=True)
