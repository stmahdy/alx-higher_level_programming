#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            ind = my_list.index(search)
            my_list[ind] = replace
    return my_list
