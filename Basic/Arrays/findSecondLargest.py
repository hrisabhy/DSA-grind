from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys


def findSecondLargest(sequenceOfNumbers):
    max_element = float("-inf")
    second_max = float("-inf")
    for i in range(len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > max_element:
            max_element = sequenceOfNumbers[i]
    for i in range(len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > second_max and sequenceOfNumbers[i] != max_element:
            second_max = sequenceOfNumbers[i]
    if sequenceOfNumbers.count(max_element) == len(sequenceOfNumbers):
        return -1
    else:
        return second_max
    pass


# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n


# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t - 1
