import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='django-simple-open-graph',
    version='0.3',
    license='ISC',
    description='Django package for simplicity embed open graph (og:) '
                'layout in templates for different objects',
    long_description=read('README.rst') + read('CHANGES.rst'),
    url='https://github.com/saippuakauppias/django-simple-open-graph',
    author='Denis Veselov',
    author_email='progr.mail@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
