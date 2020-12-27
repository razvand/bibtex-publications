# Manage BibTeX Publications

This is a template repository for managing your list of BibTeX publications.
[BibTeX](http://www.bibtex.org/) is a format and a set of tools for managing bibliographical references.
You store your publications in the `publications.bib` file and your can then include them in your LaTeX files, process them and list them.

The `publications.bib` file stores some sample BibTeX entries for testing.
Update it with your own publications in BibTeX format.
Most publishing and indexing services (such as [ACM Digital Library](https://dl.acm.org/), [IEEExplore](https://ieeexplore.ieee.org/Xplore/home.jsp), [DBLP](https://dblp.org/), [SCOPUS](https://www.scopus.com/home.uri), [arXiv](https://arxiv.org/)) allow you to export citations in BibTeX format; you don't have to do it from scratch.

List your publications in PDF format using the `publications.tex` file by running `make`.
Once you run `make`, you create the `publications.pdf` file.
If you update the `publications.bib` file, you run `make` again to regenerate the `publications.pdf` file.
The `publications.tex` file is a basic LaTeX file; update it / customize it to your needs.

Process the items in `publications.bib` using the [BibtexParser Python library](https://bibtexparser.readthedocs.io/en/master/).
BibtexParser gives you access to the fields in each BibTex item.
You can then print certain fields or select some entries.
See the `bib_printer.py` as a sample BibtexParser processing script; it prints the publication year, title, DOI (Digital Object Identifier) and other fields for entries in the `publications.bib` file.
