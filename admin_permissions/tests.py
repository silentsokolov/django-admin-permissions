# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from admin_permissions.admin import ModelAdminPermission


class AdminPermissionTest(unittest.TestCase):
    def setUp(self):
        self.fieldsets = [
            ('General', {
                'fields': ['title', 'slug', 'preview_content', 'content', 'public'],
            }),
            ('SEO', {
                'fields': ['seo_title', 'seo_description'],
            }),
        ]

    def test_remove_fields(self):
        fieldsets = ModelAdminPermission.remove_fields(self.fieldsets, 'title')
        self.assertListEqual(['slug', 'preview_content', 'content', 'public'], fieldsets[0][1]['fields'])

    def test_remove_fields_and_empty_fieldsets(self):
        fieldsets = ModelAdminPermission.remove_fields(self.fieldsets, 'seo_title', 'seo_description')
        self.assertListEqual([('General', {'fields': ['title', 'slug', 'preview_content', 'content', 'public']})], fieldsets)
