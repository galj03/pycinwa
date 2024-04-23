from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='pycinwa',
    version='',
    packages=find_packages(exclude="tests"),
    url='',
    license='MIT License',
    author='galj',
    author_email='galjozsi45@gmail.com',
    description='TODO: write description',
    long_description=long_description,
    install_requires=['requests', 'Flask']
)
