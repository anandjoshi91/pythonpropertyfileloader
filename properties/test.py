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
    print("The following unknown keys where detected while finding substitutions:")
    for k in mis.keys() :
        print(k)

# Output

# {'foo': 'I am awesome', 'bar': 'fudge-bar', 'chocolate': 'fudge',
#  'long': 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here',
#  'url': 'example.com/api?auth_token=xyz'}
