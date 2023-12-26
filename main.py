import tabula
import time
from pdfminer.high_level import extract_pages, extract_text
import math
import pandas as pd

notes = pd.read_excel('notas_brokers.xlsx')
note_ids = notes['Nombre'].tolist()
issuers = notes['ISSUER'].tolist()

notes_by_issuer = {}
for issuer in set([issuer.upper() for issuer in issuers if type(issuer) == str]):
    if type(issuer) == str:
        notes_by_issuer[issuer] = []
#print(notes_by_issuer)

for i in range(len(note_ids)):
    if type(issuers[i]) == str:
        notes_by_issuer[issuers[i].upper()].append(note_ids[i])

for key, value in notes_by_issuer.items():
    print(f"Issuer: {key}, Notes: {value}")