# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.keyvault.aio import KeyVaultManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestKeyVaultManagementManagedHsmsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(KeyVaultManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.managed_hsms.begin_create_or_update(
                resource_group_name=resource_group.name,
                name="str",
                parameters={
                    "id": "str",
                    "identity": {
                        "type": "str",
                        "principalId": "str",
                        "tenantId": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "properties": {
                        "createMode": "str",
                        "enablePurgeProtection": True,
                        "enableSoftDelete": True,
                        "hsmUri": "str",
                        "initialAdminObjectIds": ["str"],
                        "networkAcls": {
                            "bypass": "str",
                            "defaultAction": "str",
                            "ipRules": [{"value": "str"}],
                            "virtualNetworkRules": [{"id": "str"}],
                        },
                        "privateEndpointConnections": [
                            {
                                "etag": "str",
                                "id": "str",
                                "privateEndpoint": {"id": "str"},
                                "privateLinkServiceConnectionState": {
                                    "actionsRequired": "str",
                                    "description": "str",
                                    "status": "str",
                                },
                                "provisioningState": "str",
                            }
                        ],
                        "provisioningState": "str",
                        "publicNetworkAccess": "Enabled",
                        "regions": [{"isPrimary": bool, "name": "str", "provisioningState": "str"}],
                        "scheduledPurgeDate": "2020-02-20 00:00:00",
                        "securityDomainProperties": {"activationStatus": "str", "activationStatusMessage": "str"},
                        "softDeleteRetentionInDays": 90,
                        "statusMessage": "str",
                        "tenantId": "str",
                    },
                    "sku": {"family": "B", "name": "str"},
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-11-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_begin_update(self, resource_group):
        response = await (
            await self.client.managed_hsms.begin_update(
                resource_group_name=resource_group.name,
                name="str",
                parameters={
                    "id": "str",
                    "identity": {
                        "type": "str",
                        "principalId": "str",
                        "tenantId": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "properties": {
                        "createMode": "str",
                        "enablePurgeProtection": True,
                        "enableSoftDelete": True,
                        "hsmUri": "str",
                        "initialAdminObjectIds": ["str"],
                        "networkAcls": {
                            "bypass": "str",
                            "defaultAction": "str",
                            "ipRules": [{"value": "str"}],
                            "virtualNetworkRules": [{"id": "str"}],
                        },
                        "privateEndpointConnections": [
                            {
                                "etag": "str",
                                "id": "str",
                                "privateEndpoint": {"id": "str"},
                                "privateLinkServiceConnectionState": {
                                    "actionsRequired": "str",
                                    "description": "str",
                                    "status": "str",
                                },
                                "provisioningState": "str",
                            }
                        ],
                        "provisioningState": "str",
                        "publicNetworkAccess": "Enabled",
                        "regions": [{"isPrimary": bool, "name": "str", "provisioningState": "str"}],
                        "scheduledPurgeDate": "2020-02-20 00:00:00",
                        "securityDomainProperties": {"activationStatus": "str", "activationStatusMessage": "str"},
                        "softDeleteRetentionInDays": 90,
                        "statusMessage": "str",
                        "tenantId": "str",
                    },
                    "sku": {"family": "B", "name": "str"},
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-11-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_begin_delete(self, resource_group):
        response = await (
            await self.client.managed_hsms.begin_delete(
                resource_group_name=resource_group.name,
                name="str",
                api_version="2024-11-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_get(self, resource_group):
        response = await self.client.managed_hsms.get(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-11-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_list_by_resource_group(self, resource_group):
        response = self.client.managed_hsms.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-11-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_list_by_subscription(self, resource_group):
        response = self.client.managed_hsms.list_by_subscription(
            api_version="2024-11-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_list_deleted(self, resource_group):
        response = self.client.managed_hsms.list_deleted(
            api_version="2024-11-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_get_deleted(self, resource_group):
        response = await self.client.managed_hsms.get_deleted(
            name="str",
            location="str",
            api_version="2024-11-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_begin_purge_deleted(self, resource_group):
        response = await (
            await self.client.managed_hsms.begin_purge_deleted(
                name="str",
                location="str",
                api_version="2024-11-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_hsms_check_mhsm_name_availability(self, resource_group):
        response = await self.client.managed_hsms.check_mhsm_name_availability(
            mhsm_name={"name": "str"},
            api_version="2024-11-01",
        )

        # please add some check logic here by yourself
        # ...
