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


class BridgeVarset(object):
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
        'value': 'str',
        'variable': 'str'
    }

    attribute_map = {
        'bridge': 'bridge',
        'value': 'value',
        'variable': 'variable'
    }

    def __init__(self, bridge=None, value=None, variable=None):  # noqa: E501
        """BridgeVarset - a model defined in Swagger"""  # noqa: E501

        self._bridge = None
        self._value = None
        self._variable = None
        self.discriminator = None

        if bridge is not None:
            self.bridge = bridge
        self.value = value
        self.variable = variable

    @property
    def bridge(self):
        """Gets the bridge of this BridgeVarset.  # noqa: E501

        The bridge on which the variable was set.  # noqa: E501

        :return: The bridge of this BridgeVarset.  # noqa: E501
        :rtype: Bridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this BridgeVarset.

        The bridge on which the variable was set.  # noqa: E501

        :param bridge: The bridge of this BridgeVarset.  # noqa: E501
        :type: Bridge
        """

        self._bridge = bridge

    @property
    def value(self):
        """Gets the value of this BridgeVarset.  # noqa: E501

        The new value of the variable.  # noqa: E501

        :return: The value of this BridgeVarset.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BridgeVarset.

        The new value of the variable.  # noqa: E501

        :param value: The value of this BridgeVarset.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def variable(self):
        """Gets the variable of this BridgeVarset.  # noqa: E501

        The variable that changed.  # noqa: E501

        :return: The variable of this BridgeVarset.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this BridgeVarset.

        The variable that changed.  # noqa: E501

        :param variable: The variable of this BridgeVarset.  # noqa: E501
        :type: str
        """
        if variable is None:
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501

        self._variable = variable

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
        if issubclass(BridgeVarset, dict):
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
        if not isinstance(other, BridgeVarset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
