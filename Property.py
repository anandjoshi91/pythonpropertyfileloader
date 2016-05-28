## Author : Anand Joshi
## Email : anandhjoshi@outlook.com



import re


class Property():

    ''' A class similar to Properties class in Java
        Reads varibales/properties defined in a file
        Allows cross referencing of variables
    '''

    # Dictionary which stores key value pair
    # Static member. Do not directly modify this
    props = {}

    def __init__(self,assign_token = '=', comment_token = '#', line_append_token = '\\'):
        ''' optional parameters
            A standard property file follows the convention
            =  is used to assign a vriable or property
            # for comments in the property file
            \ a long varibale definition can span across multiple lies. Use \ to continue to next line
            override them if your proprty file uses different convention
        '''
        self.assign_token = assign_token
        self.comment_token = comment_token
        self.line_append_token = line_append_token


    def load(self,*argv):
        ''' Load one or more property files
            Takes in the input path of the file as a String 
        '''

        if(len(argv) < 1):
            print('Please provide a property file to be loaded.')
        else:
            try :
                for prop_file in argv:
                    line = ''
                    with open(prop_file,'rt') as f:
                        for single_line in f:
                            l = single_line.strip()
                            if l and not l.startswith(self.comment_token):
                                if l.endswith(self.line_append_token):
                                    # Property descriptions spans multiple lines. Append new line with previous lines 
                                    line = line + l
                                    line = line[:-1] # Strip \ from the line
                                else:
                                    if( len(line) > 0):
                                        line = line + l
                                        l = line.strip()
                                    key_value = l.split(self.assign_token)
                                    key = key_value[0].strip()
                                    value = key_value[1].strip()

                                    if(key not in Property.props.keys()):
                                        Property.props[key] = value
                                        line = ''
                                    else:
                                        print('Property : ',key,' = ',value,' already defined !')
            except Exception as e:
                print('Error in loading property file. Check file(s) = ',argv)
                raise e

    def get(self,key):
        ''''Returns the property value for a defined key'''
        if(key not in Property.props.keys()):
            return
        else:
            return self._get(key)

    def _get(self,key):
        ''' Private method.
            Recursively evaluates a property defined
            in terms of other properties
        '''

        if(key in Property.props.keys()):
            val = Property.props[key]
        else:
            val = key

        evalset = set(re.findall(r'(?<={)[^}]*(?=})',val))

        try:
            # If the set is empty. This is the final value. return it
            if not evalset :
                return val
            else:
                for token in evalset :
                    replace_this = '${'+token+'}'
                    replace_with = Property.props[token]
                    val = val.replace(replace_this,replace_with)
                    return self._get(val)
        except Exception as e:
            print('Please check property files. Some property might not be defined. Check ',token)
            raise e

    def showall(self):
        return Property.props
                                        


    

    
