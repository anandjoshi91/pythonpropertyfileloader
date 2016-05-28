# pythonpropertyfileloader
A python module to load  property files. Similar to the Properties class in Java.


Example
--------
Let's say you have the following properties defined in my_file.properties file


foo = I am awesome
bar = ${chocolate}-bar
chocolate = fudge


Code to load the above properties

prop = Property()
prop.load('path/to/my_file.properties')
prop.get('foo')  # I am awesome
prop.get('bar')  # fudge-bar
