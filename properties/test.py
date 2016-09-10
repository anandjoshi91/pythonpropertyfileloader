from properties import p

prop = p.Property()
prop.load('my_file.properties')

print(prop.get('foo'))
# I am awesome

print(prop.get('bar'))
# fudge-bar

print(prop.get('long'))
# a very long property that tis described in the property file which takes up multiple lines can be defined by the escape character as it is done here

print(prop.get('unknown'))
# None

#  Use showall() to get the key value pair of all the properties defined

print(prop.showall())