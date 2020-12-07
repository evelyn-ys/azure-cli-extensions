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

from knack.help_files import helps


helps['storage local-user'] = """
    type: group
    short-summary: Manage local user with storage
"""

helps['storage local-user list'] = """
    type: command
    short-summary: "List the local users associated with the storage account."
    examples:
      - name: StorageAccountListLocalUsers
        text: |-
               az storage local-user list --account-name "sto2527" --resource-group "res6977"
"""

helps['storage local-user show'] = """
    type: command
    short-summary: "Get the local user of the storage account by username."
    examples:
      - name: StorageAccountGetLocalUser
        text: |-
               az storage local-user show --account-name "sto2527" --resource-group "res6977" --username "user1"
"""

helps['storage local-user create'] = """
    type: command
    short-summary: "Create the local user properties of the storage account."
    parameters:
      - name: --permission-scopes
        short-summary: "The permission scopes of the local user."
        long-summary: |
            Usage: --permission-scopes permissions=XX service=XX resource-name=XX

            permissions: The permissions for the local user. Possible values include: Read (r), Write (w), Delete (d), \
List (l), and Create (c).
            service: The service used by the local user, e.g. blob, file.
            resource-name: The name of resource used by the local user.

            Multiple actions can be specified by using more than one --permission-scopes argument.
      - name: --ssh-authorized-keys
        short-summary: "Optional, local user ssh authorized keys for SFTP."
        long-summary: |
            Usage: --ssh-authorized-keys description=XX key=XX

            description: Optional
            key: Ssh public key base64 encoded

            Multiple actions can be specified by using more than one --ssh-authorized-keys argument.
    examples:
      - name: StorageAccountCreateLocalUsers
        text: |-
               az storage local-user create --account-name "sto2527" --permission-scopes permissions="rwd" \
resource-name="share1" service="file" --permission-scopes permissions="r" resource-name="share2" service="file" \
--resource-group "res6977" --username "user1"
"""

helps['storage local-user update'] = """
    type: command
    short-summary: "Update the local user properties of the storage account."
    parameters:
      - name: --permission-scopes
        short-summary: "The permission scopes of the local user."
        long-summary: |
            Usage: --permission-scopes permissions=XX service=XX resource-name=XX

            permissions: The permissions for the local user. Possible values include: Read (r), Write (w), Delete (d), \
List (l), and Create (c).
            service: The service used by the local user, e.g. blob, file.
            resource-name: The name of resource used by the local user.

            Multiple actions can be specified by using more than one --permission-scopes argument.
      - name: --ssh-authorized-keys
        short-summary: "Optional, local user ssh authorized keys for SFTP."
        long-summary: |
            Usage: --ssh-authorized-keys description=XX key=XX

            description: Optional
            key: Ssh public key base64 encoded

            Multiple actions can be specified by using more than one --ssh-authorized-keys argument.
    examples:
      - name: StorageAccountUpdateLocalUsers
        text: |-
               az storage local-user update --account-name "sto2527" --resource-group "res6977" --username "user1"
"""

helps['storage local-user delete'] = """
    type: command
    short-summary: "Deletes the local user associated with the specified storage account."
    examples:
      - name: StorageAccountDeleteLocalUsers
        text: |-
               az storage local-user delete --account-name "sto2527" --resource-group "res6977" --username "user1"
"""

helps['storage local-user list-key'] = """
    type: command
    short-summary: "List the local user keys."
    examples:
      - name: StorageAccountListLocalUserKeys
        text: |-
               az storage local-user list-key --account-name "sto2527" --resource-group "res6977" --username "user1"
"""
