from flask_socketio import SocketIO
from flask import Flask
from routes.socketio import RandomThread
from routes.dashboard import dashboard_page
from routes.index import index_page
from routes.error import error_page

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)


@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    thread = RandomThread("mvn -B dependency:get -Dartifact=wadi:wadi:0.9 -Dmaven.repo.local=/home/test",socketio)
    thread.start()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


app.register_blueprint(dashboard_page, url_prefix='/dashboard')
app.register_blueprint(index_page, url_prefix='/')
app.register_blueprint(error_page)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='9090')
