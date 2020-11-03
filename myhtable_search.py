# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """

    # dct_index = defaultdict() # Create an empty dict
    # for file in files: # Iterate through every given file names
    #     s_content = get_text(file) # Turn each file name into a string content
    #     lst_word = words(s_content) # Turn the string content into a list of normalized words
    #     for word in lst_word: # For each normalized words, update the dict by word-file as key-value pairs
            # if word not in dct_index:
            #     dct_index[word] = {file} # If the key doesn't exist, create one
            # else:
            #     dct_index[word].add(file) # If the key exist, add the file name into the set of the file names under that word
    # return dct_index


    NBUCKETS = 4011
    table = htable(NBUCKETS) # Create an empty dict
    for idx,fname in enumerate(files): # Iterate through every given file names
        s_content = get_text(fname) # Turn each file name into a string content
        lst_word = words(s_content) # Turn the string content into a list of normalized words
        for word in lst_word: # For each normalized words, update the dict by word-file as key-value pairs
            set_IDs = htable_get(table, word)
            if set_IDs == None:
                htable_put(table, word, {idx}) # index or file name
            else:
                set_IDs.add(idx)
    return table

def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    # set_file = set(files)
    # for term in terms:
    #     set_file = set_file.intersection(index[term]) # The set will getting smaller under each loop
    # return list(set_file)


    # set_file = set(files)
    # for term in terms:
    #     if htable_get(index, term) == None: # Edge case
    #         break
    #     else:
    #         set_file = set_file.intersection(htable_get(index, term)) # The set will getting smaller under each loop
    # return list(set_file)

    # the argument index is the self-defined table
    set_file = set(files) # files is a list of file names, not file IDs
    for term in terms:
        if htable_get(index, term) == None: # Edge case
            return []
        # Turn the IDs into file names
        set_IDs = htable_get(index, term)
        lst_fnames_of_the_term = []
        for ID in set_IDs:
            print(ID)
            # Get back the file names by ID, the index of the files (they are ordered in the list)
            lst_fnames_of_the_term.append(files[ID])

        set_file = set_file.intersection(set(lst_fnames_of_the_term)) # The set will getting smaller under each loop

    return list(set_file)


if __name__ == '__main__':
    # # Test: myhtable_create_index()
    # mtable = myhtable_create_index(['/Users/seanlin/data/slate/51/ArticleIP_38825.txt',
    #         '/Users/seanlin/data/slate/50/ArticleIP_27730.txt',
    #         '/Users/seanlin/data/slate/5/Article247_604.txt'])
    # print(htable_buckets_str(mtable))

    # Test: myhtable_index_search()
    mtable = myhtable_create_index(['/Users/seanlin/data/slate/51/ArticleIP_38825.txt',
            '/Users/seanlin/data/slate/50/ArticleIP_27730.txt',
            '/Users/seanlin/data/slate/5/Article247_604.txt',
            '/Users/seanlin/data/slate/5/Article247_605.txt'])
    lst = myhtable_index_search(['/Users/seanlin/data/slate/5/Article247_604.txt'], mtable, ['ronald', 'reagan'])
    print(lst)
