# -*- coding: utf-8 -*-

from copy import deepcopy


class FieldPermissionMixin(object):
    """Adds simple functionality to check the permissions for the fields"""

    fields_permissions = {}  # type: ignore
    fields_permissions_read_only = False

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(FieldPermissionMixin, self).get_fieldsets(request, obj)

        if not self.fields_permissions_read_only:
            # if formset was received by link we should make copy before removing fields
            if getattr(self, "fieldsets", None) is fieldsets:
                fieldsets = deepcopy(fieldsets)
            for permission, fields in self.fields_permissions.items():
                if not request.user.has_perm(permission):
                    if isinstance(fields, (str, list)):
                        fields = (fields,)
                    fieldsets = self.remove_fields(fieldsets, *fields)

        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        fieldsets = super(FieldPermissionMixin, self).get_readonly_fields(request, obj)

        if self.fields_permissions_read_only:
            for permission, fields in self.fields_permissions.items():
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
            fs[1]["fields"] = [field for field in fs[1]["fields"] if field not in remove_fields]
            if not fs[1]["fields"]:
                fieldsets.pop(count)
        return fieldsets
