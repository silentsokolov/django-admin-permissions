[![Build Status](https://drone.io/github.com/SilentSokolov/django-admin-permissions/status.png)](https://drone.io/github.com/SilentSokolov/django-admin-permissions/latest)

django-admin-permissions
===============

Very simple extension that adds a permissions check on the field in admin


Installation
===============

### Requires

    django >= 1.4


Install with ``pip``:

Run ``pip install git+https://github.com/SilentSokolov/django-admin-permissions.git``

Open ``settings.py`` and add ``admin_permissions`` to your ``INSTALLED_APPS``:

    INSTALLED_APPS = (
        ...
        'admin_permissions',
        ...
    )


Example usage
===============

Use class ``ModelAdminPermission`` and set permissions using ``fields_permissions``:

    class ArticleAdmin(ModelAdminPermission):
        fieldsets = [
            ('General', {
                'fields': ['title', 'slug', 'text'],
            }),
            ('SEO', {
                'fields': ['seo_title', 'seo_description'],
            }),
        ]

        fields_permissions = {
            # 'permission': ('field',)
            'articles.can_change_admin_seo_fields': ('seo_title', 'seo_description'),
        }


### Options

If you want the user to see the field, but could not edit them, set ``fields_permissions_read_only`` is ``True``, default ``False``.