import ctypes
import re

import pyperclip


def message_box(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)


a = pyperclip.paste()

reg = re.compile(r"(?:(?<=\. |\? |\! )|(?<=^))\w|\bi'm\b|\bi\b")


def replacer(match):
    thing = match.group(0).lower()
    if thing == "i'm":
        return "I'm"
    return thing.upper()


result = reg.sub(replacer, a)
pyperclip.copy(result)

message_box("Text fixed!", "Text has been fixed and copied to your clipboard!")
