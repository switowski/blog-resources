# from collections import OrderedDict

# def perform_operations(dictionary):
#     dictionary[200] = 'goodbye'
#     is_50_included = 50 in dictionary
#     item_20 = dictionary.get(20)
#     non_existing_item = dictionary.get('a')

# def test_ordereddict():
#     dictionary = OrderedDict.fromkeys(range(100), 'hello world')
#     perform_operations(dictionary)

# def test_dict():
#     dictionary = dict.fromkeys(range(100), 'hello world')
#     perform_operations(dictionary)

from collections import OrderedDict

def perform_operations(dictionary):
    dictionary[20000] = 'goodbye'
    is_5000_included = 5000 in dictionary
    item_2000 = dictionary.get(2000)
    nonexistent_item = dictionary.get('a')

def ordereddict():
    dictionary = OrderedDict.fromkeys(range(10000), 'hello world')
    perform_operations(dictionary)

def standard_dict():
    dictionary = dict.fromkeys(range(10000), 'hello world')
    perform_operations(dictionary)
