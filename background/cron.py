"""
  Cron File, to run handler in certain interval - check cron.yaml
"""

import webapp2


class SampleHandler(webapp2.RequestHandler):

    """Cron Job."""

    def get(self):
        """Copy data."""
        self.response.out.write('OK')
