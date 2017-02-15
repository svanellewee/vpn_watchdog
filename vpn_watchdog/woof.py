from subprocess import Popen, PIPE
import yaml
import os
import sys
import time

config = None
try:
    with open(".config.yml") as config_file:
        config = yaml.load(config_file.read())
except FileNotFoundError:
    print("""Please configure your .config.yml

    credentials:
        servicename: "vpn name"
        username: vpn_username
        password: PASssWORD
    """)
    sys.exit(1)

try:
    vpn_name = config['credentials']['servicename']
    username = config['credentials']['username']
    password = config['credentials']['password']
except KeyError:
    sys.exit(1)

def is_online():
    process = Popen(["bash", os.path.join(os.getcwd(), "scripts/macos/status.sh"), vpn_name ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err =process.communicate()
    return process.returncode == 0


def go_online():
    process = Popen(["bash", os.path.join(os.getcwd(), "scripts/macos/connect.sh"), vpn_name, username, password ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err =process.communicate()
    return process.returncode == 0



def main(time_val=None):
    while True:
        if time_val:
            time.sleep(time_val)
        if is_online():
            print("ONLINE!")
        else:
            print("WOOF!")
            go_online()
            time.sleep(10)
main(5)
