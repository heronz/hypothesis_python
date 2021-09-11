import json
from typing import AnyStr

from hypothesis_python.api_helper import ApiHelper
from hypothesis_python.domains.http_methods import HTTPMethodsEnum
from hypothesis_python.domains.type_search import TypeSearchEnum
from hypothesis_python.logger import Logger


class HypothesisParser:
    """
    Helper class that takes care of parsing the response

    """

    @staticmethod
    def __call__(response):
        """
        Parse the responses to a dictionary

        :param response: response object from any of the methos on Hypothesis class
        :return: Dict with the content or the errors of the response
        """
        parsed_result = {}
        if response['status_code'] == 200:
            parsed_result['content'] = json.loads(response['content'].decode())
        else:
            parsed_result['errors'] = response['errors']

        return parsed_result


class HypothesisPython:
    """
    Class to consume Hypothesis API

    """
    def __init__(self, bearer_token):
        """
        Initialize some configurations:
            host: URI for consuming the API
            logger: Instance of a Logger
        """
        self.host = "https://hypothes.is/api"
        self.logger = Logger('C:/temp')
        self.api_helper = ApiHelper()
        self.auth_header = {
            "Authorization": f"Bearer {bearer_token}"
        }

    def search_annotations(self, what_to_search: AnyStr, search_type: TypeSearchEnum, limit=20, offset=0):
        """
        Method for searching annotations

        :param what_to_search: Text to search
        :param search_type: Type of the search
        :param limit: How many rows the search should return
        :param offset: How many rows the search should jump ahead
        :return: Object with the response
        """
        api_helper = ApiHelper()
        params = {
            "limit": limit,
            "offset": offset,
            search_type.value: what_to_search
        }
        response = api_helper(host=self.host, endpoint='/search', params=params, headers=self.auth_header)
        response = HypothesisParser()(response)
        self.logger.log(response)
        return response

    def get_annotation(self, id_annotation):
        """
        Method for getting a single annotation by it's ID

        :param id_annotation: ID of the desired annotation
        :return: Object with the response
        """
        api_helper = ApiHelper()
        response = api_helper(host=self.host, endpoint=f'/annotations/{id_annotation}', headers=self.auth_header)
        response = HypothesisParser()(response)
        self.logger.log(response)
        return response

    def new_annotation(self, annotation):
        """
        Method for creating a new annotation

        :param annotation: A text that should contain a JSON of a annotation according to the documentation
        :return: Object with the response
        """
        api_helper = ApiHelper()
        response = api_helper(host=self.host, endpoint='/annotations', method=HTTPMethodsEnum.POST, data=annotation,
                              headers=self.auth_header)
        response = HypothesisParser()(response)
        self.logger.log(response)
        return response

    def delete_annotation(self, id_annotation):
        """
        Method for deleting a new annotation

        :param id_annotation: ID of the desired annotation for deletion
        :return: Object with the response
        """
        api_helper = ApiHelper()
        response = api_helper(host=self.host, endpoint=f'/annotations/{id_annotation}', method=HTTPMethodsEnum.DELETE,
                              headers=self.auth_header)
        response = HypothesisParser()(response)
        self.logger.log(response)
        return response

