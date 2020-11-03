# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words
# words 又不需要？！search 已經做過了呀


""" EX:
files = ['/data/slate/51/ArticleIP_38825.txt',
        '/data/slate/50/ArticleIP_27730.txt']]
words = ["Reagan", "Ronald"]
"""
def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """


    # path = "~/data/slate"
    # for path_name, subdir, f_name in os.walk(path):
    #     for f in files:
    #         if f in files:
    #             path
    #             p = os.path.join(path_name, f_name) # Can't use "os."
    #             s = get_text(f)
    #             print(s)
    all_in = True
    lst_qualified = []
    for idx,file in enumerate(files):

        # print(idx, f)
        # s = get_text(f) # Use the existing function words()
        # for term in terms:
        #     if term not in s: # Check if all the terms are contained in the file
        #         all_in = False
        # if all_in == True: # Then this file is fully-qualified
        #     lst_qualified.append(file)
        #     print("!!!!!!")
        # print(idx, f)

        # with open(file) as f:
        #     lst = f.readlines()
        #     for line in lst:
        #         for term in terms:
        #             if term not in : # Check if all the terms are contained in the file
        #                 all_in = False
        #         if all_in == True: # Then this file is fully-qualified
        #             lst_qualified.append(file)
        #             print("!!!!!!")

        if set(terms) == set(words(get_text(file))).intersection(set(terms)):
            lst_qualified.append(file)
            # print("!!!!!!")

    return lst_qualified


    # for file in files:
    #     with open(file) as f:
    #         # lst = f.readlines()
    #         # print(lst[0])
    #         s = get_text(f)
    #         print(s)


# result = []
# for doc in docs:
#     with open(doc) as f:
#         lst = f.readlines()
#         s = ''.join(lst)
#         for term in terms:
#             if term in s: # Matched
#                 print("match")
#                 s1 = lst[]
#                 s2 = lst[]
#                 result.append(lst[0])
#                 result.append(lst[1])

if __name__ == '__main__':
    lst = linear_search(['/data/slate/51/ArticleIP_38825.txt',
            '/data/slate/50/ArticleIP_27730.txt',
            '/data/slate/5/Article247_604.txt'], ["reagan", "ronald"])
    # print(lst)
