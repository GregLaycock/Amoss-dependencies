import glob

pyfiles = glob.glob('*.py')

modulenames = [f.split('.')[0] for f in pyfiles]

# print(modulenames)

for f in pyfiles:
    contents = open(f).read()
    for m in modulenames:
        v1 = "import " + m
        v2 = "from " + m
        if v1 or v2 in contents:
            contents = contents.replace(v1, "import ."+m)
            contents = contents.replace(v2, "from ."+m)
    with open('new_'+f, 'w') as outf:
        outf.write(contents)

