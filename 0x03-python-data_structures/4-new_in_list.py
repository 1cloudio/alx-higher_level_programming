#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    pip = my_list[:]
    if idx >= 0 and idx < len(pip):
        pip[idx] = element
    return pip
