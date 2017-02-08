import re


class Property:
    """ A class similar to Properties class in Java
        Reads variables/properties defined in a file
        Allows cross referencing of variables
    """

    def __init__(self, assign_token='=', comment_token='#', line_append_token='\\'):
        """ optional parameters
            A standard property file follows the convention
            =  is used to assign a variable or property
            # for comments in the property file
            \ a long variable definition can span across multiple lines. Use \ to continue to next line
            override them if your property file uses different convention
        """
        self.__props = {}
        self.__assign_token = assign_token
        self.__comment_token = comment_token
        self.__line_append_token = line_append_token

    def load_property_files(self, *argv):
        """
        :param argv: Takes variable length of arguments. Enter the property files to be loaded.
        :return: Dictionary. Key value pair of properties after their evaluation
        """
        self.__read_property_files(*argv)

        for key in self.__props.keys():
            self.__props[key] = self.__evaluate_properties(key)

        return self.__props

    def __read_property_files(self, *argv):
        """ Reads one or more property files
            Takes in the input path of the file as a String
        """

        if len(argv) < 1:
            print('Please provide a property file to be loaded.')
        else:
            try:
                for prop_file in argv:
                    line = ''
                    with open(prop_file, 'rt') as f:
                        for single_line in f:
                            l = single_line.strip()
                            if l and not l.startswith(self.__comment_token):
                                if l.endswith(self.__line_append_token):
                                    # Property descriptions spans multiple lines. Append new line with previous lines 
                                    line += l
                                    line = line[:-1]  # Strip \ from the line
                                else:
                                    if len(line) > 0:
                                        line += l
                                        l = line.strip()
                                    index_of_separator = l.find('=')
                                    key = l[:index_of_separator].strip()
                                    value = l[index_of_separator+1:].strip()

                                    if key not in self.__props.keys():
                                        self.__props[key] = value
                                        line = ''
                                    else:
                                        print('Property : ', key, ' = ', value, ' already defined !')

            except Exception as error:
                raise IOError('Error in loading property file. Check file(s) = ', argv, ' ', error)

    def __evaluate_properties(self, key):
        """ Private method.
            Recursively evaluates a property defined
            in terms of other properties
        """

        if key in self.__props.keys():
            val = self.__props[key]
        else:
            val = key

        evalset = set(re.findall(r'(?<={)[^}]*(?=})', val))

        try:
            # If the set is empty. This is the final value. return it
            if not evalset:
                return val
            else:
                for token in evalset:
                    replace_this = '${' + token + '}'
                    replace_with = self.__props[token]
                    val = val.replace(replace_this, replace_with)
                    return self.__evaluate_properties(val)
        except Exception as error:
            raise ValueError('Please check property files. Some property might not be defined. Check ', token, ' ',
                             error)
