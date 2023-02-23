# pythonpropertyfileloader
### A python module to load property files.
 Actually it is like the PropertyPlaceholderConfigurer in spring which lets you use ${variable-reference} to refer to already defined property ).

 Placeholders are also resolved using env variables, like the spring property loader does, if the class is instantiated with the `use_env` argument (defaults to false for backward compatibility)

Install
----------

```pip install property```



Example
---------

## my_file.properties
```
foo = I am awesome
bar = ${chocolate}-bar
chocolate = fudge
long = a very long property that is described in the property file which takes up \
multiple lines can be defined by the escape character as it is done here
url=example.com/api?auth_token=xyz
user_dir=${HOME}/test
unresolved = ${HOME}/files/${id}/${bar}/
fname_template = /opt/myapp/{arch}/ext/{objid}.dat
```


## Code
```python
from properties.p import Property

prop = Property(use_env = True)
dic_prop = prop.load_property_files('my_file.properties')


print(dic_prop)

# Output

# {'foo': 'I am awesome', 'bar': 'fudge-bar', 'chocolate': 'fudge', 'long': 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here', 'url': 'example.com/api?auth_token=xyz', 'user_dir': '/home/user/test', 'unresolved': '/home/user/files/${id}/fudge-bar/', 'fname_template': '/opt/myapp/{arch}/ext/{objid}.dat'}
```