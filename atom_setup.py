import pip
import os
import pathlib

cwd = pathlib.Path.cwd()

def file_location(file_name):
    return r'packages\{}'.format(file_name)


for n in range(1, 5):
    os.startfile(file_location('AtomPackage{}.bat'.format(n)))