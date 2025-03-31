# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

logger = get_logger(__name__)


def sfi_warning_handler(_, **kwargs):
    """
    An event handler for SFI warning when EVENT_INVOKER_POST_PARSE_ARGS event is invoked.
    """
    command = kwargs.get('command')
    args = kwargs.get('args')
    logger.warning(f'SFI Warning for command {command}, args {args}')
