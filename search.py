# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

import sys
import webbrowser

from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results

"""
Usage:

$ python search.py linear ~/data/slate
$ python search.py index ~/data/slate
$ python search.py myhtable ~/data/slate
"""

impl = sys.argv[1] # EX: "linear" or "index" or "myhtable"
rootdir = sys.argv[2] # EX: "~/data/slate"
files = filelist(rootdir) # This is a list of (.txt) file names, under each sub dir (from "1" to "55") of the "slate" dir

# Uncomment the next line to test just the first 100 files instead of all files
# files = files[:100]
N = len(files) # N will be 4530
print(N, "files")

index = None

while True:
    terms = input("Search terms: ") # EX: "Ronald Reagan"
    terms = words(terms) # EX: ['reagan', 'ronald']

    if impl=='linear':
        # print("YES")
        # print(files)
        # print(terms)
        docs = linear_search(files, terms)

    elif impl == 'index':
        if index is None:
            index = create_index(files) # files is a list of fully-qualified filenames
            print("Index complete") # terms is a list of normalized words
        docs = index_search(files, index, terms)
    elif impl == 'myhtable':
        if index is None:
            index = myhtable_create_index(files)
            print("Index complete")
        docs = myhtable_index_search(files, index, terms)
    else:
        print("Invalid search type:", impl)
        break
    page = results(docs, terms)
    with open("/tmp/results.html", "w", encoding='UTF-8') as f:
        f.write(page)
    webbrowser.open_new_tab("file:///tmp/results.html")
