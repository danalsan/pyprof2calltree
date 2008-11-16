from setuptools import setup, find_packages
import sys, os

version = '1.0'
classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: X11 Applications :: KDE
License :: OSI Approved :: BSD License
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Desktop Environment :: K Desktop Environment (KDE)
Topic :: Software Development
Topic :: Software Development :: Profilers
Topic :: Software Development :: Quality Assurance
Topic :: System :: System Shells
Topic :: Utilities
"""

setup(
    name='pyprof2calltree',
    version=version,
    description="Help visualize profiling data from cProfile with kcachegrind",
    long_description=file('README.txt').read(),
    keywords='profiler visualization programming tool kde kcachegrind',
    classifiers=[c for c in classifiers.split("\n") if c and c.strip()],
    author='Olivier Grisel',
    author_email='olivier.grisel@ensta.org',
    url='http://www.bitbucket.org/ogrisel/pyprof2calltree/src/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    entry_points = {
        'setuptools.installation': [
            'eggsecutable = pyprof2calltree:main',
        ],
        'console_scripts': [
            'pyprof2calltree = pyprof2calltree:main',
        ],
    }
)