import json
import time
import os
import psutil
from datetime import datetime
from flask import Blueprint, Response, render_template

dashboard_page = Blueprint('dashboard_page', __name__,
                           template_folder='templates')


@dashboard_page.route('/')
def page_dashboard():
    return render_template('dashboard/dashboard.html')


@dashboard_page.route('/icons')
def page_icons():
    return render_template('dashboard/icons.html')


@dashboard_page.route('/map')
def page_map():
    return render_template('dashboard/map.html')


@dashboard_page.route('/notifications')
def page_notifications():
    return render_template('dashboard/notifications.html')


@dashboard_page.route('/tables')
def page_tables():
    return render_template('dashboard/tables.html')


@dashboard_page.route('/typography')
def page_typography():
    return render_template('dashboard/typography.html')


@dashboard_page.route('/user')
def page_user():
    return render_template('dashboard/user.html')


@dashboard_page.route('/chart-data')
def page_chart_data():
    def generate_random_data():
        while True:
            pid = os.getpid()
            py = psutil.Process(pid)
            process = psutil.virtual_memory()[2]
            memoryu = py.memory_percent()
            disk = psutil.disk_usage('/')
            disk_percent_used = disk.percent
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': psutil.cpu_percent(), 'memory': memoryu,
                 'total': process, 'disk': disk_percent_used})
            yield f"data:{json_data}\n\n"
            time.sleep(1)
    return Response(generate_random_data(), mimetype='text/event-stream')
