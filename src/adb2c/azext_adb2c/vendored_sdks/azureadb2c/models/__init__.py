# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AsyncOperationStatus
    from ._models_py3 import AsyncOperationStatusError
    from ._models_py3 import B2CResourceSku
    from ._models_py3 import B2CTenantResource
    from ._models_py3 import B2CTenantResourceList
    from ._models_py3 import B2CTenantResourcePropertiesBillingConfig
    from ._models_py3 import B2CTenantUpdateRequest
    from ._models_py3 import CheckNameAvailabilityRequestBody
    from ._models_py3 import CreateTenantRequestBody
    from ._models_py3 import CreateTenantRequestBodyProperties
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import NameAvailabilityResponse
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
except (SyntaxError, ImportError):
    from ._models import AsyncOperationStatus  # type: ignore
    from ._models import AsyncOperationStatusError  # type: ignore
    from ._models import B2CResourceSku  # type: ignore
    from ._models import B2CTenantResource  # type: ignore
    from ._models import B2CTenantResourceList  # type: ignore
    from ._models import B2CTenantResourcePropertiesBillingConfig  # type: ignore
    from ._models import B2CTenantUpdateRequest  # type: ignore
    from ._models import CheckNameAvailabilityRequestBody  # type: ignore
    from ._models import CreateTenantRequestBody  # type: ignore
    from ._models import CreateTenantRequestBodyProperties  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import NameAvailabilityResponse  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore

from ._cpim_configuration_client_enums import (
    B2CResourceSkuName,
    BillingType,
    NameAvailabilityReasonType,
    StatusType,
)

__all__ = [
    'AsyncOperationStatus',
    'AsyncOperationStatusError',
    'B2CResourceSku',
    'B2CTenantResource',
    'B2CTenantResourceList',
    'B2CTenantResourcePropertiesBillingConfig',
    'B2CTenantUpdateRequest',
    'CheckNameAvailabilityRequestBody',
    'CreateTenantRequestBody',
    'CreateTenantRequestBodyProperties',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'NameAvailabilityResponse',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'B2CResourceSkuName',
    'BillingType',
    'NameAvailabilityReasonType',
    'StatusType',
]
