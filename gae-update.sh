#!/bin/bash

sudo ./clean-pyc

./google_appengine/appcfg.py backends . update queue-issue
./google_appengine/appcfg.py update .
