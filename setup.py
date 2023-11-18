# setup.py
from setuptools import setup, find_packages

setup(
    name='netspresso',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'paramiko',
        'python-decouple',
        'click',
        'rich',
        'pytest'
    ],
    entry_points='''
        [console_scripts]
        netspresso=netspresso.cli:main
    ''',
)
