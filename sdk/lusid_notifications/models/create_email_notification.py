# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.516
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_notifications.configuration import Configuration


class CreateEmailNotification(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'description': 'str',
        'subject': 'str',
        'plain_text_body': 'str',
        'html_body': 'str',
        'email_address_to': 'list[str]',
        'email_address_cc': 'list[str]',
        'email_address_bcc': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'subject': 'subject',
        'plain_text_body': 'plainTextBody',
        'html_body': 'htmlBody',
        'email_address_to': 'emailAddressTo',
        'email_address_cc': 'emailAddressCc',
        'email_address_bcc': 'emailAddressBcc'
    }

    required_map = {
        'description': 'required',
        'subject': 'required',
        'plain_text_body': 'required',
        'html_body': 'optional',
        'email_address_to': 'required',
        'email_address_cc': 'optional',
        'email_address_bcc': 'optional'
    }

    def __init__(self, description=None, subject=None, plain_text_body=None, html_body=None, email_address_to=None, email_address_cc=None, email_address_bcc=None, local_vars_configuration=None):  # noqa: E501
        """CreateEmailNotification - a model defined in OpenAPI"
        
        :param description:  The summary of the services provided by the notification (required)
        :type description: str
        :param subject:  The subject of the email (required)
        :type subject: str
        :param plain_text_body:  The plain text body of the email (required)
        :type plain_text_body: str
        :param html_body:  The HTML body of the email (if any)
        :type html_body: str
        :param email_address_to:  'To' recipients of the email (required)
        :type email_address_to: list[str]
        :param email_address_cc:  'Cc' recipients of the email
        :type email_address_cc: list[str]
        :param email_address_bcc:  'Bcc' recipients of the email
        :type email_address_bcc: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._subject = None
        self._plain_text_body = None
        self._html_body = None
        self._email_address_to = None
        self._email_address_cc = None
        self._email_address_bcc = None
        self.discriminator = None

        self.description = description
        self.subject = subject
        self.plain_text_body = plain_text_body
        self.html_body = html_body
        self.email_address_to = email_address_to
        self.email_address_cc = email_address_cc
        self.email_address_bcc = email_address_bcc

    @property
    def description(self):
        """Gets the description of this CreateEmailNotification.  # noqa: E501

        The summary of the services provided by the notification  # noqa: E501

        :return: The description of this CreateEmailNotification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEmailNotification.

        The summary of the services provided by the notification  # noqa: E501

        :param description: The description of this CreateEmailNotification.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 512):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def subject(self):
        """Gets the subject of this CreateEmailNotification.  # noqa: E501

        The subject of the email  # noqa: E501

        :return: The subject of this CreateEmailNotification.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CreateEmailNotification.

        The subject of the email  # noqa: E501

        :param subject: The subject of this CreateEmailNotification.  # noqa: E501
        :type subject: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) > 1024):
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) < 1):
            raise ValueError("Invalid value for `subject`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and not re.search(r'^[\s\S]*$', subject)):  # noqa: E501
            raise ValueError(r"Invalid value for `subject`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._subject = subject

    @property
    def plain_text_body(self):
        """Gets the plain_text_body of this CreateEmailNotification.  # noqa: E501

        The plain text body of the email  # noqa: E501

        :return: The plain_text_body of this CreateEmailNotification.  # noqa: E501
        :rtype: str
        """
        return self._plain_text_body

    @plain_text_body.setter
    def plain_text_body(self, plain_text_body):
        """Sets the plain_text_body of this CreateEmailNotification.

        The plain text body of the email  # noqa: E501

        :param plain_text_body: The plain_text_body of this CreateEmailNotification.  # noqa: E501
        :type plain_text_body: str
        """
        if self.local_vars_configuration.client_side_validation and plain_text_body is None:  # noqa: E501
            raise ValueError("Invalid value for `plain_text_body`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plain_text_body is not None and len(plain_text_body) > 2147483647):
            raise ValueError("Invalid value for `plain_text_body`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plain_text_body is not None and len(plain_text_body) < 1):
            raise ValueError("Invalid value for `plain_text_body`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plain_text_body is not None and not re.search(r'^[\s\S]*$', plain_text_body)):  # noqa: E501
            raise ValueError(r"Invalid value for `plain_text_body`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._plain_text_body = plain_text_body

    @property
    def html_body(self):
        """Gets the html_body of this CreateEmailNotification.  # noqa: E501

        The HTML body of the email (if any)  # noqa: E501

        :return: The html_body of this CreateEmailNotification.  # noqa: E501
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body):
        """Sets the html_body of this CreateEmailNotification.

        The HTML body of the email (if any)  # noqa: E501

        :param html_body: The html_body of this CreateEmailNotification.  # noqa: E501
        :type html_body: str
        """
        if (self.local_vars_configuration.client_side_validation and
                html_body is not None and len(html_body) > 2147483647):
            raise ValueError("Invalid value for `html_body`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                html_body is not None and len(html_body) < 1):
            raise ValueError("Invalid value for `html_body`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                html_body is not None and not re.search(r'^[\s\S]*$', html_body)):  # noqa: E501
            raise ValueError(r"Invalid value for `html_body`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._html_body = html_body

    @property
    def email_address_to(self):
        """Gets the email_address_to of this CreateEmailNotification.  # noqa: E501

        'To' recipients of the email  # noqa: E501

        :return: The email_address_to of this CreateEmailNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_to

    @email_address_to.setter
    def email_address_to(self, email_address_to):
        """Sets the email_address_to of this CreateEmailNotification.

        'To' recipients of the email  # noqa: E501

        :param email_address_to: The email_address_to of this CreateEmailNotification.  # noqa: E501
        :type email_address_to: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_address_to is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address_to`, must not be `None`")  # noqa: E501

        self._email_address_to = email_address_to

    @property
    def email_address_cc(self):
        """Gets the email_address_cc of this CreateEmailNotification.  # noqa: E501

        'Cc' recipients of the email  # noqa: E501

        :return: The email_address_cc of this CreateEmailNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_cc

    @email_address_cc.setter
    def email_address_cc(self, email_address_cc):
        """Sets the email_address_cc of this CreateEmailNotification.

        'Cc' recipients of the email  # noqa: E501

        :param email_address_cc: The email_address_cc of this CreateEmailNotification.  # noqa: E501
        :type email_address_cc: list[str]
        """

        self._email_address_cc = email_address_cc

    @property
    def email_address_bcc(self):
        """Gets the email_address_bcc of this CreateEmailNotification.  # noqa: E501

        'Bcc' recipients of the email  # noqa: E501

        :return: The email_address_bcc of this CreateEmailNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_bcc

    @email_address_bcc.setter
    def email_address_bcc(self, email_address_bcc):
        """Sets the email_address_bcc of this CreateEmailNotification.

        'Bcc' recipients of the email  # noqa: E501

        :param email_address_bcc: The email_address_bcc of this CreateEmailNotification.  # noqa: E501
        :type email_address_bcc: list[str]
        """

        self._email_address_bcc = email_address_bcc

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateEmailNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateEmailNotification):
            return True

        return self.to_dict() != other.to_dict()
