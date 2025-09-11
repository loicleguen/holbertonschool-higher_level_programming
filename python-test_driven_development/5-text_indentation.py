#!/usr/bin/python3
def text_indentation(text):
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
        print(x, end="")
