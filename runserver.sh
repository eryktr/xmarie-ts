#!/usr/bin/env bash

echo "Server path is $XMARIE_SERVER_PATH"
cd $XMARIE_SERVER_PATH
source env/bin/activate
python -m flask run
