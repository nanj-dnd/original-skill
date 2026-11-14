import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from bench import persona
name, qfile, afile = sys.argv[1:4]
open(afile, 'w').write(persona(name, open(qfile).read()))
print(open(afile).read())
