from setuptools import setup
import pathlib
import os
cwd = pathlib.Path.cwd()
wd = cwd # pathlib.Path(cwd,'packages')

names = (os.listdir(wd))
print(names)
print(wd)
setup(
    name='ordering',
    version='1.0',
 #   package_dir = wd,
    packages= ['safe_eliminations','sdopt_tearing'], #names,
    url='',
    license='',
    author='Baharev',
    author_email='',
    description= 'package containing all python modules from Baharevs sdoptearing and safe elims packages'
)


