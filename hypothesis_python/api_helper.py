from requests import get, post, put, delete
from requests.exceptions import ConnectionError

from hypothesis_python.domains.http_methods import HTTPMethodsEnum


class ApiHelper:
    """
    Helper class to consume an REST API
    """

    def __call__(self, **kwargs):
        """
        Method that consumes the API

        :param host: URI of the API
        :param method: HTTP method to use
        :param endpoint:  API endpoint
        :param params: URI params
        :param data:  Request body
        :param headers: Request headers
        :return: Dict with status code and content
        """
        host = kwargs.pop("host", None)
        method = kwargs.pop("method", HTTPMethodsEnum.GET)
        endpoint = kwargs.pop("endpoint", "")
        params = kwargs.pop("params", {})
        data = kwargs.pop("data", None)
        headers = kwargs.pop("headers", None)

        result = {
            "status_code": 0,
            "content": "",
            "errors": []
        }

        if method in HTTPMethodsEnum:
            if method == HTTPMethodsEnum.GET:
                action = get
            elif method == HTTPMethodsEnum.POST:
                action = post
            elif method == HTTPMethodsEnum.PUT:
                action = put
            elif method == HTTPMethodsEnum.DELETE:
                action = delete
            try:
                response = action(url=host + endpoint, headers=headers, params=params, data=data)
                result['content'] = response.content
                result['status_code'] = response.status_code
            except ConnectionError as err:
                result['errors'].append(str(err))

        return result

    def make_authorization(self):
        pass
