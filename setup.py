from setuptools import setup

setup(
  name = 'pgdumper',
  description = 'Simple PostgreSQL dumper',
  author = 'Roman Dolgushin',
  author_email = 'rd@roman-dolgushin.ru',
  url = 'https://github.com/rdolgushin/pgdumper',
  license = 'MIT',
  version = '0.1',
  packages = ['pgdumper'],
  install_requires = ['mydumper'],
  entry_points = {
    'console_scripts': ['pgdumper = pgdumper.pgdumper:main']
  },
  classifiers = [
    'Topic :: Utilities',
    'Topic :: Database',
    'Topic :: System :: Systems Administration',
    'Environment :: Console',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX'
  ],
)
