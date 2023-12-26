import datetime
import tabula
import time
from pdfminer.high_level import extract_pages, extract_text

date_strs = []
i = 1
for page_layout in extract_pages("termsheets/F7 - XS2671818883.pdf"):
    if i == 3:
        objetos = page_layout.__dict__['_objs']

        j = 0
        for j in range(4 + 1):
            if j >= 3:
                dates_str = objetos[j].get_text().strip()
                dates_str_list = dates_str.split('\n')
                dates_str_list = dates_str_list[1: len(dates_str_list) - 1]
                date_strs.extend(dates_str_list)
                #dates.append(datetime.datetime.strptime(date_str, '%d %B %Y').date())
        break

    i += 1


print(date_strs)

dates = [datetime.datetime.strptime(date_str.strip(), '%B %d, %Y') for date_str in date_strs]
print(dates)

dates.sort()
dates_str = [datetime.datetime.strftime(x, '%d %B %Y') for x in dates]
print(dates_str)










