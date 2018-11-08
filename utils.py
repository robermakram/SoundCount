import os
import wave
import logging
import contextlib
import environment as env
import speech_recognition as sr

from os import path


def calc(array, first, last):
    sum = 0
    for x in range(first, last+1):
        sum += array[x]
    return sum
