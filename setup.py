from setuptools import find_packages
from setuptools import setup


setup(
    name='santa.content',
    version='0.1',
    description="",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='ABITA',
    author_email='taito.horiuchi@abita.fi',
    url='http://santa.abita.fi/',
    license='Non-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['santa'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'hexagonit.testing',
        'plone.app.dexterity',
        'plone.app.referenceablebehavior',
        'plone.namedfile [blobs]',
        'setuptools',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
