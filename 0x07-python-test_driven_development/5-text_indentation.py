#!/usr/bin/python3
"""
prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after ., ? and :."""

    if type(text) is not str:
        raise TypeError('text must be a string')

    l = len(text)
    i = 0
    if text[0] == " ":
        while text[i] == " ":
            i += 1
    while i < l:
        if text[i] == " " and text[i - 1] == ".":
            while text[i] == " ":
                i += 1
        if text[i] == " " and text[i - 1] == "?":
            while text[i] == " ":
                i += 1
        if text[i] == " " and text[i - 1] == ":":
            while text[i] == " ":
                i += 1
        if text[i] == " " and text[i - 1] == "\n":
            while text[i] == " ":
                i += 1
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("{}".format(text[i]))
            print("")
        else:
            print("{}".format(text[i]), end="")
        i += 1
