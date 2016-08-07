"""Sample API."""

import endpoints
import logging

from api.api_messages import SampleRequest
from api.api_messages import SampleResponse
from endpoints import api_config
from protorpc import remote


_AUTH_CONFIG = api_config.ApiAuth(allow_cookie_auth=True)


@endpoints.api(name='sample', version='v1',
               description='Sample API',
               title='Sample Service',
               auth=_AUTH_CONFIG, owner_name='SampleApp',
               owner_domain='sample.com')
class SampleApi(remote.Service):

    """Class which defines sample API v1."""

    @endpoints.method(SampleRequest, SampleResponse,
                      path='sample/get/{name}', name='sample.return_name_get',
                      http_method='GET')
    def return_name_get(self, request):
        """Return name from same request."""
        logging.info(request.name)
        return SampleResponse(name=request.name)

    @endpoints.method(SampleRequest, SampleResponse,
                      path='sample/post', name='sample.return_name_post',
                      http_method='POST')
    def return_name_post(self, request):
        """Return name for same request."""
        return SampleResponse(name=request.name)
