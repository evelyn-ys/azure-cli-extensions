# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def storage_local_user_list(client,
                            resource_group_name,
                            account_name):
    return client.list(resource_group_name=resource_group_name,
                       account_name=account_name)


def storage_local_user_show(client,
                            resource_group_name,
                            account_name,
                            username):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      username=username)


def storage_local_user_create(client,
                              resource_group_name,
                              account_name,
                              username,
                              permission_scopes=None,
                              home_directory=None,
                              ssh_authorized_keys=None):
    properties = {}
    properties['permission_scopes'] = permission_scopes
    properties['home_directory'] = home_directory
    properties['ssh_authorized_keys'] = ssh_authorized_keys
    return client.create_or_update(resource_group_name=resource_group_name,
                                   account_name=account_name,
                                   username=username,
                                   properties=properties)


def storage_local_user_update(client,
                              resource_group_name,
                              account_name,
                              username,
                              permission_scopes=None,
                              home_directory=None,
                              ssh_authorized_keys=None):
    properties = {}
    properties['permission_scopes'] = permission_scopes
    properties['home_directory'] = home_directory
    properties['ssh_authorized_keys'] = ssh_authorized_keys
    return client.create_or_update(resource_group_name=resource_group_name,
                                   account_name=account_name,
                                   username=username,
                                   properties=properties)


def storage_local_user_delete(client,
                              resource_group_name,
                              account_name,
                              username):
    return client.delete(resource_group_name=resource_group_name,
                         account_name=account_name,
                         username=username)


def storage_local_user_list_key(client,
                                resource_group_name,
                                account_name,
                                username):
    return client.list_keys(resource_group_name=resource_group_name,
                            account_name=account_name,
                            username=username)
