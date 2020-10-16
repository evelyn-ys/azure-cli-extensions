# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import tempfile
import shutil

from azure.cli.testsdk.preparers import AbstractPreparer


class StorageScenarioMixin(object):
    profile = None

    def get_current_profile(self):
        if not self.profile:
            self.profile = self.cmd('cloud show --query profile -otsv').output
        return self.profile

    def get_account_key(self, group, name):
        if self.get_current_profile() == '2017-03-09-profile':
            template = 'storage account keys list -n {} -g {} --query "key1" -otsv'
        else:
            template = 'storage account keys list -n {} -g {} --query "[0].value" -otsv'

        return self.cmd(template.format(name, group)).output

    def get_account_info(self, group, name):
        """Returns the storage account name and key in a tuple"""
        return name, self.get_account_key(group, name)

    def oauth_cmd(self, cmd, *args, **kwargs):
        return self.cmd(cmd + ' --auth-mode login', *args, **kwargs)

    def storage_cmd(self, cmd, account_info, *args):
        cmd = cmd.format(*args)
        cmd = '{} --account-name {} --account-key {}'.format(cmd, *account_info)
        return self.cmd(cmd)

    def storage_cmd_negative(self, cmd, account_info, *args):
        cmd = cmd.format(*args)
        cmd = '{} --account-name {} --account-key {}'.format(cmd, *account_info)
        return self.cmd(cmd, expect_failure=True)

    def create_container(self, account_info, prefix='cont', length=24):
        container_name = self.create_random_name(prefix=prefix, length=length)
        self.storage_cmd('storage container create -n {}', account_info, container_name)
        return container_name

    def create_share(self, account_info, prefix='share', length=24):
        share_name = self.create_random_name(prefix=prefix, length=length)
        self.storage_cmd('storage share create -n {}', account_info, share_name)
        return share_name


class StorageTestFilesPreparer(AbstractPreparer):
    def __init__(self, parameter_name='test_dir'):
        super(StorageTestFilesPreparer, self).__init__(name_prefix='test', name_len=24)
        self.parameter_name = parameter_name

    def create_resource(self, name, **_kwargs):  # pylint: disable=unused-argument
        temp_dir = os.path.join(tempfile.gettempdir(), self.random_name)
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)

        with open(os.path.join(temp_dir, 'readme'), 'w') as f:
            f.write('This directory contains test files generated by Azure CLI storage command '
                    'module tests.')

        for folder_name in ['apple', 'butter', 'butter/charlie', 'duff/edward']:
            for file_index in range(10):
                file_path = os.path.join(temp_dir, folder_name, 'file_%s' % file_index)
                if not os.path.exists(os.path.dirname(file_path)):
                    os.makedirs(os.path.dirname(file_path))

                with open(file_path, 'w') as f:
                    f.write('Azure CLI storage command module test sample file. origin:'
                            ' %s' % file_path)

        setattr(self, '_temp_dir', temp_dir)
        return {self.parameter_name: temp_dir}

    def remove_resource(self, name, **_kwargs):  # pylint: disable=unused-argument
        temp_dir = self.get_temp_dir()
        if temp_dir:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def get_temp_dir(self):
        return getattr(self, '_temp_dir', None)
