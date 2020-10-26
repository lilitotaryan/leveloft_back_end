from rest_framework.views import exception_handler

def custom_error_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.

    if response is not None:
        response.data = {"success": False,
                         "message": "unsuccessful response",
                         "error": {
                             "error_message": response.data.get('detail'),
                             "status_code": response.status_code
                             }
                         }

    return response