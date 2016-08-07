"""
  Route file.
"""

import endpoints
import main
import webapp2

from api.sample_api import SampleApi
from background import cron


APPLICATION = webapp2.WSGIApplication([
    webapp2.Route(r'/', main.HomeHandler, name='home'),
    webapp2.Route(
        '/cron/sample', cron.SampleHandler, name='SampleCron')
], config={}, debug=True)

API = endpoints.api_server(
    [SampleApi],
    restricted=False
)
