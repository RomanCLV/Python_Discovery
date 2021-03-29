# -*- coding: utf-8 -*-

"""
base64 module

Copyright © 2021 Roman Clavier

Module base64 by Roman Clavier.
"""
import string


def _check(obj):
    print(obj)


def encode(to_encode):
    """
    Function to encode a string with the base64 encoding

    :param to_encode: The string to encode
    :return: The string encoded
    """
    chars = _get_chars(to_encode)
    _check(chars)
    chars = _get_chars_ascii(chars)
    _check(chars)
    chars = _convert_decimals_to_binary(chars)
    _check(chars)
    binary = _join_array(chars)
    _check(binary)
    chars = _binary_to_list_of_n_bytes(binary, 6)
    _check(chars)
    _format_binaries_block_of_6_binaries(chars)
    _check(chars)
    chars = _convert_binaries_to_decimal(chars)
    _check(chars)
    chars = _convert_decimals_to_base64(chars)
    _check(chars)
    to_encode = _join_array(chars)
    _check(to_encode)
    to_encode = _format_base64(to_encode)
    _check(to_encode)
    return to_encode


def decode(to_decode):
    """
    Function to decode a string encoded in base64

    :param to_decode: The string to decode
    """
    to_decode = _format_base64(to_decode)
    chars = _convert_base64_to_decimals(to_decode)
    _check(chars)
    chars = _convert_decimals_to_binary(chars, False)
    _check(chars)
    _format_binaries_block_to_remove_last_0(chars)
    _check(chars)
    to_decode = _join_array(chars)
    chars = _binary_to_list_of_n_bytes(to_decode, 8)
    _check(chars)
    chars = _convert_binaries_to_decimal(chars)
    _check(chars)
    chars = _get_ascii_from_decimals(chars)
    _check(chars)
    to_decode = _join_array(chars)
    return to_decode


def _get_chars(to_encode):
    """
    Get a characters array

    :param to_encode: The initial string to encode
    :return: An array of each character of the initial string to encode
    """
    return list(to_encode)


def _get_chars_ascii(chars):
    """
    Get the ASCII values of each character of the sequence given

    :param chars: The array of each character of the initial string to encode
    :return: An array of the ASCII value of each character of the initial string to encode
    """
    return [ord(x) for x in chars]


def _get_ascii_from_decimals(decimals):
    """
    Get the ASCII values from the decimals sequence given

    :param decimals: The array of each decimal value
    :return: An array of the ASCII value
    """
    return [chr(x) for x in decimals]


def _convert_decimals_to_binary(chars, in_octet=True):
    """
    Get the Binary values of each character of the sequence given

    :param chars: The array of the ASCII value of each character of the initial string to encode
    :return: An array of the binary (8 bits) value of each character of the initial string to encode
    """
    return [format(x, '08b' if in_octet else '06b') for x in chars]


def _join_array(chars):
    """
    Join the given characters array

    :param chars: The array of the binaries value (8 bits) of each character of the initial string to encode
    :return: The string given by join the chars
    """
    return ''.join(chars)


def _binary_to_list_of_n_bytes(binary, n):
    """
    Format the binary string into an array of byte (6 bytes -> 2^6 = 64)

    :param binary: The string in binary (multiple of 8)
    :return: An array of 6 bytes by item
    """
    return [binary[i:i + n] for i in range(0, len(binary), n)]


def _format_binaries_block_of_6_binaries(binaries):
    """
    Check and add missing "0" to the last item to have a byte of 6 digits

    :param binaries: The source array
    """
    if len(binaries) > 0:
        index = len(binaries) - 1
        while len(binaries[index]) < 6:
            binaries[index] += "0"


def _format_binaries_block_to_remove_last_0(binaries):
    if len(binaries) > 0:
        while binaries[-1][-1] == '0':
            binaries[-1] = binaries[-1][:-1]
            if len(binaries[-1]) == 0:
                break


def _convert_binaries_to_decimal(binaries):
    """
    Get decimals array from a bytes array

    :param binaries: The array of binary values (6 bits)
    :return: An array of decimal values
    """
    return [int(x, 2) for x in binaries]


def _get_base64_table():
    """
    Get a string with all the base64 characters with the format Uppercase, Lowercase, Digits, +, /, =

    :return: The base64 table
    """
    return string.ascii_uppercase + string.ascii_lowercase + string.digits + "+" + "/" + "="


def _convert_decimals_to_base64(decimals):
    """
    Get an array of base64 value from a decimals [0-64] array

    :param decimals: An array of decimals value
    :return: An array of characters
    """
    table_base64 = _get_base64_table()
    return [table_base64[x] for x in decimals]


def _convert_base64_to_decimals(base64):
    """
    Get an array of decimals of each character of the base64 given

    :param base64: The source to extract
    :return: An array od decimals
    """
    table_base64 = _get_base64_table()
    decimals = [table_base64.index(x) for x in base64]
    while decimals.__contains__(64):
        decimals.remove(64)
    return decimals


def _format_base64(base64):
    while len(base64) % 4 != 0:
        base64 += "="
    return base64
