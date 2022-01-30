from setuptools import setup, find_packages

setup(
    name='gamestat-back',
    version='1.0',
    install_requires=['Django>=3.0,<4.0',
                      'django-debug-toolbar',
                      'psycopg2-binary',
                      'pillow'],
    packages=find_packages()
)
