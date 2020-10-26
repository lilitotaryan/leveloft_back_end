from django.utils.encoding import smart_text
from rest_framework import renderers


class ResponseRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if not(data.get('success') == False):
            data = {"success": True,
                    "message": "successful response",
                    "data": data}
        return super(ResponseRenderer, self).render(data, accepted_media_type=None, renderer_context=None)