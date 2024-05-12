from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='pycinwa',
    version='0.1.0',
    packages=find_packages(exclude="tests"),
    url='https://github.com/galj03/pycinwa',
    license='MIT License',
    author='galj',
    author_email='galjozsi45@gmail.com',
    description='TODO: write description',
    long_description=long_description,
    install_requires=['requests', 'Flask', 'Flask-Session', 'icalendar', 'mock']
)
