# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IdentitySource(Model):
    """vCenter Single Sign On Identity Source.

    :param name: The name of the identity source
    :type name: str
    :param alias: The domain's NetBIOS name
    :type alias: str
    :param domain: The domain's dns name
    :type domain: str
    :param base_user_dn: The base distinguished name for users
    :type base_user_dn: str
    :param base_group_dn: The base distinguished name for groups
    :type base_group_dn: str
    :param primary_server: Primary server URL
    :type primary_server: str
    :param secondary_server: Secondary server URL
    :type secondary_server: str
    :param ssl: Protect LDAP communication using SSL certificate (LDAPS).
     Possible values include: 'Enabled', 'Disabled'
    :type ssl: str or ~vendored_sdks.models.SslEnum
    :param username: The ID of an Active Directory user with a minimum of
     read-only access to Base DN for users and group
    :type username: str
    :param password: The password of the Active Directory user with a minimum
     of read-only access to Base DN for users and groups.
    :type password: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'base_user_dn': {'key': 'baseUserDN', 'type': 'str'},
        'base_group_dn': {'key': 'baseGroupDN', 'type': 'str'},
        'primary_server': {'key': 'primaryServer', 'type': 'str'},
        'secondary_server': {'key': 'secondaryServer', 'type': 'str'},
        'ssl': {'key': 'ssl', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, alias: str=None, domain: str=None, base_user_dn: str=None, base_group_dn: str=None, primary_server: str=None, secondary_server: str=None, ssl=None, username: str=None, password: str=None, **kwargs) -> None:
        super(IdentitySource, self).__init__(**kwargs)
        self.name = name
        self.alias = alias
        self.domain = domain
        self.base_user_dn = base_user_dn
        self.base_group_dn = base_group_dn
        self.primary_server = primary_server
        self.secondary_server = secondary_server
        self.ssl = ssl
        self.username = username
        self.password = password
