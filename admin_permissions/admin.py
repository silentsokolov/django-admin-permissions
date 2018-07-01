# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin


class ModelAdminPermission(admin.ModelAdmin):
    """Adds simple functionality to check the permissions for the fields"""
    fields_permissions = {}
    fields_permissions_read_only = False

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(ModelAdminPermission, self).get_fieldsets(request, obj)

        if not self.fields_permissions_read_only:
            for permission, fields in self.fields_permissions.iteritems():
                if not request.user.has_perm(permission):
                    if isinstance(fields, (str, list)):
                        fields = (fields,)
                    fieldsets = self.remove_fields(fieldsets, *fields)

        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        fieldsets = super(ModelAdminPermission, self).get_readonly_fields(request, obj)

        if self.fields_permissions_read_only:
            for permission, fields in self.fields_permissions.iteritems():
                if not request.user.has_perm(permission):
                    if isinstance(fields, (str, list)):
                        fields = (fields,)
                    fieldsets += fields

        return fieldsets

    @staticmethod
    def remove_fields(fieldsets, *remove_fields):
        """
        Removes all the anterior field,
        if there is no fieldsets available fields, it is also removed,
        Returns the modified fieldsets
        """
        for count, fs in enumerate(fieldsets):
            fs[1]['fields'] = [field for field in fs[1]['fields'] if field not in remove_fields]
            if not fs[1]['fields']:
                fieldsets.pop(count)
        return fieldsets
