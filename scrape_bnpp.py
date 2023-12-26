import datetime
import tabula
import time
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTChar
import re

# B4 - XS2237717850.pdf
# B - XS2033213849.pdf
dates = []
i = 1
text = ''
for page_layout in extract_pages("termsheets/B4 - XS2237717850-unlocked.pdf"):
    #print(page_layout.__dict__)
    if i in [2, 3]:
        objetos = page_layout.__dict__['_objs'][0]
        for element in objetos:
            if isinstance(element, LTChar):
                text += element.get_text()
        if i == 3:
            break
    i += 1

regex = r"([A-Z])\w+ [0-9]{2}th, [0-9]{4}"
matches = re.finditer(regex, text, re.MULTILINE)

current_table_num = 0
for matchNum, match in enumerate(matches, start=1):
    date_str = match.group()

    matches_0 = re.finditer(r"[A-Z][a-z]+[0-9]+", date_str, re.MULTILINE)
    new_starts = []
    for matchNum_0, match_0 in enumerate(matches_0, start=1):
        new_starts.append(match_0.end())
    if new_starts:
        date_str = date_str[new_starts[0]:]
        current_table_num += 1

    if current_table_num == 2:
        break
    dates.append(datetime.datetime.strptime(date_str, '%B %dth, %Y'))
print(dates)

dates.sort()
dates_str = [datetime.datetime.strftime(x, '%d %B %Y') for x in dates]
print(dates_str)

