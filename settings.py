# Django settings for razoss_dock project.
import os, time

LOCALE_DEBUG = False # use logging.debug to debug the system
REMOTE_DEBUG = True # use urlfetch to send REMOTE_DEBUGGER debug messages
REMOTE_DEBUGGER = "http://theosp.no-ip.org:81"

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# determine whether we are live or in the SDK
if not os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/non_gae_indicator'):
    GOOGLE_APP_ENGINE_LIVE = True
else:
    GOOGLE_APP_ENGINE_LIVE = False

SITE_URL = 'http://queue-issue.appspot.com/'
SITE_CDN = ''

MEDIA_URL = '/media'

SECRET_KEY = '8m!1)jn76gxr(dkt5^3t$xs8$bn-y5xg2%le1qejo5f3rqqfmx'

ROOT_PATH = os.path.dirname(__file__) or "./"

INSTANCE_ID = str(int(time.time()))
