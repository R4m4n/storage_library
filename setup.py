from setuptools import find_packages, setup
setup(
    name='storage_lib',
    packages=find_packages(include=['StorageLib']),
    version='0.1.0',
    description='Storage library containing CRUD operations.',
    author='Raman',
    license='MIT',
    install_requires=['dicttoxml', 'xmltodict', 'boto3'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)