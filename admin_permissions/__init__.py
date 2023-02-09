# -*- coding: utf-8 -*-

import django

__author__ = "Dmitriy Sokolov"
__version__ = "1.1.0"


if django.VERSION < (3, 2):
    default_app_config = "admin_permissions.apps.AdminPermissionsConfig"


VERSION = __version__
