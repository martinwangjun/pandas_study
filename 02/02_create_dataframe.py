# -*- coding: utf-8 -*-
"""
    :author: Martin Wang(martin.wang@thermofisher.com)
    :license: MIT, see LICENSE for more details.
"""

import pandas as pd

scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Goset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-0416', '1937-10-16'],
    'Age': [37, 61]
})

print(scientists)

scientists = pd.DataFrame(
    data={
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-0416', '1937-10-16'],
        'Age': [37, 61]
    },
    index=['Rosaline Franklin', 'William Goset'],
    columns=['Occuptation', 'Born', 'Died', 'Age'])

print(scientists)

from collections import OrderedDict

scientists = pd.DataFrame(OrderedDict(
    [
        ('Name', ['Rosaline Franklin', 'William Goset']),
        ('Occupation', ['Chemist', 'Statistician']),
        ('Born', ['1920-07-25', '1876-06-13']),
        ('Died', ['1958-0416', '1937-10-16']),
        ('Age', [37, 61]),
    ])
)
print(scientists)
