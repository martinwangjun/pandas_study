# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import configparser



from bs4 import BeautifulSoup
import openpyxl




class SFDB(object):
    def sync(self):
        i = 0
        j = 0
        rs = list()
        with open('sfdc_all_accounts2.xls', 'r', encoding='utf-8') as f:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'lxml')
            table = soup.table
            trs = table.find_all("tr")
            for tr in trs:
                row = list()
                tds = None
                if i == 0:
                    tds = tr.find_all("th")
                else:
                    tds = tr.find_all("td")
                for td in tds:
                    # print(td.get_text())
                    row.append(td.get_text())
                rs.append(row)
                i = i + 1
            self.write07Excel(rs, "result.xlsx")

        return i

    def write07Excel(self, rs, path):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = '2007测试表'

        for i in range(0, len(rs)):
            for j in range(0, len(rs[i])):
                content = str(rs[i][j])
                sheet.cell(row=i+1, column=j+1, value=content)
        wb.save(path)
        print("写入数据成功！")



if __name__ == "__main__":
    start = time.time()
    carrier = SFDB()
    qty = carrier.sync()

    end = time.time()

    print('Finish copying %d records in %s seconds.' % (
        qty, int(end - start))
    )
