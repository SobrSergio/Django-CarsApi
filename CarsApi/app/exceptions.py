from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError, AuthenticationFailed

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None and isinstance(response.data, dict):
        if 'detail' in response.data:
            if response.data['detail'].code == 'no_active_account':
                return Response({
                    'status_code': 401,
                    'error': 'Неправильное имя пользователя или пароль.'
                }, status=401)
            elif response.data['detail'].code == 'authentication_failed':
                return Response({
                    'status_code': 401,
                    'error': 'Не удалось выполнить аутентификацию. Проверьте свои учетные данные.'
                }, status=401)
        elif 'detail' in response.data and isinstance(response.data['detail'], str):
            response.data = {
                'status_code': response.status_code,
                'error': response.data['detail']
            }

    if isinstance(exc, (InvalidToken, TokenError)):
        return Response({
            'status_code': 401,
            'error': 'Токен недействителен или истек. Пожалуйста, войдите снова.'
        }, status=401)


    if response is not None:
        if response.status_code == 400:
            response.data = {
                'status_code': response.status_code,
                'error': 'Ошибка валидации данных.',
                'details': response.data
            }
            
        elif response.status_code == 404:
            response.data = {
                'status_code': response.status_code,
                'error': 'Запрашиваемый ресурс не найден.'
            }
        elif response.status_code == 500:
            response.data = {
                'status_code': response.status_code,
                'error': 'Произошла непредвиденная ошибка на сервере.'
            }
        else:
            response.data = {
                'status_code': response.status_code,
                'error': response.data.get('detail', 'Произошла непредвиденная ошибка.')
            }

    return response
