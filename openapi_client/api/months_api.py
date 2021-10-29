"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.month_detail_response import MonthDetailResponse
from openapi_client.model.month_summaries_response import MonthSummariesResponse


class MonthsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_budget_month_endpoint = _Endpoint(
            settings={
                'response_type': (MonthDetailResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/budgets/{budget_id}/months/{month}',
                'operation_id': 'get_budget_month',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'month',
                ],
                'required': [
                    'budget_id',
                    'month',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'budget_id':
                        (str,),
                    'month':
                        (date,),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                    'month': 'month',
                },
                'location_map': {
                    'budget_id': 'path',
                    'month': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_budget_months_endpoint = _Endpoint(
            settings={
                'response_type': (MonthSummariesResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/budgets/{budget_id}/months',
                'operation_id': 'get_budget_months',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'last_knowledge_of_server',
                ],
                'required': [
                    'budget_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'budget_id':
                        (str,),
                    'last_knowledge_of_server':
                        (int,),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                    'last_knowledge_of_server': 'last_knowledge_of_server',
                },
                'location_map': {
                    'budget_id': 'path',
                    'last_knowledge_of_server': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_budget_month(
        self,
        budget_id,
        month,
        **kwargs
    ):
        """Single budget month  # noqa: E501

        Returns a single budget month  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_budget_month(budget_id, month, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
            month (date): The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MonthDetailResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        kwargs['month'] = \
            month
        return self.get_budget_month_endpoint.call_with_http_info(**kwargs)

    def get_budget_months(
        self,
        budget_id,
        **kwargs
    ):
        """List budget months  # noqa: E501

        Returns all budget months  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_budget_months(budget_id, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).

        Keyword Args:
            last_knowledge_of_server (int): The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MonthSummariesResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        return self.get_budget_months_endpoint.call_with_http_info(**kwargs)
