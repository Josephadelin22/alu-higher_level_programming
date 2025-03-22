#!/usr/bin/python3
def uppercase(str):
    result = "".join(chr(ord(c) - 32) if 'a' <= c <= 'Z' else c for c in str)
    print("{}".format(esult))
