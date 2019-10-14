#!/usr/bin/env python
from subprocess import Popen, PIPE

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line


if __name__ == "__main__":
    for path in run("mvn -B dependency:get -Dartifact=wadi:wadi:0.9 -Dmaven.repo.local=/home/test"):
        print(path.decode("utf-8"))