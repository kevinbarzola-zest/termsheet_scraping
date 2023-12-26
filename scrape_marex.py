import datetime
import tabula
import time
from pdfminer.high_level import extract_pages, extract_text

dates = []
i = 1
for page_layout in extract_pages("termsheets/B5M - XS2275812555.PDF"):
    if i == 4:
        objetos = page_layout.__dict__['_objs']

        j = 0
        for j in range(185):
            if j >= 114:
                date_str = objetos[j].get_text().strip()
                dates.append(datetime.datetime.strptime(date_str, '%d %B %Y').date())
        break
    i += 1
dates.sort()
dates_str = [datetime.datetime.strftime(x, '%d %B %Y') for x in dates]
print(dates_str)







