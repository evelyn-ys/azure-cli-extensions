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
from .example_steps import step_list_sku
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_list_sku(test, rg, checks=[JMESPathCheckGreaterThan('length(@)', 0)])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class GeneralScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdata_box_edge_GroupForEdgeAutomation'[:7], key='rg',
                           parameter_name='rg')
    def test_general_Scenario(self, rg):

        self.kwargs.update({
            'myDevice': 'testedgedevice',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
