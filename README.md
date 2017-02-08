# pythonpropertyfileloader
### A python module to load  property files.
 Actually it is like the PropertyPlaceholderConfigurer in spring which lets you use ${variable-reference} to refer to already defined property ).


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

# {'foo': 'I am awesome', 'bar': 'fudge-bar', 'chocolate': 'fudge',
#  'long': 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here',
#  'url': 'example.com/api?auth_token=xyz'}

```
