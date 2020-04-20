from setuptools import setup, find_packages

setup(
    name='pomanager',
    version='0.1', 
    include_package_data=True,
    install_requires=['Click', 'colorama'],
    entry_points='''
        [console_scripts]
        pomgr=main:main
    ''',
    packages=find_packages(),
)
