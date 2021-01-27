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

helps['ad'] = """
type: group
short-summary: Manage Azure Active Directory related entities and resources.
"""

helps['ad ds'] = """
type: group
short-summary: Manage domain service with azure active directory
"""

helps['ad ds list'] = """
type: command
short-summary: "List domain services in resource group or in subscription."
examples:
  - name: List Domain Service By Group
    text: |-
           az ad ds list --resource-group "TestResourceGroup"
  - name: List Domain Service By Sub
    text: |-
           az ad ds list
"""

helps['ad ds show'] = """
type: command
short-summary: "Get the specified domain service."
examples:
  - name: Get Domain Service
    text: |-
           az ad ds show --name "TestDomainService.com" --resource-group "TestResourceGroup"
"""

helps['ad ds create'] = """
type: command
short-summary: "Create a new domain service with the specified parameters."
parameters:
  - name: --replica-sets
    short-summary: "List of ReplicaSets"
    long-summary: |
        Usage: --replica-sets location=XX subnet-id=XX

        location: Virtual network location
        subnet-id: The id of the subnet that Domain Services will be deployed on.

        Multiple actions can be specified by using more than one --replica-sets argument.
  - name: --settings
    short-summary: "List of settings for Resource Forest. This can be either a JSON-formatted string or the location to a file containing the JSON object."
    long-summary: |
        The format of the settings JSON object for Resource Forest:
        [
            {
                'trusted_domain_fqdn': 'XX',
                'trust_direction': 'XX',
                'friendly_name': 'XX',
                'remote_dns_ips': 'XX',
                'trust_password': 'XX'
            },
            ...n
        ]
examples:
  - name: Create Domain Service
    text: |-
           az ad ds create --domain "TestDS.com" --replica-sets location="West US" subnet-id="<subnetId>" --name "TestDS.com" --resource-group "rg"
  - name: Create Domain Service with specified settings (Line breaks for legibility only)
    text: |-
           az ad ds create --domain "TestDS.com" --replica-sets location="West US" subnet-id="<subnetId>" --name "TestDS.com" --resource-group "rg"
           --ntlm-v1 "Enabled" --sync-ntlm-pwd "Enabled" --tls-v1 "Disabled" --filtered-sync "Enabled" --external-access "Enabled"
           --ldaps "Enabled" --pfx-cert "cert or path to cert" --pfx-cert-pwd "<pfxCertificatePassword>"
           --notify-others "a@gmail.com" "b@gmail.com" --notify-dc-admins "Enabled" --notify-global-admins "Enabled"
"""

helps['ad ds update'] = """
type: command
short-summary: "Update the existing deployment properties for domain service."
parameters:
  - name: --replica-sets
    short-summary: "List of ReplicaSets"
    long-summary: |
        Usage: --replica-sets location=XX subnet-id=XX

        location: Virtual network location
        subnet-id: The id of the subnet that Domain Services will be deployed on.

        Multiple actions can be specified by using more than one --replica-sets argument.
  - name: --settings
    short-summary: "List of settings for Resource Forest. This can be either a JSON-formatted string or the location to a file containing the JSON object."
    long-summary: |
        The format of the settings JSON object for Resource Forest:
        [
            {
                'trusted_domain_fqdn': 'XX',
                'trust_direction': 'XX',
                'friendly_name': 'XX',
                'remote_dns_ips': 'XX',
                'trust_password': 'XX'
            },
            ...n
        ]
examples:
  - name: Update sku
    text: |-
           az ad ds update --name "TestDS.com" --resource-group "rg" --sku "Enterprise"
  - name: Update domain security settings
    text: |-
           az ad ds update --name "TestDS.com" --resource-group "rg" --ntlm-v1 "Enabled" --tls-v1 "Disabled"
  - name: Update ldaps settings
    text: |-
           az ad ds update --name "TestDS.com" --resource-group "rg" --external-access "Enabled" --ldaps "Enabled" --pfx-cert "MIIDPDCCAiSg..." --pfx-cert-pwd "<pfxCertificatePassword>"
  - name: Update notification settings
    text: |-
           az ad ds update --name "TestDS.com" --resource-group "rg" --notify-dc-admins "Enabled" --notify-global-admins "Disabled"
"""
