from setuptools import setup, find_packages
setup(
    name='Rest-RouterOS',
    version='0.1.0',
    packages=find_packages(include=['RestRouterOS', 'RestRouterOS.*']),
    description='A python module for RouterOS REST API',
    author='Silvertoken',
    author_email='https://github.com/silvertoken',
    url='https://github.com/silvertoken/rest-routeros',
    install_requires=[
        'httpx'
    ],
    keywords=[
        'mikrotik',
        'routeros'
    ]
)