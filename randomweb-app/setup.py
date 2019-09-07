from setuptools import setup, find_packages

setup(
    name='randomweb-app',
    version='1.0',
    description='Random Webapp',
    author='Fishy Baker',
    author_email='fishybaker@hotmail.com',
    packages=find_packages(),
    install_requires = [
        'Flask >= 1.1.1',
        'Flask-Bootstrap >= 3.3.7.1',
        'Flask-WTF >= 0.14.2',
        'jsonschema >= 3.0.1',
        'bettermath-lib >= 1.0'
    ],
    include_package_data=True,
    package_data={'randomweb_app': ['templates/*', 'static/*']}
)
