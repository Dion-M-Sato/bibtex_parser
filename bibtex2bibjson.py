"""
via https://github.com/internaut/bibtex2bibjson/blob/master/bibtex2bibjson.py
"""
#!/usr/bin/python3

"""
A simple script to convert a single input bib-file to BibJSON output that is send to stdout.
"""

import sys
import bibjson
import os
import json
from datetime import datetime
import codecs

def main():
    """
    Script main function: Read arguments, produce BibJSON output.
    """
    if len(sys.argv) < 2:
        print("will output BibJSON to stdout", file=sys.stderr)
        print("usage: %s <bibtex-file>" % sys.argv[0], file=sys.stderr)
        exit(1)

    bibtex_file = sys.argv[1]

    # 'collection' identifier is the file name without extension
    collection = os.path.splitext(os.path.basename(bibtex_file))[0]

    # read the bibtex file
    with open(bibtex_file) as f:
        bibtex_str = f.read()

        # create BibJSON collection from file
        bibjson_collection = bibjson.collection_from_bibtex_str(
                bibtex_str,
                collection=collection,
                source=bibtex_file,
                created=datetime.utcnow().isoformat()
                )

        # print it to stdout with nice indentation
        k = 0
        while True:
            try:
                article = bibjson_collection['records'][k]
                print(article)
                bib_author_pre = article['author'][0]
                bib_author = bib_author_pre['name']
                print(bib_author)
                bib_title = article['title']
                print(bib_title)
                bib_journal_number = article['journal']['number']
                print(bib_journal_number)
                bib_journal_volume = article['journal']['volume']
                print(bib_journal_volume)
                bib_journal_name = article['journal']['name']
                print(bib_journal_name)
                bib_year = article['year']
                print(bib_year)
                print(bib_author+bib_title+bib_journal_name+bib_journal_number+bib_journal_volume+bib_year)
                k +=  1
            except IndexError:
                break

if __name__ == '__main__':
    main()
