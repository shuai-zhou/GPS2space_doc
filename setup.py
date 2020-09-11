from setuptools import setup

setup(
	  name='gps2space',
	  packages=['gps2space'],
      version='0.1.1',
      license='MIT',
      description='A Python library for building spatial data and calculating buffer- and Convex hull-based activity space from raw GPS data',
      author='GPS2space',
      author_email='sxz217@psu.edu',
      url='https://gps2space.readthedocs.io/en/latest/',
      keywords = ['GPS', 'activity space', 'buffer', 'convex hull'],
      install_requires=[
                        'pandas',
                        'geopandas',
                        'numpy',
                        'scipy',
                        'shapely'],
	  classifiers=[
	  	           'Development Status :: 4 - Beta',
	  	           'Programming Language :: Python :: 3',
	               'License :: OSI Approved :: MIT License',
				   'Operating System :: OS Independent'],
      )
