# pythonpropertyfileloader

![Build](https://github.com/anandjoshi91/pythonpropertyfileloader/actions/workflows/python-package.yml/badge.svg)
[![Downloads](https://static.pepy.tech/badge/property)](https://pepy.tech/project/property)

## A python module to load property files

- Load multiple property files
- Recursively define properties (Similar to [PropertyPlaceholderConfigurer](https://docs.spring.io/spring-framework/docs/2.5.x/javadoc-api/org/springframework/beans/factory/config/PropertyPlaceholderConfigurer.html)) in spring which lets you use `${variable-reference}` to refer to already defined property)
- Placeholders are also resolved using env variables, like the spring property loader does, if the class is instantiated with the `use_env` argument (defaults to false for backward compatibility)

## Install

```bash
pip install property
```

## Example

### my_file.properties

```bash
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

### Code

```python
from properties.p import Property


## set use_env to evaluate properties from shell / os environment
prop = Property(use_env = True)
dic_prop = prop.load_property_files('my_file.properties')


print(dic_prop)

# Output

# {'foo': 'I am awesome', 'bar': 'fudge-bar', 'chocolate': 'fudge',
#  'long': 'a very long property that is described in the property file which takes up multiple lines
#  can be defined by the escape character as it is done here', 'url': 'example.com/api?auth_token=xyz',
#  'user_dir': '/home/user/test',
#  'unresolved': '/home/user/files/${id}/fudge-bar/',
#  'fname_template': '/opt/myapp/{arch}/ext/{objid}.dat'}
```
