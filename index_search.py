from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """

    dct_index = defaultdict() # Create an empty dict
    for idx,fname in enumerate(files): # Iterate through every given file names
        s_content = get_text(fname) # Turn each file name into a string content
        lst_word = words(s_content) # Turn the string content into a list of normalized words
        for word in lst_word: # For each normalized words, update the dict by word-file as key-value pairs
            if word not in dct_index:
                dct_index[word] = {idx} # If the key doesn't exist, create one
            else:
                dct_index[word].add(idx) # If the key exist, add the file name into the set of the file names under that word

    return dct_index


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    # index is a dictionary, containg words mapping to its file IDs
    set_file = set(files) # files is a list of file names, not file IDs

    for term in terms:

        if term not in index: # Edge case
            # print("!!!!!!")
            return []

        # Turn the IDs into file names
        set_IDs = index[term]
        lst_fnames_of_the_term = []
        for ID in set_IDs:
            # Get back the file names by ID, the index of the files (they are ordered in the list)
            lst_fnames_of_the_term.append(files[ID])

            # for idx,fname in enumerate(files): # Iterate through all the file names
            #     # Get back the file names by ID, the index of the files (they are ordered in the list)
            #     if ID == idx:
            #         lst_fnames_of_the_term.append(fname)

        set_file = set_file.intersection(set(lst_fnames_of_the_term)) # The set will getting smaller under each loop

    # return lst_file_names_result
    return list(set_file)

    # all_in = True
    # lst_qualified = []
    #
    # for idx,file in enumerate(files):
    #
    #     # print(idx, f)
    #     # s = get_text(f) # Use the existing function words()
    #     # for term in terms:
    #     #     if term not in s: # Check if all the terms are contained in the file
    #     #         all_in = False
    #     # if all_in == True: # Then this file is fully-qualified
    #     #     lst_qualified.append(file)
    #     #     print("!!!!!!")
    #     # print(idx, f)
    #
    #     # with open(file) as f:
    #     #     lst = f.readlines()
    #     #     for line in lst:
    #     #         for term in terms:
    #     #             if term not in : # Check if all the terms are contained in the file
    #     #                 all_in = False
    #     #         if all_in == True: # Then this file is fully-qualified
    #     #             lst_qualified.append(file)
    #     #             print("!!!!!!")
    #
    #     if set(terms) == set(words(get_text(file))).intersection(set(terms)):
    #         lst_qualified.append(file)




if __name__ == '__main__':
    dct = create_index(['/Users/seanlin/data/slate/51/ArticleIP_38825.txt',
            '/Users/seanlin/data/slate/50/ArticleIP_27730.txt',
            '/Users/seanlin/data/slate/5/Article247_604.txt'])
    print(len(dct))
