from setuptools import setup, find_packages
from simple_sso import __version__ as version


setup(
    name="ccisdg-django-sso",
    version=version,
    description="Simple SSO for Django modified for ACE project",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='django sso',
    author='Jonas Obrist',
    author_email='jonas.obrist@divio.ch',
    url='http://github.com/aldryn/django-simple-sso',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'itsdangerous',
        'Django>=1.11,<2.1',
        'webservices[django]',
    ],
    include_package_data=True,
    zip_safe=False,
)
