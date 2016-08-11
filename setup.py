import os
from setuptools import setup

#with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='open-edx-api-extension-cms',
    version='0.1',
    packages=['open_edx_api_extension_cms'],
    include_package_data=True,
    description='API extension for Open edX CMS',
    #long_description=README,
    #url='https://github.com/raccoongang/open_edx_api_extension',
    author='Maxim Petrov',
    author_email='maxim.petrov@kspt.icc.spbstu.ru',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
