from rest_framework.exceptions import APIException

class NotAuthorizedError(APIException):
    status_code = 403
    default_detail = 'The api is nor authorized.'
    default_code = 'not_authorized'