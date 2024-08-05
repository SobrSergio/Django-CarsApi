from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, TokenError):
        response = {
            'status_code': 401,
            'error': 'Invalid or expired token. Please log in again.'
        }

    if response is not None:
        if response.status_code == 400:
            response.data = {
                'status_code': response.status_code,
                'error': 'Validation error.',
                'details': response.data
            }
        else:
            response.data = {
                'status_code': response.status_code,
                'error': response.data.get('detail', 'An error occurred. Please try again.')
            }
    return response
