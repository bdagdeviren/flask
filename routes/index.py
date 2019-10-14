from flask import Blueprint, Response, render_template
from database.config import MysqlConfig
from subprocess import Popen, PIPE

index_page = Blueprint('index_page', __name__,
                       template_folder='templates')


@index_page.route('/')
def page_index():
    return render_template('index/index.html')

@index_page.route('/npm')
def page_npm():
    return render_template('index/npm.html')

@index_page.route('/maven')
def page_maven():
    return render_template('index/maven.html')

@index_page.route('/docker')
def page_docker():
    return render_template('index/docker.html')
