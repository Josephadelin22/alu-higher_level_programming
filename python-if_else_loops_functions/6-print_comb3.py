#!/usr/bin/python3

print(", ".join(".{:02}".format(i) for i in range(10, 100) if i // 10 < i % 10))
