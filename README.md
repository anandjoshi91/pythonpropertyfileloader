# pythonpropertyfileloader
### A python module to load  property files.
 Actually it is like the PropertyPlaceholderConfigurer in spring which lets you use ${variable-reference} to refer to already defined property ).


Install
----------

```pip install property```



Example
---------

```python
from properties.p import Property

prop = Property()
dic_prop = prop.load_property_files('my_file.properties')


print(dic_prop)

```
