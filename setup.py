from distutils.core import setup

setup(
    name='django-admin-permissions',
    version='0.2.1',
    url='https://github.com/silentsokolov/django-admin-permissions',
    license='MIT',
    author='Dmitriy Sokolov',
    author_email='silentsokolov@gmail.com',
    description='Very simple extension that adds a permissions check on the field in admin',
    packages=['admin_permissions'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django>=1.4',
    ],
    tests_require=['Django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)