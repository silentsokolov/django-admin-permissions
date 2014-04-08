#!/usr/bin/env python
import sys
from os import path
from django.conf import settings

if not settings.configured:
    module_root = path.dirname(path.realpath(__file__))

    settings.configure(
        DEBUG=False,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },

        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.admin',
            'django.contrib.sessions',
            'admin_permissions',
        ),
        TEST_RUNNER='django.test.simple.DjangoTestSuiteRunner',
    )


def main():
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)

    test_runner = TestRunner()

    failures = test_runner.run_tests(('admin_permissions',))
    sys.exit(failures)


if __name__ == '__main__':
    main()