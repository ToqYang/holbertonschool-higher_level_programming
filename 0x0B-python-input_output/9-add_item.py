#!/usr/bin/python3
""" Load add, save json file """

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    import sys
    """ Take the argv and append the last value at the JSON file """

    try:
        filename = "add_item.json"
        my_list = load_from_json_file(filename)
    except:
        filename = "add_item.json"
        my_list = []
        save_to_json_file(my_list, filename)

    le = len(sys.argv)
    counter = 1

    while(counter < le):
        my_list.append(sys.argv[counter])
        counter += 1

    save_to_json_file(my_list, filename)
