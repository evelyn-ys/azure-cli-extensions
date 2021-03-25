# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class resource(msrest.serialization.Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class trackedresource(resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(trackedresource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)


class deviceservice(trackedresource):
    """The description of the Windows IoT Device Service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives.
    :type location: str
    :param etag: The Etag field is *not* required. If it is provided in the response body, it must
     also be provided as a header per the normal ETag convention.
    :type etag: str
    :param notes: Windows IoT Device Service notes.
    :type notes: str
    :ivar start_date: Windows IoT Device Service start date.
    :vartype start_date: ~datetime.datetime
    :param quantity: Windows IoT Device Service device allocation.
    :type quantity: long
    :param billing_domain_name: Windows IoT Device Service ODM AAD domain.
    :type billing_domain_name: str
    :param admin_domain_name: Windows IoT Device Service OEM AAD domain.
    :type admin_domain_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'start_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'notes': {'key': 'properties.notes', 'type': 'str'},
        'start_date': {'key': 'properties.startDate', 'type': 'iso-8601'},
        'quantity': {'key': 'properties.quantity', 'type': 'long'},
        'billing_domain_name': {'key': 'properties.billingDomainName', 'type': 'str'},
        'admin_domain_name': {'key': 'properties.adminDomainName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(deviceservice, self).__init__(**kwargs)
        self.etag = kwargs.get('etag', None)
        self.notes = kwargs.get('notes', None)
        self.start_date = None
        self.quantity = kwargs.get('quantity', None)
        self.billing_domain_name = kwargs.get('billing_domain_name', None)
        self.admin_domain_name = kwargs.get('admin_domain_name', None)


class deviceservicechecknameavailabilityparameters(msrest.serialization.Model):
    """Input values.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Windows IoT Device Service to check.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(deviceservicechecknameavailabilityparameters, self).__init__(**kwargs)
        self.name = kwargs['name']


class deviceservicedescriptionlistresult(msrest.serialization.Model):
    """The JSON-serialized array of DeviceService objects with a next link.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: The array of DeviceService objects.
    :type value: list[~device_services.models.deviceservice]
    :ivar next_link: The next link.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[deviceservice]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(deviceservicedescriptionlistresult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None


class deviceservicenameavailabilityinfo(msrest.serialization.Model):
    """The properties indicating whether a given Windows IoT Device Service name is available.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name_available: The value which indicates whether the provided name is available.
    :vartype name_available: bool
    :ivar reason: The reason for unavailability. Possible values include: "Invalid",
     "AlreadyExists".
    :vartype reason: str or ~device_services.models.Servicenameunavailabilityreason
    :param message: The detailed reason message.
    :type message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(deviceservicenameavailabilityinfo, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = kwargs.get('message', None)


class errordetails(msrest.serialization.Model):
    """The details of the error.

    :param error: The error object.
    :type error: ~device_services.models.errordetailserror
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'errordetailserror'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(errordetails, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class errordetailserror(msrest.serialization.Model):
    """The error object.

    :param code: One of a server-defined set of error codes.
    :type code: str
    :param message: A human-readable representation of the error.
    :type message: str
    :param target: The target of the particular error.
    :type target: str
    :param details: A human-readable representation of the error's details.
    :type details: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(errordetailserror, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)


class operationdisplayinfo(msrest.serialization.Model):
    """The operation supported by Azure Data Catalog Service.

    :param description: The description of the operation.
    :type description: str
    :param operation: The action that users can perform, based on their permission level.
    :type operation: str
    :param provider: Service provider: Azure Data Catalog Service.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(operationdisplayinfo, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.operation = kwargs.get('operation', None)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)


class operationentity(msrest.serialization.Model):
    """The operation supported by Azure Data Catalog Service.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The operation supported by Azure Data Catalog Service.
    :type display: ~device_services.models.operationdisplayinfo
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'operationdisplayinfo'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(operationentity, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.is_data_action = kwargs.get('is_data_action', None)


class operationlistresult(msrest.serialization.Model):
    """Result of the request to list Windows IoT Device Service operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Windows IoT Device Service operations supported by the
     Microsoft.WindowsIoT resource provider.
    :vartype value: list[~device_services.models.operationentity]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[operationentity]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(operationlistresult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class proxyresource(resource):
    """The resource model definition for a ARM proxy resource. It will have everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(proxyresource, self).__init__(**kwargs)
