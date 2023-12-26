import datetime
import tabula
import time
from pdfminer.high_level import extract_pages, extract_text
import re

date_strs = []
i = 1
for page_layout in extract_pages("termsheets/D54 - XS2430954417.pdf"):
    if i == 3:
        objetos = page_layout.__dict__['_objs']
        #print(objetos)

        j = 0
        for j in range(143 + 1):
            if j >= 100:
                text = objetos[j].get_text().strip()
                text = ' '.join(text.split())
                date_strs.append(text)
        break

    i += 1

print(date_strs)

indices_to_pop = []
dates_to_add = []
for i in range(len(date_strs)):
    matches = re.finditer(r"[0-9]+ [A-Z]", date_strs[i], re.MULTILINE)
    split_index = None
    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                            end=match.end(), match=match.group()))
        split_index = match.end()
        indices_to_pop.append(i)
    if split_index:
        dates_to_add.append(date_strs[i][:split_index - 2])
        dates_to_add.append(date_strs[i][split_index - 1:])

print(dates_to_add)
print(indices_to_pop)
print(date_strs)

indices_to_pop.sort(reverse=True)

for index in indices_to_pop:
    date_strs.pop(index)
date_strs.extend(dates_to_add)
print(date_strs)

dates = [datetime.datetime.strptime(date_str.strip(), '%B %d, %Y') for date_str in date_strs]
print(dates)

dates.sort()
dates_str = [datetime.datetime.strftime(date, '%B %d, %Y') for date in dates]
print(dates_str)
print(len(dates_str))

"""
dates.sort()
dates_str = [datetime.datetime.strftime(x, '%d %B %Y') for x in dates]
print(dates_str)
"""







