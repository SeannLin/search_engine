import os
import re
import string

"""
put your code below
"""
def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    # return [f for f in os.listdir(root)] #
    # 什麼是 fully-qualified，txt 檔案？
    # EX: root = "~/data/slate"

    # root = root.strip('~')
    # root = '/Users/' + os.getlogin() + root
    # print(root)

    lst_file = []
    for path_name, subdirs, files in os.walk(root):
        for f_name in files:
            lst_file.append(os.path.join(path_name, f_name))
    return lst_file


""" Sample
Read the whole file as a string
"""
def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


""" Sample
EX: given "Reagan Iran", return ['reagan', 'iran']
"""
def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """

    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words



"""
Arguments docs: comes from the result of the function linear_search()
Arguments terms: comes from the user input and then the process of function words()
"""
def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """

    """
    docs = ['/data/slate/51/ArticleIP_38825.txt', '/data/slate/50/ArticleIP_27730.txt']
    terms = ['reagan', 'ronald']
    """

    """ Sample Output
    <html>
        <body>
        <h2>Search results for <b>ronald reagan</b> in 164 files</h2>

            <p><a href="file:///Users/parrt/github/msds692/data/slate/51/ArticleIP_38825.txt">/Users/parrt/github/msds692/data/slate/51/ArticleIP_38825.txt</a><br>
             such barry goldwater and <b>ronald</b> <b>reagan</b> gradually that conservatism has<br><br>

            <p><a href="file:///Users/parrt/github/msds692/data/slate/50/ArticleIP_27730.txt">/Users/parrt/github/msds692/data/slate/50/ArticleIP_27730.txt</a><br>
             united states should pull out unilaterally when <b>ronald</b> <b>reagan</b> saw that had<br><br>

            <p><a href="file:///Users/parrt/github/msds692/data/slate/20/Article247_4335.txt">/Users/parrt/github/msds692/data/slate/20/Article247_4335.txt</a><br>
             will lead any good when <b>ronald</b> <b>reagan</b> introduced similar device his<br><br>
    ...
    </body>
    </html>
    """

    # Structure
    START = "<html>\n<body>\n<h2>Search results for "
    HEADLINE = f"<b>{' '.join([term for term in terms])}</b> in {len(docs)} files</h2>\n\n"
    END = "</body>\n</html>"

    # First search the first line in the file that contains the terms
    s_body = ""
    for doc in docs:

        # print(doc)
        # s_data = get_text(doc) # s_data is whole content of the file as a string
        # s_data = words(s_data)
        # s_data = '\n'.join(s_data)
        # print(s_data)
        # # split by change liine character, then will get each line of words in doc
        # lst_data = s_data.strip().split("\n")


        # split by change liine character, then will get each line of words in doc
        s_data = get_text(doc) # s_data is whole content of the file as a string
        lst_data = s_data.strip().split("\n")
        # print(lst_data)

        for line in lst_data: # "such as Barry Goldwater and Ronald Reagan. Gradually, that conservatism has"
            lst_words_of_line = words(line)
            # print(lst_words_of_line)
            for term in terms:
                # print(term)
                if any([True if term == w else False for w in lst_words_of_line]):

                # if term in line: # Then we find the line in the file that contains the term we are searching
                #     print(term)

                    # Line 1: The directory path
                    line1 = doc
                    # Line 2: the line containing the word
                    line2 = words(line) # Normalize the line as prompt indicates
                    line2 = ' '.join(line2) # Concat list of words into a whole line as line2

                    s_body += '<p><a href="file://'
                    s_body += line1
                    s_body += '">'
                    s_body += line1
                    s_body += "</a><br>\n"
                    s_body += line2
                    s_body += "<br><br>\n\n"
                    # print("YEAH")

                    break # If one line is located, then no need to find another line in this file

    return START + HEADLINE + s_body + END

    # for i in lst_data:
        # if terms[1] in i:
            # print("got cha")


        # print(terms[0] in i)
        # s_header = lst_data[0]
        # data = [elem for idx,elem in enumerate(lst_data) if idx != 0]

        # # Header
        # lst_header = s_header.split(',')
        # html_header = "<tr><th>" + "</th><th>".join(lst_header) + "</th></tr>\n"
        #
        # # Data
        # html_data = ""
        # for row in data:
        #     lst_data = row.split(',')
        #     html_data = html_data + "<tr><td>" + "</td><td>".join(lst_data) + "</td></tr>\n"
        #
        # for doc in docs:
        #     with open(doc) as f:
        #         f.readlines




def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

if __name__ == '__main__':
    # # Test words(text)
    # s = "Reagan Iran"
    # term = words(s)
    # print(term)

    # # Test words(text) 2
    # s = get_text('/data/slate/51/ArticleIP_38825.txt')
    # s = words(s)
    # print(s)


    # # Test filelist()
    # path = "~/data/slate"
    # lst = filelist(path)
    # print(lst)
    # print(len(lst))

    # # Test results(docs, terms)
    # docs = ['/data/slate/51/ArticleIP_38825.txt', '/data/slate/50/ArticleIP_27730.txt']
    # terms = ['reagan', 'ronald']
    # s = results(docs, terms)
    # print(s)


    # docs = ["./HandRHawaii.txt"]
    # with open(docs) as f:
    #     lst = f.readlines()
    #     s = ''.join(lst)
    #     print(s)

    # results(docs, ['TEl'])


    #
    terms = 'missspellinnng'
    print(filelist('/Users/seanlin/data/berlitz1'))
    # for path_name, subdirs, files in os.walk('~/data/berlitz1'):
    #     for f_name in files:
    #         print(f_name)
            # lst_file.append(os.path.join(path_name, f_name))
    # print(words(terms))
