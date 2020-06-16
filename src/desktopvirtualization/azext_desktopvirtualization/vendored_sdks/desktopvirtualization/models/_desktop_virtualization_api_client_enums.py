# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ApplicationGroupType(str, Enum):
    """Resource Type of ApplicationGroup.
    """

    remote_app = "RemoteApp"
    desktop = "Desktop"

class ApplicationType(str, Enum):
    """Application type of application.
    """

    remote_app = "RemoteApp"
    desktop = "Desktop"

class CommandLineSetting(str, Enum):
    """Specifies whether this published application can be launched with command line arguments
    provided by the client, command line arguments specified at publish time, or no command line
    arguments at all.
    """

    do_not_allow = "DoNotAllow"
    allow = "Allow"
    require = "Require"

class HostPoolType(str, Enum):
    """HostPool type for desktop.
    """

    personal = "Personal"
    pooled = "Pooled"

class LoadBalancerType(str, Enum):
    """The type of the load balancer.
    """

    breadth_first = "BreadthFirst"
    depth_first = "DepthFirst"
    persistent = "Persistent"

class PersonalDesktopAssignmentType(str, Enum):
    """PersonalDesktopAssignment type for HostPool.
    """

    automatic = "Automatic"
    direct = "Direct"

class RegistrationTokenOperation(str, Enum):
    """The type of resetting the token.
    """

    delete = "Delete"
    none = "None"
    update = "Update"

class SessionState(str, Enum):
    """State of user session.
    """

    unknown = "Unknown"
    active = "Active"
    disconnected = "Disconnected"
    pending = "Pending"
    log_off = "LogOff"
    user_profile_disk_mounted = "UserProfileDiskMounted"

class Status(str, Enum):
    """Status for a SessionHost.
    """

    available = "Available"
    unavailable = "Unavailable"
    shutdown = "Shutdown"
    disconnected = "Disconnected"
    upgrading = "Upgrading"
    upgrade_failed = "UpgradeFailed"

class UpdateState(str, Enum):
    """Update state of a SessionHost.
    """

    initial = "Initial"
    pending = "Pending"
    started = "Started"
    succeeded = "Succeeded"
    failed = "Failed"