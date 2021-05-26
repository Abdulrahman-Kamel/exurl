from distutils.core import setup
setup(
  name = 'exurl',
  packages = ['exurl'],
  version = '1.0',
  license='MIT',
  description = 'Division url to many urls approval on parameters - to make fuzzing or testing parameters one by one',
  author = 'Abdulrahman Kamel',
  author_email = 'vulnabdo@gmail.com',
  url = 'https://github.com/Abdulrahman-Kamel/exurl',
  #download_url = 'https://github.com/Abdulrahman-Kamel/exurl/archive/pypi-0_1_3.tar.gz',
  #keywords = ['split', 'easy', 'scraper', 'website', 'download', 'links', 'images', 'videos'],
  install_requires=['urllib3>=1.25.9']
)