from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-contacto',
    version=version,
    description="Formulario de contacto // Contact form",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='fperez e imruiz',
    author_email='datosabiertos@malaga.eu',
    url='datosabiertos.malaga.eu',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.contacto'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        contacto=ckanext.contacto.plugin:ContactClass
    ''',
)
