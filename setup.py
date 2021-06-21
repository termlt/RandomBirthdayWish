from setuptools import setup, Extension

with open("README.md", "r") as f:
    long_description = f.read()

setup(
  name = 'rbwish',
  packages = ['rbwish'],
  version = '1283',
  license= 'MIT',
  description = "Random Birthday Wish!",
  author = 'termit',
  author_email = 'anoyan2014@yandex.ru',
  download_url = 'https://github.com/termlt/RandomBirthdayWish/archive/refs/tags/23.tar.gz',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/termlt/RandomBirthdayWish',
  keywords = ['happy birthday', 'wish', 'birthday wish', 'birthday'],
  install_requires=[
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Programming Language :: Python :: 3.8',
  ],
)
