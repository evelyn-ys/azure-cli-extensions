# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RestorableLocationResource(Model):
    """Properties of the regional restorable account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar location_name: The location of the regional restorable account.
    :vartype location_name: str
    :ivar regional_database_account_instance_id: The instance id of the
     regional restorable account.
    :vartype regional_database_account_instance_id: str
    :ivar creation_time: The creation time of the regional restorable database
     account (ISO-8601 format).
    :vartype creation_time: datetime
    :ivar deletion_time: The time at which the regional restorable database
     account has been deleted (ISO-8601 format).
    :vartype deletion_time: datetime
    """

    _validation = {
        'location_name': {'readonly': True},
        'regional_database_account_instance_id': {'readonly': True},
        'creation_time': {'readonly': True},
        'deletion_time': {'readonly': True},
    }

    _attribute_map = {
        'location_name': {'key': 'locationName', 'type': 'str'},
        'regional_database_account_instance_id': {'key': 'regionalDatabaseAccountInstanceId', 'type': 'str'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'deletion_time': {'key': 'deletionTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(RestorableLocationResource, self).__init__(**kwargs)
        self.location_name = None
        self.regional_database_account_instance_id = None
        self.creation_time = None
        self.deletion_time = None
