import re
import os
from collections import OrderedDict


class Property:
    """ A class similar to Properties class in Java
        Reads variables/properties defined in a file
        Allows cross referencing of variables
    """

    def __init__(self, assign_token: str = '=', comment_token: str = '#', line_append_token: str = '\\',
            ordered: bool = False, use_env: bool = False ):
        """ 
        Args:
            assign_token: Assignments operator within your property files. Default (=)
            comment_token: To ignore comments in property files. Default (#)
            line_append_token: A long property can span across multiple lines. Uses default \\ ignore line breaks
            ordered: If you want the properties to be maintained in ordered dictionary. Default (False)
            use_env: Resolve values from environment variables. Default (False)

        Returns:
            Property() object with the set configurations
        """
        self.__props = OrderedDict() if ordered else dict()
        self.__assign_token = assign_token
        self.__comment_token = comment_token
        self.__line_append_token = line_append_token
        self.__use_env = use_env
        self.__missing = None

    def load_property_files(self, *argv):
        """
        Args:
            argv: Takes variable length of arguments. Enter the property files to be loaded.
            param2: This is a second param.

        Returns:
            Dictionary. Key value pair of properties after their evaluation

        Raises:
            Exception: Raises an exception if unable to load the files
        """
        self.__read_property_files(*argv)

        # reset missing keys
        self.__missing = set()
        for key in self.__props.keys():
            self.__props[key] = self.__evaluate_properties(key)

        return self.__props

    def get_missing_values(self):
        return self.__missing

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
                                    index_of_separator = l.find(self.__assign_token)
                                    assign_token_size = len(self.__assign_token)
                                    key = l[:index_of_separator].strip()
                                    value = l[index_of_separator+assign_token_size:].strip()

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

        evalset = set(re.findall(r'(?<=\${)[^}]*(?=})', val))

        try:
                for token in evalset:
                    replace_this = '${' + token + '}'
                    replace_with = replace_this
                    if token in self.__props.keys():
                        replace_with = self.__props[token]
                    elif self.__use_env :
                        replace_with = os.getenv(token, replace_this)
                    if replace_with != replace_this:
                        val = self.__evaluate_properties(val.replace(replace_this, replace_with))
                    else:
                        self.__missing.add(token)
        except Exception as error:
            raise ValueError('Please check property files. Some property might not be defined. Check ', token, ' ',
                             error)
        return val
