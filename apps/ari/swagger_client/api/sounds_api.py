# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SoundsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sounds_get(self, **kwargs):  # noqa: E501
        """List all sounds.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sounds_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :param str lang: Lookup sound for a specific language.
        :param str format: Lookup sound in a specific format.
        :return: list[Sound]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sounds_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sounds_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def sounds_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all sounds.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sounds_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :param str lang: Lookup sound for a specific language.
        :param str format: Lookup sound in a specific format.
        :return: list[Sound]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_asterisk_id', 'lang', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sounds_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sounds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Sound]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sounds_sound_id_get(self, sound_id, **kwargs):  # noqa: E501
        """Get a sound's details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sounds_sound_id_get(sound_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sound_id: Sound's id (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Sound
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sounds_sound_id_get_with_http_info(sound_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sounds_sound_id_get_with_http_info(sound_id, **kwargs)  # noqa: E501
            return data

    def sounds_sound_id_get_with_http_info(self, sound_id, **kwargs):  # noqa: E501
        """Get a sound's details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sounds_sound_id_get_with_http_info(sound_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sound_id: Sound's id (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Sound
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sound_id', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sounds_sound_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sound_id' is set
        if ('sound_id' not in params or
                params['sound_id'] is None):
            raise ValueError("Missing the required parameter `sound_id` when calling `sounds_sound_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sound_id' in params:
            path_params['soundId'] = params['sound_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sounds/{soundId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sound',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
