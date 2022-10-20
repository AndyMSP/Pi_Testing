#!/usr/bin/bash
# start gunicorn from this directory
#source /home/andy/.bashrc
cd /home/andy/Pi_Testing
/home/andy/.local/bin/gunicorn --workers 2 --bind 0.0.0.0:5001 open_browser:app --daemon
