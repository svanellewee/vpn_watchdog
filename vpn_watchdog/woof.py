from subprocess import Popen, PIPE
import yaml
import os
import sys
import time

config = None
with open(".config.yml") as config_file:
    config = yaml.load(config_file.read())
try:
    vpn_name = config['credentials']['servicename']
except KeyError:
    sys.exit(1)

def is_online():
    process = Popen(["bash", os.path.join(os.getcwd(), "scripts/macos/status.sh"), vpn_name ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err =process.communicate()
    #print(output, err, process.returncode)
    return process.returncode == 0


def main(time_val=None):
    while True:
        if time_val:
            time.sleep(time_val)
        if is_online():
            print("ONLINE!")
        else:
            print("WOOF!")

main(5)
