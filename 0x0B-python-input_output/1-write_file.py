#!/usr/bin/python3
 """ function that returns the number of lines of a text file """


def append_write(filename="", text=""):
    """ function that returns the number of lines of a text file """I
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
