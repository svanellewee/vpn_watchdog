#!/bin/bash
VPNName=$1
USERNAME=$2
PASSWORD=$3
scutil --nc start "$VPNName" --user $USERNAME

sleep 1
osascript -e "tell application \"System Events\" to keystroke \"$PASSWORD\""
osascript -e "tell application \"System Events\" to keystroke return"

