.. image:: https://travis-ci.org/silentsokolov/django-admin-permissions.svg?branch=master
   :target: https://travis-ci.org/silentsokolov/django-admin-permissions

.. image:: https://codecov.io/gh/silentsokolov/django-admin-permissions/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/silentsokolov/django-admin-permissions


django-admin-permissions
========================

Very simple extension that adds a permissions check on the field in admin


Requirements
------------

* Python 2.7+ or Python 3.3+
* Django 1.8+


Installation
------------

Use your favorite Python package manager to install the app from PyPI, e.g.

Example:

``pip install django-admin-permissions``

Add ``admin_permissions`` to ``INSTALLED_APPS``:

Example:

.. code:: python

    INSTALLED_APPS = (
        ...
        'admin_permissions',
        ...
    )


Example usage
-------------

Use class ``ModelAdminPermission`` and set permissions using ``fields_permissions``:

.. code:: python

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


Options
~~~~~~~

If you want the user to see the field, but could not edit them, set ``fields_permissions_read_only`` is ``True``, default ``False``.
