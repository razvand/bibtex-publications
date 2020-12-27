#!/usr/bin/env python2

import bibtexparser

with open('publications.bib') as f:
    bibdb = bibtexparser.load(f)

for e in bibdb.entries:
    y = e['year']
    t = e['title']
    doi = ""
    if 'doi' in e.keys():
        doi = e['doi']
    wos = ""
    if 'note' in e.keys():
        if e['note'].find('WOS') != -1:
            wos = e['note'].split(':')[1]
    j = ""
    if e['ENTRYTYPE'] == 'inproceedings':
        j = e['booktitle']
    elif e['ENTRYTYPE'] == 'article':
        v = ''
        n = ''
        if 'volume' in e.keys():
            v = e['volume']
        if 'number' in e.keys():
            n = e['number']
        j = "{}, vol. {}, num. {}".format(e['journal'], v, n)
    issn = ""
    isbn = ""
    if 'isbn' in e:
        isbn = e['isbn']
    if 'issn' in e:
        issn = e['issn']
    print u"{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(y, t, doi, wos, "", j, issn, "", isbn)
