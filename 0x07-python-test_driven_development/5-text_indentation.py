#!/usr/bin/python3
"""
The module search characters in specific

and after the replaces for indent the text
"""


def text_indentation(text):
    """
    First search if not is a string, we give
    TypError or if not, replace's text and print
    text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(". ", ".\n\n")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")

    print(text)
