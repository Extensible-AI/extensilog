from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='extensilog',
    version='0.0.1',
    packages=find_packages(include=['extensilog', 'extensilog.*']),
    install_requires=required,
    long_description=long_description,
    license='Apache License 2.0',
    author='Parth Sareen, Omkaar Kamath',
    author_email='parth@extensible.dev, omkaar@extensible.dev',
    description='A logger for tracking your agent workflow',
    url='https://github.com/Extensible-AI/extensilog/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)