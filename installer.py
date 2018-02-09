import pip
import os
import pathlib

cwd = pathlib.Path.cwd()



def file_location(file_name):
    return r'packages\{}'.format(file_name)

## set up all required atom packages
# for n in range(1, 5):
#     os.startfile(file_location('AtomPackage{}.bat'.format(n)))

##add sdopt and safe-elims as environmental variables

Ali_Baharev_packages = ['safe-eliminations', 'sdopt-tearing']
environmental_var = [pathlib.Path(cwd, file_location(path)) for path in
                     Ali_Baharev_packages]



environmental_var = ';'.join(map(str, environmental_var))

print(environmental_var)

cmd_file = file_location('environmental_var.bat')
cmd_command = open(cmd_file, 'w')
cmd_command.write('setx PYTHONPATH {}'.format(environmental_var))
cmd_command.close()
print(environmental_var)
#os.startfile(cmd_file)

# ## pip install all dependancies from tar and whl
# pip.main(['uninstall', 'networkx'])
# packages = ['astunparse-1.4.0.tar.gz',
#             'simpleeval-0.9.1.tar.gz',
#             'tqdm-4.10.0-py2.py3-none-any.whl',
#             'anyjson-0.3.3.tar.gz',
#             'amqp-1.4.9.tar.gz',
#             'kombu-3.0.37.tar.gz',
#             'billiard-3.3.0.23.tar.gz',
#             'pytz-2017.2-py2.py3-none-any.whl',
#             'celery-3.1.25.tar.gz',
#             'tornado-4.2.tar.gz',
#             'Babel-1.0.tar.gz',
#             'flower-0.9.2.tar.gz',
#             'casadi-3.2.2-cp36-none-win_amd64.whl',
#             'namedlist-1.7.tar.gz',
#             'networkx-1.11.tar.gz']
#
# for p in packages:
#
#     pip.main(['install', file_location(p)])
# #    os.remove(file_location(p))
#






