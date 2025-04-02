# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

logger = get_logger(__name__)


def sfi_ar_1_2_3_warning(command, args):
    if not command or command not in ['aks create','aks update']:
        return

    WARNING_MSG = '''[SFI-AR-1.2.3 Warning]
All first-party services using AKS must utilize AKS Node OS Auto Upgrade feature to keep the underlying node OS and components deployed by AKS patched.
Command reference:
    az aks create --resource-group <resource group> --name <resource> --node-os-upgrade-channel NodeImage
    az aks update --resource-group <resource group> --name <resource> --node-os-upgrade-channel NodeImage
Links:
    https://eng.ms/docs/more/containers-secure-supply-chain/tsg-aks-node-auto-upgrade
    https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-node-os-image?tabs=azure-cli
    '''

    if command == 'aks create':
        if hasattr(args, 'node_os_upgrade_channel') and args.node_os_upgrade_channel == 'NodeImage':
            return
        logger.warning(WARNING_MSG)

    if command == 'aks update':
        if not hasattr(args, 'node_os_upgrade_channel') or args.node_os_upgrade_channel == 'NodeImage':
            return
        logger.warning(WARNING_MSG)


def sfi_id_4_1_1_warning(command, args):
    if not command or command != 'ad app credential reset':
        return

    WARNING_MSG = '''[SFI-ID-4.1.1 Warning]
Eliminate internal usage of unmanaged secrets to authenticate to Azure resources.
Links:
    https://eng.ms/docs/products/onecert-certificates-key-vault-and-dsms/key-vault-dsms/certandsecretmngmt/tsg/aadappapasswordcert
    '''
    logger.warning(WARNING_MSG)


def sfi_warning_handler(_, **kwargs):
    """
    An event handler for SFI warning when EVENT_INVOKER_POST_PARSE_ARGS event is invoked.
    """
    command = kwargs.get('command')
    args = kwargs.get('args')
    warning_funcs = [sfi_ar_1_2_3_warning]
    for warning_func in warning_funcs:
        warning_func(command, args)
