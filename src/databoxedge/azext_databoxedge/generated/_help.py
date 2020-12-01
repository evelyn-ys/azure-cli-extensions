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


helps['data-box-edge device'] = """
    type: group
    short-summary: Manage device with data box edge
"""

helps['data-box-edge device list'] = """
    type: command
    short-summary: "Gets all the Data Box Edge/Data Box Gateway devices in a resource group. And Gets all the Data Box \
Edge/Data Box Gateway devices in a subscription."
    examples:
      - name: DataBoxEdgeDeviceGetByResourceGroup
        text: |-
               az data-box-edge device list --resource-group "GroupForEdgeAutomation"
      - name: DataBoxEdgeDeviceGetBySubscription
        text: |-
               az data-box-edge device list
"""

helps['data-box-edge device show'] = """
    type: command
    short-summary: "Gets the properties of the Data Box Edge/Data Box Gateway device."
    examples:
      - name: DataBoxEdgeDeviceGetByName
        text: |-
               az data-box-edge device show --name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge device create'] = """
    type: command
    short-summary: "Create a Data Box Edge/Data Box Gateway resource."
    parameters:
      - name: --sku
        short-summary: "The SKU type."
        long-summary: |
            Usage: --sku name=XX tier=XX

            name: SKU name.
            tier: The SKU tier. This is based on the SKU name.
    examples:
      - name: DataBoxEdgeDevicePut
        text: |-
               az data-box-edge device create --location "eastus" --sku name="Edge" tier="Standard" --name \
"testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge device update'] = """
    type: command
    short-summary: "Modifies a Data Box Edge/Data Box Gateway resource."
    examples:
      - name: DataBoxEdgeDevicePatch
        text: |-
               az data-box-edge device update --name "testedgedevice" --tags Key1="value1" Key2="value2" \
--resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge device delete'] = """
    type: command
    short-summary: "Deletes the Data Box Edge/Data Box Gateway device."
    examples:
      - name: DataBoxEdgeDeviceDelete
        text: |-
               az data-box-edge device delete --name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge device download-update'] = """
    type: command
    short-summary: "Downloads the updates on a Data Box Edge/Data Box Gateway device."
    examples:
      - name: DownloadUpdatesPost
        text: |-
               az data-box-edge device download-update --name "testedgedevice" --resource-group \
"GroupForEdgeAutomation"
"""

helps['data-box-edge device install-update'] = """
    type: command
    short-summary: "Installs the updates on the Data Box Edge/Data Box Gateway device."
    examples:
      - name: InstallUpdatesPost
        text: |-
               az data-box-edge device install-update --name "testedgedevice" --resource-group \
"GroupForEdgeAutomation"
"""

helps['data-box-edge device scan-for-update'] = """
    type: command
    short-summary: "Scans for updates on a Data Box Edge/Data Box Gateway device."
    examples:
      - name: ScanForUpdatesPost
        text: |-
               az data-box-edge device scan-for-update --name "testedgedevice" --resource-group \
"GroupForEdgeAutomation"
"""

helps['data-box-edge device show-update-summary'] = """
    type: command
    short-summary: "Gets information about the availability of updates based on the last scan of the device. It also \
gets information about any ongoing download or install jobs on the device."
    examples:
      - name: UpdateSummaryGet
        text: |-
               az data-box-edge device show-update-summary --name "testedgedevice" --resource-group \
"GroupForEdgeAutomation"
"""

helps['data-box-edge device wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the data-box-edge device is met.
    examples:
      - name: Pause executing next line of CLI script until the data-box-edge device is successfully created.
        text: |-
               az data-box-edge device wait --name "testedgedevice" --resource-group "GroupForEdgeAutomation" \
--created
      - name: Pause executing next line of CLI script until the data-box-edge device is successfully deleted.
        text: |-
               az data-box-edge device wait --name "testedgedevice" --resource-group "GroupForEdgeAutomation" \
--deleted
"""

helps['data-box-edge alert'] = """
    type: group
    short-summary: Manage alert with data box edge
"""

helps['data-box-edge alert list'] = """
    type: command
    short-summary: "Gets all the alerts for a Data Box Edge/Data Box Gateway device."
    examples:
      - name: AlertGetAllInDevice
        text: |-
               az data-box-edge alert list --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge alert show'] = """
    type: command
    short-summary: "Gets an alert by name."
    examples:
      - name: AlertGet
        text: |-
               az data-box-edge alert show --name "159a00c7-8543-4343-9435-263ac87df3bb" --device-name \
"testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge bandwidth-schedule'] = """
    type: group
    short-summary: Manage bandwidth schedule with data box edge
"""

helps['data-box-edge bandwidth-schedule list'] = """
    type: command
    short-summary: "Gets all the bandwidth schedules for a Data Box Edge/Data Box Gateway device."
    examples:
      - name: BandwidthScheduleGetAllInDevice
        text: |-
               az data-box-edge bandwidth-schedule list --device-name "testedgedevice" --resource-group \
"GroupForEdgeAutomation"
"""

helps['data-box-edge bandwidth-schedule show'] = """
    type: command
    short-summary: "Gets the properties of the specified bandwidth schedule."
    examples:
      - name: BandwidthScheduleGet
        text: |-
               az data-box-edge bandwidth-schedule show --name "bandwidth-1" --device-name "testedgedevice" \
--resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge bandwidth-schedule create'] = """
    type: command
    short-summary: "Create a bandwidth schedule."
    examples:
      - name: BandwidthSchedulePut
        text: |-
               az data-box-edge bandwidth-schedule create --name "bandwidth-1" --device-name "testedgedevice" --days \
"Sunday" --days "Monday" --rate-in-mbps 100 --start "0:0:0" --stop "13:59:0" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge bandwidth-schedule update'] = """
    type: command
    short-summary: "Update a bandwidth schedule."
"""

helps['data-box-edge bandwidth-schedule delete'] = """
    type: command
    short-summary: "Deletes the specified bandwidth schedule."
    examples:
      - name: BandwidthScheduleDelete
        text: |-
               az data-box-edge bandwidth-schedule delete --name "bandwidth-1" --device-name "testedgedevice" \
--resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge bandwidth-schedule wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the data-box-edge bandwidth-schedule is met.
    examples:
      - name: Pause executing next line of CLI script until the data-box-edge bandwidth-schedule is successfully \
created.
        text: |-
               az data-box-edge bandwidth-schedule wait --name "bandwidth-1" --device-name "testedgedevice" \
--resource-group "GroupForEdgeAutomation" --created
      - name: Pause executing next line of CLI script until the data-box-edge bandwidth-schedule is successfully \
updated.
        text: |-
               az data-box-edge bandwidth-schedule wait --name "bandwidth-1" --device-name "testedgedevice" \
--resource-group "GroupForEdgeAutomation" --updated
      - name: Pause executing next line of CLI script until the data-box-edge bandwidth-schedule is successfully \
deleted.
        text: |-
               az data-box-edge bandwidth-schedule wait --name "bandwidth-1" --device-name "testedgedevice" \
--resource-group "GroupForEdgeAutomation" --deleted
"""

helps['data-box-edge'] = """
    type: group
    short-summary: Manage job with data box edge
"""

helps['data-box-edge show-job'] = """
    type: command
    short-summary: "Gets the details of a specified job on a Data Box Edge/Data Box Gateway device."
    examples:
      - name: JobsGet
        text: |-
               az data-box-edge show-job --name "159a00c7-8543-4343-9435-263ac87df3bb" --device-name "testedgedevice" \
--resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge'] = """
    type: group
    short-summary: Manage node with data box edge
"""

helps['data-box-edge list-node'] = """
    type: command
    short-summary: "Gets all the nodes currently configured under this Data Box Edge device."
    examples:
      - name: NodesGetAllInDevice
        text: |-
               az data-box-edge list-node --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge order'] = """
    type: group
    short-summary: Manage order with data box edge
"""

helps['data-box-edge order list'] = """
    type: command
    short-summary: "Lists all the orders related to a Data Box Edge/Data Box Gateway device."
    examples:
      - name: OrderGetAllInDevice
        text: |-
               az data-box-edge order list --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge order show'] = """
    type: command
    short-summary: "Gets a specific order by name."
    examples:
      - name: OrderGet
        text: |-
               az data-box-edge order show --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge order create'] = """
    type: command
    short-summary: "Create an order."
    examples:
      - name: OrderPut
        text: |-
               az data-box-edge order create --device-name "testedgedevice" --company-name "Microsoft" \
--contact-person "John Mcclane" --email-list "john@microsoft.com" --phone "(800) 426-9400" --address-line1 "Microsoft \
Corporation" --address-line2 "One Microsoft Way" --address-line3 "Redmond" --city "WA" --country "USA" --postal-code \
"98052" --state "WA" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge order update'] = """
    type: command
    short-summary: "Update an order."
"""

helps['data-box-edge order delete'] = """
    type: command
    short-summary: "Deletes the order related to the device."
    examples:
      - name: OrderDelete
        text: |-
               az data-box-edge order delete --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation"
"""

helps['data-box-edge order wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the data-box-edge order is met.
    examples:
      - name: Pause executing next line of CLI script until the data-box-edge order is successfully created.
        text: |-
               az data-box-edge order wait --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation" \
--created
      - name: Pause executing next line of CLI script until the data-box-edge order is successfully updated.
        text: |-
               az data-box-edge order wait --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation" \
--updated
      - name: Pause executing next line of CLI script until the data-box-edge order is successfully deleted.
        text: |-
               az data-box-edge order wait --device-name "testedgedevice" --resource-group "GroupForEdgeAutomation" \
--deleted
"""

helps['data-box-edge'] = """
    type: group
    short-summary: Manage sku with data box edge
"""

helps['data-box-edge list-sku'] = """
    type: command
    short-summary: "List all the available Skus in the region and information related to them."
    examples:
      - name: ListSkus
        text: |-
               az data-box-edge list-sku
"""
