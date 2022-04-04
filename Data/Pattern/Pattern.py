import re

'''
    re.findall(pattern, to_search)
    re.search(pattern, to_search)
    re.split(pattern, to_search)
    re.sub(pattern, to_search)
    
    []      a set of characters                 [a-m]
    \       a special sequance                  \d
    .       any character except \n             he..o
    ^       line starts with                    ^hello
    $       line ends with                      bye$
    *       zero or more of the previous char   he.*o
    +       one or more of the previous char    he.+o
    ?       zero or more of the previous char   he.?o
    {x}     exactly x of the previous char      hel{2}
    |       either                              hello|bye
    ()      capture and group
    
    \A      string starts with
    \Z      string ends with
    
'''

class Pattern:
    def __init__(self):
        pass

    def test(self):
        txt = "The rain in Spain"
        x = re.search("^The.*Spain$", txt)
        print(x)


