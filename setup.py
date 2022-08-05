from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='lordchk',
  version='0.0.1',
  description='A very basic Checker Module',
  long_description=open('README.txt').read() + '\n\n',
  url='',  
  author='yusiqo',
  author_email='yusiqo10@gmail.com,
  license='MIT', 
  classifiers=classifiers,
  keywords='lordchk', 
  packages=find_packages(),
  install_requires=['requests'] 
)
