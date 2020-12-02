# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk.checkers import JMESPathCheckGreaterThan
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_device_create
from .example_steps import step_device_list
from .example_steps import step_device_list2
from .example_steps import step_device_update
from .example_steps import step_device_show
from .example_steps import step_device_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_general
@try_manual
def setup_general(test, rg):
    pass


# Env cleanup_general
@try_manual
def cleanup_general(test, rg):
    pass


# Testcase: general
@try_manual
def call_general(test, rg):
    setup_general(test, rg)
    step_device_create(test, rg, checks=[
        test.check("location", "eastus", case_sensitive=False),
        test.check("sku.name", "Edge", case_sensitive=False),
        test.check("sku.tier", "Standard", case_sensitive=False),
        test.check("name", "{myDevice}", case_sensitive=False),
    ])
    step_device_show(test, rg, checks=[
        test.check("location", "eastus", case_sensitive=False),
        test.check("sku.name", "Edge", case_sensitive=False),
        test.check("sku.tier", "Standard", case_sensitive=False),
        test.check("name", "{myDevice}", case_sensitive=False),
    ])
    step_device_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_device_list2(test, rg, checks=[
        JMESPathCheckGreaterThan('length(@)', 0),
    ])
    step_device_update(test, rg, checks=[
        test.check("location", "eastus", case_sensitive=False),
        test.check("sku.name", "Edge", case_sensitive=False),
        test.check("sku.tier", "Standard", case_sensitive=False),
        test.check("name", "{myDevice}", case_sensitive=False),
        test.check("tags.Key1", "value1", case_sensitive=False),
        test.check("tags.Key2", "value2", case_sensitive=False),
    ])
    step_device_show(test, rg, checks=[
        test.check("location", "eastus", case_sensitive=False),
        test.check("sku.name", "Edge", case_sensitive=False),
        test.check("sku.tier", "Standard", case_sensitive=False),
        test.check("name", "{myDevice}", case_sensitive=False),
    ])
    step_device_delete(test, rg, checks=[])
    step_device_list(test, rg, checks=[
        test.check('length(@)', 0),
    ])
    cleanup_general(test, rg)


# Test class for general
@try_manual
class DevicegeneralTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdata_box_edge_GroupForEdgeAutomation'[:7], key='rg',
                           parameter_name='rg')
    def test_device_general(self, rg):

        self.kwargs.update({
            'myDevice': 'testedgedevice',
        })

        call_general(self, rg)
        calc_coverage(__file__)
        raise_if()
