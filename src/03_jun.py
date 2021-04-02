# -*- coding: utf-8 -*-
"""
Generate Reports according to Jun Luo (jun.luo@thermofisher.com) Requirements.

@author:    Martin Wang(martin.wang@thermofisher.com)
@license:   MIT, see LICENSE for more details.
@copyright: Thermo Fisher Scientific
"""

import pandas as pd

sales_team = pd.DataFrame()
print(sales_team)

pipeline = pd.read_excel(
    '../data/funnel.xlsx',
    sheet_name='Pipeline',
    engine='openpyxl')


backlog = pd.read_excel(
    '../data/funnel.xlsx',
    sheet_name='Backlog QDay1',
    engine='openpyxl')

# print(pipeline)

# pipeline.to_excel('../output/03.xlsx', index=False)

print(pipeline.shape)
print(backlog.shape)
