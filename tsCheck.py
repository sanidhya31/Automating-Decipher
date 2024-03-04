list_term = [['[term]', '[Term]', '[Terminate]']]
list_shuffle = [['[shuffle]', '[randomize]', '[Randomize]']]


def check_for_term_and_shuffle(wholeques):
    first_line_here = True
    for index, eachline in enumerate(wholeques):
        print(eachline)
        eachline = eachline.split(' ')
        print (eachline)

        if first_line_here:
            first_line_here = False

        else:
            pass