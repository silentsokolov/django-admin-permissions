from distutils.core import setup

setup(
    name='django-admin-permissions',
    version='0.1',
    url='https://github.com/SilentSokolov/django-admin-permissions',
    license='MIT',
    author='Dmitriy Sokolov',
    author_email='silentsokolov@gmail.com',
    description='Very simple extension that adds a permissions check on the field in admin',
    packages=['admin_permissions'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django>=1.5',
    ],
)