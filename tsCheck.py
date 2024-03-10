list_term = ['[term]', '[Term]', '[Terminate]', '[TERMINATE]']
list_shuffle = ['[shuffle]', '[randomize]', '[Randomize]']


def check_for_term_and_shuffle(eachline):
    final_str=[]
    is_term = False
    for i in eachline:
        i=i.strip()
        # check for square brackets
        if i[0] == '[' and i[-1] == ']':
            if i in list_term: #check for term
                is_term=True
            elif i in list_shuffle: #check for shuffle
                pass #pass for now
        # to remover square bracket text
        else:
            final_str.append(i)

    return final_str,is_term