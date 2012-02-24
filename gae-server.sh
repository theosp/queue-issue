#!/bin/bash

sudo python2.6 ./google_appengine/dev_appserver.py -a "0.0.0.0" -c -d -p 80 --allow_skipped_files .

sudo ./clean-pyc
