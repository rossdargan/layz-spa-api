from distutils.core import setup
setup(
  name = 'lazy_spa',
  packages = ['lazy_spa'], 
  version = '0.2',
  license='MIT',
  description = 'An API to control wifi based lay-z spas', 
  author = 'Ross Dargan',
  author_email = 'lazyspa@the-dargans.co.uk', 
  url = 'https://github.com/rossdargan/', 
  download_url = 'https://github.com/rossdargan/lazy-spa-api/archive/0.2.tar.gz',  
  keywords = ['Lazy Spa', 'Lay-z spa'],   
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