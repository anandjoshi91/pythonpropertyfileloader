from p import Property
from pathlib import Path
import os
import sys

__use_env = True

for arg in sys.argv[1:]:
    if arg == "env":
        __use_env=True
    elif arg == "noenv":
        __use_env=False

prop = Property(use_env=__use_env)
testfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'my_file.properties')
dic_prop = prop.load_property_files(testfile)

print(dic_prop)

if mis := prop.get_missing_values() :
    print("The following unknown keys where detected while resolving substitutions:")
    for k in mis.keys() :
        print(k)
