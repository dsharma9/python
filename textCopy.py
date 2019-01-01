#!/usr/bin/env python3.7
import pyperclip

print("This program is got process the copied clipboard text and save it in the same variable")

text = pyperclip.paste()

lines = text.split('.')

for i in range(len(lines)):
    lines[i] = " * " + lines[i]

text = '.'.join(lines)
print(text)
print()
print()
print()
print(lines[0:])
pyperclip.copy(text)
print()
print("the modified text is ")
print(text)
