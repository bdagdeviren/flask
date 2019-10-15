from threading import Thread, Event
from subprocess import Popen, PIPE

thread = Thread()
thread_stop_event = Event()


class RandomThread(Thread):
    command = ""
    socketio = None

    def __init__(self, command, socketio):
        self.delay = 1
        self.command = command
        self.socketio = socketio
        super(RandomThread, self).__init__()

    def createProcess(self):
        process = Popen(self.command, stdout=PIPE, shell=True)
        while True:
            line = process.stdout.readline().rstrip()
            if not line:
                break
            yield line

    def run(self):
        for path in self.createProcess():
            self.socketio.emit('newnumber', path.decode("utf-8"), namespace='/test')
