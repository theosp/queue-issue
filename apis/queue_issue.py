#!/usr/bin/env python

from google.appengine.dist import use_library
use_library('django', '1.2')

# imports {{{
from google.appengine.api import taskqueue, runtime, backends
from google.appengine.ext import webapp, db, blobstore
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from lib import simplejson as json

import os, sys

import settings

import time
import re
import logging

from apis import tools
# }}}

# EnqueueTasks {{{
class EnqueueTasks(webapp.RequestHandler):
    def get(self):
        import random, string
        def random_string(length):
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(length))

        blobs_to_process = [random_string(100) for _ in xrange(35)]

        tasks_amount = 100000000
        for i in xrange(tasks_amount):
            task = (random_string(100), random_string(100), "2012-02-24")

            tools.debug("EnqueueTasks", "add-task-%d" % i)

            taskqueue.add(\
                    name=("Process_%s_files---%s--%s--%s--%s" % \
                                (len(blobs_to_process), task[1], task[0], task[2], int(time.time()))),\
                    queue_name="files-processor",\
                    url="/run_task/",\
                    params={"processing_task": json.dumps({"profile": task, "blobs_to_process": blobs_to_process})})
# }}}

# RunTask {{{
class RunTask(webapp.RequestHandler):
    def post(self):
        if backends.get_backend() != "queue-issue" and settings.GOOGLE_APP_ENGINE_LIVE:
            logging.warn("Only the queue-issue backend can call /run_task/")
            return

        return self.response.out.write("OK")
# }}}

# init application {{{
application = webapp.WSGIApplication([
    ('/run_task/', RunTask), # login: admin
    ('/enqueue_tasks/', EnqueueTasks), # login: admin
], debug=True)

def main():
    run_wsgi_app(application)
# }}}

# init the events-logger backend {{{
if backends.get_backend() == "queue-issue":
    tools.debug("%s-backend" % backends.get_backend(), "%s-backend-initiated" % backends.get_backend(), \
            {"instance_id": backends.get_instance(), 
                "backend_instance_url": backends.get_url(instance=backends.get_instance()),
                "backend_load_balancer_url": backends.get_url()
            })
# }}}

if __name__ == '__main__':
    main()
