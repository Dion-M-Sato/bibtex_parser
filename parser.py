import bibtexparser
from bibtexparser.bparser import BibTexParser
import json

with open('database_sample.bib') as bibtex_file:
    parser = BibTexParser()
    load_database = bibtexparser.load(bibtex_file)
    #print(bib_database.entries)
    bib_database = load_database.entries
    bib_database = json.dumps(bib_database, utf=true)
    print(bib_database)
