#!/bin/bash

source /etc/default/devnetsandbox

echo $PASSWORD | /usr/sbin/openconnect --verbose --user=$USER --passwd-on-stdin $GATEWAY:$PORT
