# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /Services/put/Service_Create
@try_manual
def step_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az windows-iot-services create '
             '--name "{wiot}" '
             '--location "East US" '
             '--admin-domain-name "{domain}" '
             '--billing-domain-name "{domain}" '
             '--notes "notes" '
             '--quantity 100 '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Services/get/Service_List
@try_manual
def step_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az windows-iot-services list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Services/get/Service_ListByResourceGroup
@try_manual
def step_list2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az windows-iot-services list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Services/get/Services_GetProperties
@try_manual
def step_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az windows-iot-services show '
             '--name "{wiot}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Services/patch/Service_Update
@try_manual
def step_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az windows-iot-services update '
             '--name "{wiot}" '
             '--admin-domain-name "{domain}" '
             '--billing-domain-name "{domain}" '
             '--notes "new notes" '
             '--quantity 300 '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Services/delete/Service_Delete
@try_manual
def step_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az windows-iot-services delete -y '
             '--name "{wiot}" '
             '--resource-group "{rg}"',
             checks=checks)
