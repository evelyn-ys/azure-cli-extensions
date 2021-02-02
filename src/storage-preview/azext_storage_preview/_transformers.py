# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import base64
from dateutil import parser
from knack.log import get_logger
from knack.util import to_camel_case, todict

storage_account_key_options = {'primary': 'key1', 'secondary': 'key2'}
logger = get_logger(__name__)


def transform_acl_list_output(result):
    """ Transform to convert SDK output into a form that is more readily
    usable by the CLI and tools such as jpterm. """
    from collections import OrderedDict
    new_result = []
    for key in sorted(result.keys()):
        new_entry = OrderedDict()
        new_entry['Name'] = key
        new_entry['Start'] = result[key]['start']
        new_entry['Expiry'] = result[key]['expiry']
        new_entry['Permissions'] = result[key]['permission']
        new_result.append(new_entry)
    return new_result


def transform_container_permission_output(result):
    return {'publicAccess': result.public_access or 'off'}


def transform_cors_list_output(result):
    from collections import OrderedDict
    new_result = []
    for service in sorted(result.keys()):
        for i, rule in enumerate(result[service]):
            new_entry = OrderedDict()
            new_entry['Service'] = service
            new_entry['Rule'] = i + 1

            new_entry['AllowedMethods'] = ', '.join((x for x in rule.allowed_methods))
            new_entry['AllowedOrigins'] = ', '.join((x for x in rule.allowed_origins))
            new_entry['ExposedHeaders'] = ', '.join((x for x in rule.exposed_headers))
            new_entry['AllowedHeaders'] = ', '.join((x for x in rule.allowed_headers))
            new_entry['MaxAgeInSeconds'] = rule.max_age_in_seconds
            new_result.append(new_entry)
    return new_result


def transform_entity_query_output(result):
    from collections import OrderedDict
    new_results = []
    ignored_keys = ['etag', 'Timestamp', 'RowKey', 'PartitionKey']
    for row in result['items']:
        new_entry = OrderedDict()
        new_entry['PartitionKey'] = row['PartitionKey']
        new_entry['RowKey'] = row['RowKey']
        other_keys = sorted([x for x in row.keys() if x not in ignored_keys])
        for key in other_keys:
            new_entry[key] = row[key]
        new_results.append(new_entry)
    return new_results


def transform_entities_result(result):
    for entity in result.items:
        transform_entity_result(entity)
    return result


def transform_entity_result(entity):
    for key in entity.keys():
        entity_property = entity[key]
        if hasattr(entity_property, 'value') and isinstance(entity_property.value, bytes):
            entity_property.value = base64.b64encode(entity_property.value).decode()
    return entity


def transform_logging_list_output(result):
    from collections import OrderedDict
    new_result = []
    for key in sorted(result.keys()):
        new_entry = OrderedDict()
        new_entry['Service'] = key
        new_entry['Read'] = str(result[key]['read'])
        new_entry['Write'] = str(result[key]['write'])
        new_entry['Delete'] = str(result[key]['delete'])
        new_entry['RetentionPolicy'] = str(result[key]['retentionPolicy']['days'])
        new_result.append(new_entry)
    return new_result


def transform_metrics_list_output(result):
    from collections import OrderedDict
    new_result = []
    for service in sorted(result.keys()):
        service_name = service
        for interval in sorted(result[service].keys()):
            item = result[service][interval]
            new_entry = OrderedDict()
            new_entry['Service'] = service_name
            service_name = ''
            new_entry['Interval'] = str(interval)
            new_entry['Enabled'] = str(item['enabled'])
            new_entry['IncludeApis'] = str(item['includeApis'])
            new_entry['RetentionPolicy'] = str(item['retentionPolicy']['days'])
            new_result.append(new_entry)
    return new_result


def create_boolean_result_output_transformer(property_name):
    def _transformer(result):
        return {property_name: result}

    return _transformer


def transform_storage_list_output(result):
    if getattr(result, 'next_marker', None):
        logger.warning('Next Marker:')
        logger.warning(result.next_marker)
    return list(result)


# pylint: disable=unused-argument
def transform_file_upload(result):
    return None


def transform_queue_stats_output(result):
    if isinstance(result, dict):
        new_result = {}
        from azure.cli.core.commands.arm import make_camel_case
        for key in result.keys():
            new_key = make_camel_case(key)
            new_result[new_key] = transform_queue_stats_output(result[key])
        return new_result
    return result


def transform_message_list_output(result):
    for i, item in enumerate(result):
        result[i] = transform_message_output(item)
    return list(result)


def transform_message_output(result):
    result = todict(result)
    new_result = {'expirationTime': result.pop('expires_on', None),
                  'insertionTime': result.pop('inserted_on', None),
                  'timeNextVisible': result.pop('next_visible_on', None)}
    from azure.cli.core.commands.arm import make_camel_case
    for key in sorted(result.keys()):
        new_result[make_camel_case(key)] = result[key]
    return new_result


def transform_queue_policy_json_output(result):
    new_result = {}
    for policy in sorted(result.keys()):
        new_result[policy] = transform_queue_policy_output(result[policy])
    return new_result


def transform_queue_policy_output(result):
    result = todict(result)
    if result['start']:
        result['start'] = parser.parse(result['start'])
    if result['expiry']:
        result['expiry'] = parser.parse(result['expiry'])
    return result
