# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ChannelUserevent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bridge': 'Bridge',
        'channel': 'Channel',
        'endpoint': 'Endpoint',
        'eventname': 'str',
        'userevent': 'object'
    }

    attribute_map = {
        'bridge': 'bridge',
        'channel': 'channel',
        'endpoint': 'endpoint',
        'eventname': 'eventname',
        'userevent': 'userevent'
    }

    def __init__(self, bridge=None, channel=None, endpoint=None, eventname=None, userevent=None):  # noqa: E501
        """ChannelUserevent - a model defined in Swagger"""  # noqa: E501

        self._bridge = None
        self._channel = None
        self._endpoint = None
        self._eventname = None
        self._userevent = None
        self.discriminator = None

        if bridge is not None:
            self.bridge = bridge
        if channel is not None:
            self.channel = channel
        if endpoint is not None:
            self.endpoint = endpoint
        self.eventname = eventname
        self.userevent = userevent

    @property
    def bridge(self):
        """Gets the bridge of this ChannelUserevent.  # noqa: E501

        A bridge that is signaled with the user event.  # noqa: E501

        :return: The bridge of this ChannelUserevent.  # noqa: E501
        :rtype: Bridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this ChannelUserevent.

        A bridge that is signaled with the user event.  # noqa: E501

        :param bridge: The bridge of this ChannelUserevent.  # noqa: E501
        :type: Bridge
        """

        self._bridge = bridge

    @property
    def channel(self):
        """Gets the channel of this ChannelUserevent.  # noqa: E501

        A channel that is signaled with the user event.  # noqa: E501

        :return: The channel of this ChannelUserevent.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelUserevent.

        A channel that is signaled with the user event.  # noqa: E501

        :param channel: The channel of this ChannelUserevent.  # noqa: E501
        :type: Channel
        """

        self._channel = channel

    @property
    def endpoint(self):
        """Gets the endpoint of this ChannelUserevent.  # noqa: E501

        A endpoint that is signaled with the user event.  # noqa: E501

        :return: The endpoint of this ChannelUserevent.  # noqa: E501
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ChannelUserevent.

        A endpoint that is signaled with the user event.  # noqa: E501

        :param endpoint: The endpoint of this ChannelUserevent.  # noqa: E501
        :type: Endpoint
        """

        self._endpoint = endpoint

    @property
    def eventname(self):
        """Gets the eventname of this ChannelUserevent.  # noqa: E501

        The name of the user event.  # noqa: E501

        :return: The eventname of this ChannelUserevent.  # noqa: E501
        :rtype: str
        """
        return self._eventname

    @eventname.setter
    def eventname(self, eventname):
        """Sets the eventname of this ChannelUserevent.

        The name of the user event.  # noqa: E501

        :param eventname: The eventname of this ChannelUserevent.  # noqa: E501
        :type: str
        """
        if eventname is None:
            raise ValueError("Invalid value for `eventname`, must not be `None`")  # noqa: E501

        self._eventname = eventname

    @property
    def userevent(self):
        """Gets the userevent of this ChannelUserevent.  # noqa: E501

        Custom Userevent data  # noqa: E501

        :return: The userevent of this ChannelUserevent.  # noqa: E501
        :rtype: object
        """
        return self._userevent

    @userevent.setter
    def userevent(self, userevent):
        """Sets the userevent of this ChannelUserevent.

        Custom Userevent data  # noqa: E501

        :param userevent: The userevent of this ChannelUserevent.  # noqa: E501
        :type: object
        """
        if userevent is None:
            raise ValueError("Invalid value for `userevent`, must not be `None`")  # noqa: E501

        self._userevent = userevent

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ChannelUserevent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChannelUserevent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
