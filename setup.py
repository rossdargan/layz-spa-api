from distutils.core import setup

def readme():
    with open('README.rst') as desc:
        return desc.read()

setup(
  name = 'layz_spa',
  packages = ['layz_spa'], 
  version = '0.4',
  license='MIT',
  description = 'An API to control wifi based lay-z spas', 
  long_description=readme(),
  long_description_content_type='text/markdown',
  author = 'Ross Dargan',
  author_email = 'layzspa@the-dargans.co.uk', 
  url = 'https://github.com/rossdargan/', 
  download_url = 'https://github.com/rossdargan/layz-spa-api/archive/0.4.tar.gz',  
  keywords = ['Lazy Spa', 'Layz Spa', 'Lay-z spa'],   
  install_requires=[
          'aiohttp'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',     
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)