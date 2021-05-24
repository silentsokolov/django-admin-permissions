# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django

__author__ = 'Dmitriy Sokolov'
__version__ = '0.2.2'


if django.VERSION < (3, 2):
    default_app_config = 'admin_permissions.apps.AdminPermissionsConfig'


VERSION = __version__
