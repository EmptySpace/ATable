from setuptools import find_packages, setup

import versioneer

_deps_ = ['astropy',
          'fitsio',
          'pandas',
          'versioneer']

setup(name='aTable',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Another table interface',
      packages=['atable'],
      install_requires=_deps_,
      zip_safe=False,
      include_package_data=True)
