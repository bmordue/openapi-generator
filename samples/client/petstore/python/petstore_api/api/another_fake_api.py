# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from petstore_api.api_client import ApiClient


class AnotherFakeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    Ref: https://openapi-generator.tech
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def test_special_tags(self, client, **kwargs):  # noqa: E501
        """To test special tags  # noqa: E501

        To test special tags  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_special_tags(client, async=True)
        >>> result = thread.get()

        :param async bool
        :param Client client: client model (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.test_special_tags_with_http_info(client, **kwargs)  # noqa: E501
        else:
            (data) = self.test_special_tags_with_http_info(client, **kwargs)  # noqa: E501
            return data

    def test_special_tags_with_http_info(self, client, **kwargs):  # noqa: E501
        """To test special tags  # noqa: E501

        To test special tags  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_special_tags_with_http_info(client, async=True)
        >>> result = thread.get()

        :param async bool
        :param Client client: client model (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_special_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client' is set
        if ('client' not in params or
                params['client'] is None):
            raise ValueError("Missing the required parameter `client` when calling `test_special_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client' in params:
            body_params = params['client']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/another-fake/dummy', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Client',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
