# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import StorageManagementClientConfiguration
from .operations import Operations
from .operations import SkusOperations
from .operations import StorageAccountsOperations
from .operations import DeletedAccountsOperations
from .operations import UsagesOperations
from .operations import ManagementPoliciesOperations
from .operations import BlobInventoryPoliciesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ObjectReplicationPoliciesOperations
from .operations import LocalUsersOperations
from .operations import EncryptionScopesOperations
from .operations import BlobServicesOperations
from .operations import BlobContainersOperations
from .operations import FileServicesOperations
from .operations import FileSharesOperations
from .operations import QueueServicesOperations
from .operations import QueueOperations
from .operations import TableServicesOperations
from .operations import TableOperations
from . import models


class StorageManagementClient(object):
    """The Azure Storage Management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2020_08_01_preview.operations.Operations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.storage.v2020_08_01_preview.operations.SkusOperations
    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts: azure.mgmt.storage.v2020_08_01_preview.operations.StorageAccountsOperations
    :ivar deleted_accounts: DeletedAccountsOperations operations
    :vartype deleted_accounts: azure.mgmt.storage.v2020_08_01_preview.operations.DeletedAccountsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.storage.v2020_08_01_preview.operations.UsagesOperations
    :ivar management_policies: ManagementPoliciesOperations operations
    :vartype management_policies: azure.mgmt.storage.v2020_08_01_preview.operations.ManagementPoliciesOperations
    :ivar blob_inventory_policies: BlobInventoryPoliciesOperations operations
    :vartype blob_inventory_policies: azure.mgmt.storage.v2020_08_01_preview.operations.BlobInventoryPoliciesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.storage.v2020_08_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.storage.v2020_08_01_preview.operations.PrivateLinkResourcesOperations
    :ivar object_replication_policies: ObjectReplicationPoliciesOperations operations
    :vartype object_replication_policies: azure.mgmt.storage.v2020_08_01_preview.operations.ObjectReplicationPoliciesOperations
    :ivar local_users: LocalUsersOperations operations
    :vartype local_users: azure.mgmt.storage.v2020_08_01_preview.operations.LocalUsersOperations
    :ivar encryption_scopes: EncryptionScopesOperations operations
    :vartype encryption_scopes: azure.mgmt.storage.v2020_08_01_preview.operations.EncryptionScopesOperations
    :ivar blob_services: BlobServicesOperations operations
    :vartype blob_services: azure.mgmt.storage.v2020_08_01_preview.operations.BlobServicesOperations
    :ivar blob_containers: BlobContainersOperations operations
    :vartype blob_containers: azure.mgmt.storage.v2020_08_01_preview.operations.BlobContainersOperations
    :ivar file_services: FileServicesOperations operations
    :vartype file_services: azure.mgmt.storage.v2020_08_01_preview.operations.FileServicesOperations
    :ivar file_shares: FileSharesOperations operations
    :vartype file_shares: azure.mgmt.storage.v2020_08_01_preview.operations.FileSharesOperations
    :ivar queue_services: QueueServicesOperations operations
    :vartype queue_services: azure.mgmt.storage.v2020_08_01_preview.operations.QueueServicesOperations
    :ivar queue: QueueOperations operations
    :vartype queue: azure.mgmt.storage.v2020_08_01_preview.operations.QueueOperations
    :ivar table_services: TableServicesOperations operations
    :vartype table_services: azure.mgmt.storage.v2020_08_01_preview.operations.TableServicesOperations
    :ivar table: TableOperations operations
    :vartype table: azure.mgmt.storage.v2020_08_01_preview.operations.TableOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deleted_accounts = DeletedAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_policies = ManagementPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_inventory_policies = BlobInventoryPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.object_replication_policies = ObjectReplicationPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.local_users = LocalUsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.encryption_scopes = EncryptionScopesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_services = BlobServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_services = FileServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_shares = FileSharesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queue_services = QueueServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queue = QueueOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.table_services = TableServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.table = TableOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> StorageManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
