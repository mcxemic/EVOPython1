import operator
import re
from functools import reduce


def optimize_data(string, dictionary):
    """
    Get dictionary and string for parsing and return
    :param nested dictionary:
    :param tuple with string for parsing:
    :return pretty output with data from dictionary:
    """
    try:
        string = string.split('\n')
        dat = []

        if string[-1] == '': string = string[:-1]  # for multiply input
        for i in string: dat.append(re.split('{|} ', i))
        prestring = []
        for i in dat: prestring.append(i[0])  # rewrite to functional style
        dictionary_string = []
        for i in dat: dictionary_string.append(i[1])  # rewrite too
        string = []
        for i in dictionary_string: string.append(
            i.replace('{', ' ').replace('}', ' ').replace('[', ' ').replace(']', ' '))
        data = []
        for i in string: data.append(filter(None, i.split(' ')))

        dictionary_data = []
        for i in data: dictionary_data.append(str(reduce(operator.getitem, i, dictionary)))
        output = []
        for i in range(len(prestring)): output.append(prestring[i] + dictionary_data[i])

        return set(output)
    except KeyError as e:
        print("Key Error: ", e)
    except TypeError as message:
        print("Type Eroor: ", message)
        print("Maybe you input too match data?")
