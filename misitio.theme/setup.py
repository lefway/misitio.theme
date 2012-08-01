from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='misitio.theme',
      version=version,
      description="descripcion corta del paquete tema",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='luis eduardo florez bautista',
      author_email='lflorez@vtv.gob.ve',
      url='git@github.com:lefway/misitio.theme.git',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['misitio'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
