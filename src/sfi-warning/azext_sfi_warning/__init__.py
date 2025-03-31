# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from knack.events import EVENT_INVOKER_POST_PARSE_ARGS
from .hooks import sfi_warning_handler


class SFIWarningCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        super(SFIWarningCommandsLoader, self).__init__(cli_ctx=cli_ctx)
        self.cli_ctx.register_event(EVENT_INVOKER_POST_PARSE_ARGS, sfi_warning_handler)

    def load_command_table(self, _):
        return self.command_table

    def load_arguments(self, _):
        pass


COMMAND_LOADER_CLS = SFIWarningCommandsLoader
