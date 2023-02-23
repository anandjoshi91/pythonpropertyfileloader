from p import Property
import os
import sys
import pytest


def get_test_file(file = 'my_file.properties'):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), file)


def test_simple_prop_reader():
    prop = Property()
    dic_prop = prop.load_property_files(get_test_file())
    assert dic_prop.get('bar') == 'fudge-bar'
    assert dic_prop.get('foo') == 'I am awesome'
    assert dic_prop.get('long') == 'a very long property that is described in the property file which takes up multiple lines can be defined by the escape character as it is done here'
    assert dic_prop.get('url') == 'example.com/api?auth_token=xyz'
    assert len(dic_prop) == 8

def test_prop_reader_no_env():
    prop = Property()
    dic_prop = prop.load_property_files(get_test_file())
    assert dic_prop.get('unresolved') == '${HOME}/files/${id}/fudge-bar/'

def test_prop_reader_with_env():
    prop = Property(use_env=True)
    os.environ['HOME'] = '/home/user'
    dic_prop = prop.load_property_files(get_test_file())
    assert dic_prop.get('user_dir') == '/home/user/test'
    os.environ['HOME'] = ''

def test_prop_reader_with_env_override():
    prop = Property(use_env=True)
    os.environ['bar'] = 'ice-cream-bar'
    dic_prop = prop.load_property_files(get_test_file())
    assert dic_prop.get('bar') == 'fudge-bar'
    os.environ['bar'] = ''

def test_prop_reader_with_missing_vals():
    prop = Property()
    prop.load_property_files(get_test_file())
    assert len(prop.get_missing_values()) == 2
    assert 'HOME' in prop.get_missing_values()
    assert 'id' in prop.get_missing_values()

def test_prop_reader_with_multiple_files():
    prop = Property()
    dic_prop = prop.load_property_files(get_test_file('test-files/test1.prop'), get_test_file('test-files/test2.properties'))
    assert dic_prop.get('app') == 'test-app-2.5'

def test_prop_reader_with_custom_separator():
    prop = Property(assign_token='=>')
    dic_prop = prop.load_property_files(get_test_file('test-files/test3.properties'))
    assert dic_prop.get('foo') == 'bar'