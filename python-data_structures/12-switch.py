#!/usr/bin/python3

def uppercase_str(my_str):
    result = ""
    for char in my_str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
