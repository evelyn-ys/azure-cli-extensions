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


helps['windows-iot-services'] = """
    type: group
    short-summary: Manage service with windows iot services
"""

helps['windows-iot-services list'] = """
    type: command
    short-summary: "Get all the IoT hubs in a resource group. And Get all the IoT hubs in a subscription."
    examples:
      - name: Service_ListByResourceGroup
        text: |-
               az windows-iot-services list --resource-group "res6117"
      - name: Service_List
        text: |-
               az windows-iot-services list
"""

helps['windows-iot-services show'] = """
    type: command
    short-summary: "Get the non-security related metadata of a Windows IoT Device Service."
    examples:
      - name: Services_GetProperties
        text: |-
               az windows-iot-services show --name "service8596" --resource-group "res9407"
"""

helps['windows-iot-services create'] = """
    type: command
    short-summary: "Create the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to \
retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values \
in a new body to update the Windows IoT Device Service."
    examples:
      - name: Service_Create
        text: |-
               az windows-iot-services create --name "service4445" --location "East US" --admin-domain-name "d.e.f" \
--billing-domain-name "a.b.c" --notes "blah" --quantity 1000000 --resource-group "res9101"
"""

helps['windows-iot-services update'] = """
    type: command
    short-summary: "Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to \
retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values \
in a new body to update the Windows IoT Device Service."
    examples:
      - name: Service_Update
        text: |-
               az windows-iot-services update --name "service8596" --location "East US" --admin-domain-name "d.e.f" \
--billing-domain-name "a.b.c" --notes "blah" --quantity 1000000 --resource-group "res9407"
"""

helps['windows-iot-services delete'] = """
    type: command
    short-summary: "Delete a Windows IoT Device Service."
    examples:
      - name: Service_Delete
        text: |-
               az windows-iot-services delete --name "service2434" --resource-group "res4228"
"""
