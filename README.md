# pythonpropertyfileloader


[![Downloads](https://static.pepy.tech/badge/property)](https://pepy.tech/project/property)
![Build](https://github.com/anandjoshi91/pythonpropertyfileloader/actions/workflows/python-package.yml/badge.svg)
![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/anandjoshi91/a10c3bfcf9d174b0b0119bfd3d8d1c82/raw/pythonpropertyfileloader__main.json)

## A python module to load property files

- Load multiple property files
- Recursively define properties (Similar to [PropertyPlaceholderConfigurer](https://docs.spring.io/spring-framework/docs/2.5.x/javadoc-api/org/springframework/beans/factory/config/PropertyPlaceholderConfigurer.html)) in spring which lets you use `${variable-reference}` to refer to already defined property)
- Placeholders are also resolved using env variables, like the spring property loader does, if the class is instantiated with the `use_env` argument (defaults to false for backward compatibility)

## Install

Available on [PyPI](https://pypi.org/project/property/)

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

## Read multiple files
## dic_prop = prop.load_property_files('file1', 'file2')


print(dic_prop)

# Output

# {'foo': 'I am awesome', 'bar': 'fudge-bar', 'chocolate': 'fudge',
#  'long': 'a very long property that is described in the property file which takes up multiple lines
#  can be defined by the escape character as it is done here', 'url': 'example.com/api?auth_token=xyz',
#  'user_dir': '/home/user/test',
#  'unresolved': '/home/user/files/${id}/fudge-bar/',
#  'fname_template': '/opt/myapp/{arch}/ext/{objid}.dat'}
```

## Develop

```bash
git clone https://github.com/anandjoshi91/pythonpropertyfileloader.git
cd pythonpropertyfileloader

## make your changes and open a PR - https://github.com/anandjoshi91/pythonpropertyfileloader/pulls
## Ensure all tests pass

## Check Dependencies
pip install pipreqs
pipreqs .

## Test
pip install pytest
pytest

## Publish to PyPi
pip install twine

update setup.py
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```