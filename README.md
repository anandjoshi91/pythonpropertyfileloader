# pythonpropertyfileloader
### A python module to load property files.
 Actually it is like the PropertyPlaceholderConfigurer in spring which lets you use ${variable-reference} to refer to already defined property ).

 Placeholders are also resolved using env variables, like the spring property loader does, if the class is istantiated with the 'use_env' argument (defaults to false for backward compatibility)

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
```


## Code
```python
from properties.p import Property

prop = Property()
dic_prop = prop.load_property_files('my_file.properties')


print(dic_prop)

# Output

# OrderedDict([('foo', 'I am awesome'), ('bar', 'fudge-bar'), ('chocolate', 'fudge'),
# ('long', 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here'),
# ('url', 'example.com/api?auth_token=xyz')])
```

```python
from properties.p import Property

prop = Property(ordered=False)
dic_prop = prop.load_property_files('my_file.properties')


print(dic_prop)

# Output

# {'bar': 'fudge-bar', 'chocolate': 'fudge', 'url': 'example.com/api?auth_token=xyz', 'foo': 'I am awesome',
# 'long': 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here'}
```

## env variables

Use test.py and check the different outputs

`python3 properties/test.py env`

vs.

`python3 properties/test.py noenv`

