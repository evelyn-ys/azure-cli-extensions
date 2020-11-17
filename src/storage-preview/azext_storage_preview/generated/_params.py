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
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import resource_group_name_type
from azext_storage_preview.action import (
    AddPermissionScopes,
    AddSshAuthorizedKeys
)


def load_arguments(self, _):

    with self.argument_context('storage account local-user list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='The name of the storage account within the specified resource '
                   'group. Storage account names must be between 3 and 24 characters in length and use numbers and '
                   'lower-case letters only. Swagger name=accountName')

    with self.argument_context('storage account local-user show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='The name of the storage account within the specified resource '
                   'group. Storage account names must be between 3 and 24 characters in length and use numbers and '
                   'lower-case letters only. Swagger name=accountName', id_part='name')
        c.argument('username', type=str, help='The name of local user. The username must contain lowercase letters and '
                   'numbers only. It must be unique only within the storage account. Swagger name=username',
                   id_part='child_name_1')

    with self.argument_context('storage account local-user create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='The name of the storage account within the specified resource '
                   'group. Storage account names must be between 3 and 24 characters in length and use numbers and '
                   'lower-case letters only. Swagger name=accountName')
        c.argument('username', type=str, help='The name of local user. The username must contain lowercase letters and '
                   'numbers only. It must be unique only within the storage account. Swagger name=username')
        c.argument('permission_scopes', action=AddPermissionScopes, nargs='*', help='The permission scopes of the '
                   'local user. Swagger name=permissionScopes')
        c.argument('home_directory', type=str, help='Optional, local user home directory. Swagger name=homeDirectory')
        c.argument('ssh_authorized_keys', action=AddSshAuthorizedKeys, nargs='*', help='Optional, local user ssh '
                   'authorized keys for SFTP. Swagger name=sshAuthorizedKeys')

    with self.argument_context('storage account local-user update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='The name of the storage account within the specified resource '
                   'group. Storage account names must be between 3 and 24 characters in length and use numbers and '
                   'lower-case letters only. Swagger name=accountName', id_part='name')
        c.argument('username', type=str, help='The name of local user. The username must contain lowercase letters and '
                   'numbers only. It must be unique only within the storage account. Swagger name=username',
                   id_part='child_name_1')
        c.argument('permission_scopes', action=AddPermissionScopes, nargs='*', help='The permission scopes of the '
                   'local user. Swagger name=permissionScopes')
        c.argument('home_directory', type=str, help='Optional, local user home directory. Swagger name=homeDirectory')
        c.argument('ssh_authorized_keys', action=AddSshAuthorizedKeys, nargs='*', help='Optional, local user ssh '
                   'authorized keys for SFTP. Swagger name=sshAuthorizedKeys')

    with self.argument_context('storage account local-user delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='The name of the storage account within the specified resource '
                   'group. Storage account names must be between 3 and 24 characters in length and use numbers and '
                   'lower-case letters only. Swagger name=accountName', id_part='name')
        c.argument('username', type=str, help='The name of local user. The username must contain lowercase letters and '
                   'numbers only. It must be unique only within the storage account. Swagger name=username',
                   id_part='child_name_1')

    with self.argument_context('storage account local-user list-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='The name of the storage account within the specified resource '
                   'group. Storage account names must be between 3 and 24 characters in length and use numbers and '
                   'lower-case letters only. Swagger name=accountName')
        c.argument('username', type=str, help='The name of local user. The username must contain lowercase letters and '
                   'numbers only. It must be unique only within the storage account. Swagger name=username')
