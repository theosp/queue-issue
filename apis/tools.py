from itertools import chain
import logging
import settings
from google.appengine.api.urlfetch import fetch
from google.appengine.api import runtime
import urllib2


def debug(location, message, params=None, force=False):
    if not (settings.REMOTE_DEBUG or settings.LOCALE_DEBUG or force):
        return

    if params is None:
        params = {}

    params["memory"] = runtime.memory_usage().current()
    params["instance_id"] = settings.INSTANCE_ID

    debug_message = "%s/%s?%s" % (urllib2.quote(location), urllib2.quote(message), "&".join(["%s=%s" % (p, urllib2.quote(unicode(params[p]).encode("utf-8"))) for p in params]))

    try:
        if settings.REMOTE_DEBUG or force:
            fetch("%s/%s" % (settings.REMOTE_DEBUGGER, debug_message))
    except:
        pass
        
    if settings.LOCALE_DEBUG or force:
        logging.debug(debug_message)
