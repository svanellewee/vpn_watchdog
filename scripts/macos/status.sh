#!/bin/bash
VPN_NAME=$1
VPN_STATE=$(echo `scutil --nc status "$VPN_NAME"` |cut -d" " -f1)
if [[ ${VPN_STATE} == "Disconnected" ]]; then
    echo "Disconnected!"
    exit 1
else
    echo "Connected"
    exit 0
fi

