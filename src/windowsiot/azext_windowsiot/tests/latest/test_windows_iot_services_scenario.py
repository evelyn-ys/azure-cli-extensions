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
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import JMESPathCheck, JMESPathCheckGreaterThan
from .example_steps import step_create
from .example_steps import step_list
from .example_steps import step_list2
from .example_steps import step_show
from .example_steps import step_update
from .example_steps import step_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg, rg_2, rg_3, rg_4):
    test.kwargs.update({
        'wiot': 'testwindowiot',
        'domain': 'microsoft.onmicrosoft.com'
    })
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg, rg_2, rg_3, rg_4):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg, rg_2, rg_3, rg_4):
    setup_scenario(test, rg, rg_2, rg_3, rg_4)
    step_create(test, rg, rg_2, rg_3, rg_4, checks=[
        JMESPathCheck('name', test.kwargs['wiot']),
        JMESPathCheck('adminDomainName', test.kwargs['domain']),
        JMESPathCheck('billingDomainName', test.kwargs['domain']),
        JMESPathCheck('notes', 'notes'),
        JMESPathCheck('quantity', 100)
    ])
    step_list(test, rg, rg_2, rg_3, rg_4, checks=[
        JMESPathCheckGreaterThan('length(@)', 0)
    ])
    step_list2(test, rg, rg_2, rg_3, rg_4, checks=[
        JMESPathCheck('length(@)', 1)
    ])
    step_show(test, rg, rg_2, rg_3, rg_4, checks=[
        JMESPathCheck('name', test.kwargs['wiot']),
        JMESPathCheck('adminDomainName', test.kwargs['domain']),
        JMESPathCheck('billingDomainName', test.kwargs['domain']),
        JMESPathCheck('notes', 'notes'),
        JMESPathCheck('quantity', 100)
    ])
    step_update(test, rg, rg_2, rg_3, rg_4, checks=[
        JMESPathCheck('name', test.kwargs['wiot']),
        JMESPathCheck('adminDomainName', test.kwargs['domain']),
        JMESPathCheck('billingDomainName', test.kwargs['domain']),
        JMESPathCheck('notes', 'new notes'),
        JMESPathCheck('quantity', 300)
    ])
    step_delete(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_list2(test, rg, rg_2, rg_3, rg_4, checks=[
        JMESPathCheck('length(@)', 0)
    ])
    cleanup_scenario(test, rg, rg_2, rg_3, rg_4)


# Test class for Scenario
@try_manual
class Windows_iot_servicesScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(Windows_iot_servicesScenarioTest, self).__init__(*args, **kwargs)

    @ResourceGroupPreparer(name_prefix='clitestwindows_iot_services_res6117'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestwindows_iot_services_res9407'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestwindows_iot_services_res9101'[:7], key='rg_3', parameter_name='rg_3')
    @ResourceGroupPreparer(name_prefix='clitestwindows_iot_services_res4228'[:7], key='rg_4', parameter_name='rg_4')
    def test_windows_iot_services_Scenario(self, rg, rg_2, rg_3, rg_4):
        call_scenario(self, rg, rg_2, rg_3, rg_4)
        calc_coverage(__file__)
        raise_if()
