def code(str):
    str_1 = ''
    for char in str:
        str_1 += chr(ord(char) + 3)
    return str_1

print(code("RutteAlkmaarDen Helder"))