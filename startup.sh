#!/usr/bin/bash
# start gunicorn from this app
cd /home/andy/pi
/home/andy/.local/bin/gunicorn --workers 2 --bind 0.0.0.0:5001 incoming_call:app --daemon
