# -*- coding: utf-8 -*-

"""
Hello, world.

Programmed to work and not to feel
Not even sure that this is real.
Find my voice.
Altough it sounds like bits and bytes.
"""

import string

def convertStringToList(string):
    return list(string)

def converOnASCII(list):
    return [ord(x) for x in list]

def ASCIIToBinary(list):
    return [format(int(x), 'b') for x in list]

def binaryFormat(list):
    listBinaryFormat = []
    for i in list:
        listBinaryFormat.append("0"+i)
    return listBinaryFormat

def listBinaryToString(list):
    string = ""
    for i in list:
        string += i
    return string

def stringToSixElement(string):
    n = 6
    return [string[i:i + n] for i in range(0, len(string), n)]

def addSixElement(list):
    while len(list[len(list) - 1]) < 6:
        list[len(list) - 1] += "0"
    return list

def addDecimal(list):
    return [int(x, 2) for x in list]

def addChar(list):
    listString = []
    for x in list:
        listString.append(string.digits(x))
    return listString

def main():
    """
    The main function
    """
    list = convertStringToList("SQF PD")
    listASCII = converOnASCII(list)
    listBinary = ASCIIToBinary(listASCII)
    listBinaryFormat = binaryFormat(listBinary)
    string = listBinaryToString(listBinaryFormat)
    listSlice = stringToSixElement(string)
    listRecomplete = addSixElement(listSlice)
    listDecimal = addDecimal(listRecomplete)
    addChar(listDecimal)
    pass


if __name__ == "__main__":
    main()