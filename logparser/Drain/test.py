import re
import os
import numpy as np
import pandas as pd
import hashlib
from datetime import datetime

def generate_logformat_regex(logformat):
    """ Function to generate regular expression to split log messages
    """
    headers = []
    splitters = re.split(r'(<[^<>]+>)', logformat)
    print splitters
    regex = ''
    for k in range(len(splitters)):
        if k % 2 == 0:
            splitter = re.sub(' +', '\\\s+', splitters[k])
            regex += splitter
            print regex
        else:
            header = splitters[k].strip('<').strip('>')
            regex += '(?P<%s>.*?)' % header
            headers.append(header)
    regex = re.compile('^' + regex + '$')
    print headers,"regex=", regex

if __name__=='__main__':
    logformat= '<Date> <Time> <Pid> <Level> <Component>: <Content>'
    generate_logformat_regex(logformat)