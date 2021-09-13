
from setuptools import setup, find_packages

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(name='tapclient',
    version='0.0.2',
    description='Proofpoint TAP API client library',
    long_description=readme,
    log_description_content_type='text/markdown',
    author='Mike Olden',
    author_email='michael.olden@oldendigital.com',
    url = 'https://github.com/drizzo-tech/tapclient',
    project_urls={
        'Bug Tracker': 'https://github.com/drizzo-tech/tapclientissues'
    },
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    ],
    license='Apache 2.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[
        'peppercorn'
    ],
    keywords='Proofpoint, TAP'
)