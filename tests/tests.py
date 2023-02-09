# -*- coding: utf-8 -*-

import unittest
from unittest.mock import MagicMock

from admin_permissions.admin import FieldPermissionMixin


class AdminPermissionTest(unittest.TestCase):
    def setUp(self):
        self.fields_permissions_read_only = False
        self.fieldsets = [
            (
                "General",
                {
                    "fields": ["title", "slug", "preview_content", "content", "public"],
                },
            ),
            (
                "SEO",
                {
                    "fields": ["seo_title", "seo_description"],
                },
            ),
        ]

    def test_remove_fields(self):
        fieldsets = FieldPermissionMixin.remove_fields(self.fieldsets, "title")
        self.assertListEqual(
            ["slug", "preview_content", "content", "public"], fieldsets[0][1]["fields"]
        )

    def test_remove_fields_and_empty_fieldsets(self):
        fieldsets = FieldPermissionMixin.remove_fields(
            self.fieldsets, "seo_title", "seo_description"
        )
        self.assertListEqual(
            [("General", {"fields": ["title", "slug", "preview_content", "content", "public"]})],
            fieldsets,
        )

    def test_unchanging_base_fieldset(self):
        class BaseAdmin(object):
            fieldsets = None

            def get_fieldsets(self, _request, _obj):
                return self.fieldsets

        class AdminTest(FieldPermissionMixin, BaseAdmin):
            fieldsets = self.fieldsets
            fields_permissions = {
                "articles.can_change_admin_base_fields": (
                    "title",
                    "slug",
                    "preview_content",
                    "content",
                    "public",
                ),
                "articles.can_change_admin_seo_fields": ("seo_title", "seo_description"),
            }

        request = MagicMock(user=MagicMock(has_perm=MagicMock(return_value=False)))
        admin_instance = AdminTest()
        fieldsets = admin_instance.get_fieldsets(request, None)
        self.assertListEqual([], fieldsets)
        self.assertEqual(len(admin_instance.fieldsets), 2)
        self.assertListEqual(
            ["title", "slug", "preview_content", "content", "public"],
            admin_instance.fieldsets[0][1]["fields"],
        )
        self.assertListEqual(
            ["seo_title", "seo_description"], admin_instance.fieldsets[1][1]["fields"]
        )
