#!/usr/bin/python3
"""
Module that defines a function text_indentation.
"""
def text_indentation(text):
    """
    Indents the text by adding two new lines after each of these characters: ., ? and :.
    """

    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = ""
    for i in text:
        x += i
        if i in ".?:":
            print(x.strip())
            print()
            x = ""
    if x.strip():
        print(x.strip(), end="")
