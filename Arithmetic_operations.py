#!/usr/bin/env python
# coding: utf-8
"""
sum, average , product ,difference and division of two given inputs
"""


def inputs():
    """
    takes user input to perform various operations
    :return: None. Prints the values.
    """
    v_1 = int(input("enter the first number:"))
    v_2 = int(input("enter the second number:"))
    sum1(v_1, v_2)
    average(v_1, v_2)
    product(v_1, v_2)
    diff(v_1, v_2)
    div(v_1, v_2)


def sum1(a, b):
    """
    function to add two numbers
    :param a: int/float/string datatype
    :param b: int/float/string datatype
    :return: prints the int/float/string value of sum of two parameters.
    """
    c = a+b
    print("The sum of given inputs:", c)


def average(a, b):
    """
    function to take average of two numbers
    :param a: int/float/string datatype
    :param b: int/float/string datatype
    :return:  prints the int/float/string value of sum of two parameters.
    """
    c = (a+b)/2
    print("The average of given inputs", c)


def product(a, b):
    """
    function to multiply two numbers
    :param a: int/float/string datatype
    :param b: int/float/string datatype
    :return: prints the int/float/string value of sum of two parameters.
    """
    c = a*b
    print("The product of given inputs", c)


def diff(a, b):
    """
    function to subtract b from a
    :param a: int/float/string datatype
    :param b: int/float/string datatype
    :return:  prints the int/float/string value of sum of two parameters.
    """
    c = a-b
    print("The differnce of given inputs", c)


def div(a, b):
    """
    function to divide a by b. Both the values must be of same datatype.
    :param a: int/float/string datatype
    :param b: int/float/string datatype
    :return: prints the int/float/string value of sum of two parameters.
    """
    if b > 0:
        c = a/b
        d = a % b
        print("Quotient =", c, "remainder =", d)
    else:
        print("denominator should be greater than zero")


inputs()