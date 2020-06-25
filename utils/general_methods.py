from rest_framework.response import Response
import json
from django.utils import timezone
from rest_framework.status import HTTP_400_BAD_REQUEST, \
    HTTP_405_METHOD_NOT_ALLOWED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, \
    HTTP_406_NOT_ACCEPTABLE, HTTP_403_FORBIDDEN
from config.settings import SECRET_KEY
import random

ERROR_STATUS_CODE = False
SUCCESS_STATUS_CODE = True
STATUS_KEY_NAME = 'ok'
RESULT_KEY_NAME = 'members'
ERROR_MESSAGE_KEY_NAME = 'message'
INTERNAL_SERVER_ERROR_CLIENT_MESSAGE = 'Internal Server Error'
SUCCESS_MESSAGE = 'success'



class GeneralMethods:
    request = None

    def __init__(self, request=None):
        self.request = request

    def update_request(self, request):
        self.request = request

    def get_request_data(self, request=None):
        """
            Function:       get_request_data(self, request)
            Description:    To get the json data from request
        """
        if request:
            data = request.data
        else:
            data = self.request.data
        return data

    def get_request_body(self, request=None):
        """
            Function:       get_request(self, request)
            Description:    To get all the data from request
        """
        if request:
            data = request
        else:
            data = self.request
        query_params = data.query_params
        body = data.data
        headers = self.get_headers(request)
        return query_params, body, headers

    def get_headers(self, request=None):
        """
            Function:       get_headers(self, request)
            Description:    To get all the headers from request
        """
        if request:
            data = request
        else:
            data = self.request
        regex = re.compile('^HTTP_')
        return dict((regex.sub('', header), value) for (header, value)
                    in data.META.items() if header.startswith('HTTP_'))


    @staticmethod
    def random_alphanumeric(string_length=10, caps=False):
        """Generate a random string of fixed length """
        if caps:
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        else:
            characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choice(characters) for i in range(string_length))


    def is_valid_json(self, data):
        try:
            json.loads(data)
            return True
        except:
            return False

    """
        Informational:            100 <= http status code <= 199 
        Success:                  200 <= http status code <= 299 
        Redirect:                 300 <= http status code <= 399 
        Client Error:             400 <= http status code <= 499 
        Server Error:             500 <= http status code <= 599  
    """

    def client_error(self, result):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = None
        response[ERROR_MESSAGE_KEY_NAME] = result
        return Response(response, status=HTTP_400_BAD_REQUEST)

    def success_response(self, result):
        response = dict()
        response[STATUS_KEY_NAME] = SUCCESS_STATUS_CODE
        response[RESULT_KEY_NAME] = result
        # response[ERROR_MESSAGE_KEY_NAME] = SUCCESS_MESSAGE
        return Response(response, status=HTTP_200_OK)

    def error_response(self, result=INTERNAL_SERVER_ERROR_CLIENT_MESSAGE):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = result
        return Response(response, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def param_missing_response(self, key, message):
        response = dict()
        result = dict()
        errors = list()
        errors.append(message)
        result.update({
            key: errors
        })
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = result
        return Response(response, status=HTTP_400_BAD_REQUEST)

    def unauthorized_response(self):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = 'The request requires authentication. Please login to continue.'
        return Response(response, status=HTTP_401_UNAUTHORIZED)

    def forbidden_response(self):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = 'The request requires authentication.'
        return Response(response, status=HTTP_403_FORBIDDEN)

    def method_not_allowed_response(self):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = 'Method Not Allowed'
        return Response(response, status=HTTP_405_METHOD_NOT_ALLOWED)

    def not_acceptable_response(self):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = 'Request Not Acceptable'
        return Response(response, status=HTTP_406_NOT_ACCEPTABLE)

    def custom_error_response(self, status_code, result):
        response = dict()
        response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
        response[RESULT_KEY_NAME] = dict()
        response[ERROR_MESSAGE_KEY_NAME] = result
        return Response(response, status=status_code)
