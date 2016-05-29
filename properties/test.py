from properties import p

prop = p.Property()
prop.load('my_file.properties')
print(prop.get('foo')) # I am awesome
print(prop.get('bar')) # fudge-bar
