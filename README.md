# pythonpropertyfileloader
## A python module to load  property files.
### Actually it is like the PropertyPlaceholderConfigurer in spring which lets you use ${variable-reference} to refer to already defined property ).


Example
--------
Let's say you have the following properties defined in my_file.properties file


foo = I am awesome  
bar = ${chocolate}-bar  
chocolate = fudge
long = a very long property that is described in the property file which takes up \
multiple lines can be defined by the escape character as it is done here

Code to load the above properties  

from properties import p

prop = p.Property()  
prop.load('path/to/my_file.properties')  
prop.get('foo')  # I am awesome  
prop.get('bar')  # fudge-bar
prop.get('long')  # a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here
prop.get('unknown')   # None

Use showall() to get the key value pair of all the properties defined in the file(s)

print(prop.showall()) # {'long': 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here', 'foo': 'I am awesome', 'chocolate': 'fudge', 'bar': '${chocolate}-bar'}

To load multiple property files use

prop.load('path/to/first_file','path/to/second_file',....'path/to/nth_file')
