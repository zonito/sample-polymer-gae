"""ProtoRPC message class definitions for Sample API."""

from protorpc import messages


class SampleRequest(messages.Message):

    """Request object structure for sample api."""
    name = messages.StringField(1, required=True)


class SampleResponse(messages.Message):
    """Response to prepare from an api call"""
    name = messages.StringField(1, required=True)
