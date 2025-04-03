# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

logger = get_logger(__name__)


def sfi_ar_1_2_3_warning(command, args):
    if not command or command not in ['aks create', 'aks update']:
        return

    warning_msg = '''[SFI-AR-1.2.3 Warning] All first-party services using AKS must utilize AKS Node OS Auto Upgrade feature to keep the underlying node OS and components deployed by AKS patched.
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
        logger.warning(warning_msg)

    if command == 'aks update':
        if not hasattr(args, 'node_os_upgrade_channel') or args.node_os_upgrade_channel == 'NodeImage':
            return
        logger.warning(warning_msg)


def sfi_id_4_1_1_warning(command, args):
    if not command or command != 'ad app credential reset':
        return

    warning_msg = '''[SFI-ID-4.1.1 Warning] Eliminate internal usage of unmanaged secrets to authenticate to Azure resources.
Links:https://eng.ms/docs/products/onecert-certificates-key-vault-and-dsms/key-vault-dsms/certandsecretmngmt/tsg/aadappapasswordcert
    '''
    logger.warning(warning_msg)


def sfi_id_4_2_1_warning(command, args):
    if not command or command not in ['storage account create', 'storage account update']:
        return

    warning_msg = '''[SFI-ID-4.2.1 Warning] Eliminate internal usage of unmanaged secrets to authenticate to Azure resources.
Command reference:
    az storage account create --resource-group <resource group> --name <resource> --allow-shared-key-access false
    az storage account update --resource-group <resource group> --name <resource> --allow-shared-key-access false
Links:https://eng.ms/docs/products/azure-storage/security/standards/identity-based-access
    '''
    if command == 'storage account create':
        if hasattr(args, 'allow_shared_key_access') and args.allow_shared_key_access is False:
            return
        logger.warning(warning_msg)

    if command == 'storage account update':
        if not hasattr(args, 'allow_shared_key_access') or args.allow_shared_key_access is False:
            return
        logger.warning(warning_msg)


def sfi_ti_2_3_3_warning(command, args):
    if not command or command not in ['storage account create', 'storage account update']:
        return

    warning_msg = '''[SFI-TI-2.3.3 Warning] Azure Blob Storage supports anonymous read access to containers and blobs. This feature allows blobs within storage accounts to be accessible to the public internet. This presents a security risk as Microsoft confidential information can be unintentionally stored within these storage accounts and exposed to the public internet.
Command reference:
    az storage account create --resource-group <resource group> --name <resource> --allow-blob-public-access false
    az storage account update --resource-group <resource group> --name <resource> --allow-blob-public-access false
Links:https://eng.ms/docs/cloud-ai-platform/azure-edge-platform-aep/aep-engineering-systems/aep-documentation/disable-anonymous-blobs
        '''
    if command == 'storage account create':
        if hasattr(args, 'allow_blob_public_access') and args.allow_blob_public_access is False:
            return
        logger.warning(warning_msg)

    if command == 'storage account update':
        if not hasattr(args, 'allow_blob_public_access') or args.allow_blob_public_access is False:
            return
        logger.warning(warning_msg)


def sfi_ti_3_4_warning(command, args):
    if not command or command != 'ad app create':
        return

    warning_msg = '''[SFI-TI-3.4 Warning] All Entra apps in MSFT-owned tenants must include service tree ID that the app should be attributed to.
Command reference: az ad app create --display-name <app> --service-management-reference <service tree id>
Links:
    https://eng.ms/docs/microsoft-security/digital-security-and-resilience/sr-risk-management/infra-security-engineering/enterprise-sec-eng-standards/security-baseline-for-entra-id-tenants/tsgs/entraidappregistrationsmustmaptoavalidservicewithinservicetree
    https://eng.ms/docs/cloud-ai-platform/azure-core/azure-experiences-and-ecosystems/azure-portal-and-client-tools-ruhim/azure-cli-tools-azure-cli-powershell-and-terraform/azure-cli-tools/teams_docs/common/s360_tsgs/sfi_ti342
            '''
    if hasattr(args, 'service_management_reference') and args.service_management_reference:
        return
    logger.warning(warning_msg)


def sfi_warning_handler(_, **kwargs):
    """
    An event handler for SFI warning when EVENT_INVOKER_POST_PARSE_ARGS event is invoked.
    """
    command = kwargs.get('command')
    args = kwargs.get('args')
    warning_funcs = [sfi_ar_1_2_3_warning, sfi_id_4_1_1_warning, sfi_id_4_2_1_warning, sfi_ti_2_3_3_warning, sfi_ti_3_4_warning]
    for warning_func in warning_funcs:
        warning_func(command, args)
