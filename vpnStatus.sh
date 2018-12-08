#!/bin/bash

####
##
## vpnStatus.sh: checks whether there' a VPN tunnel is active. Meant as a simple way to display VPN status in Polybars
##
####

ORANGE='\033[0;33m'
result=$(nmcli -t -f type,state,connection d | egrep '^tun|tap' | grep connected | awk -F':' '{ print $3 }')
[[ -z $result ]] && echo '%{F#555}%{F-}' || echo -e "%{F#ffb52a}%{F-}"
