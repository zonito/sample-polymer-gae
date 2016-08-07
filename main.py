"""
  Main file which is responsible to instantiate appengine application.
"""

import os
import webapp2

from google.appengine.ext.webapp import template


class HomeHandler(webapp2.RequestHandler):

    """Displays home page."""

    def get(self):
        """Just render Home page."""
        self.response.headers['Content-Type'] = 'text/html'
        content = template.render(
            os.path.join(os.path.dirname(__file__), 'index.html'), {})
        self.response.out.write(content)
