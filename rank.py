from MiscFunctions import removeDelimiter, rowLabelCheck

def ques_rank(wholeques):
    rank_str = ''
    choices = int(wholeques[0].strip("[]"))
    wholeques = wholeques[1:]
    val_rowLabelCheck, val_OE, val_exc = rowLabelCheck(wholeques)

    first_line = True
    counter_for_row_label = 0
    counter_for_choice_label = 0
    # For example: wholeques = ['[question type]','Q1 What is your company Name?', '1. Google.', '2. Apple.', '3. Microsoft.', '4. Samsung.', '5. Other.', '99. dk']
    for eachline in wholeques:
        eachline = eachline.split(' ')
        # ['[cx]'] or # ['[checkbox]']
        # ['Q1', 'What', 'is', 'your', 'company', 'Name?']
        # ['1.', 'Google.']
        # ['2.', 'Apple.']
        # and so on
        eachline = removeDelimiter(
            eachline)  # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        if first_line:  # Radio and title tag
            rank_str = '<select label="{}" \n minRanks="1"\n optional="1"\n shuffle="rows"\n unique="none,cols"\n uses="ranksort_oe.4">\n'.format(eachline[0])
            rank_str += '<title>{}</title>\n'.format(' '.join(eachline[1:]))
            first_line = False
        else:  # all about rows
            counter_for_row_label += 1
            attrs = ('open="1" openSize="25" randomize="0"' if val_OE == counter_for_row_label else '') + (
                'exclusive ="1" randomize="0" ' if val_exc == counter_for_row_label else '')

            if val_rowLabelCheck in [0, 1]:
                rank_str += '<row label="r{}" {}>{}</row>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 2:  # alpha labels found for these rows
                rank_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs,' '.join(eachline[1:]))
            elif val_rowLabelCheck == 3:  # no label found for these rows
                rank_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs,' '.join(eachline))


#--------------------choices-----------------
        while choices != 0:
            choices -=1
            counter_for_choice_label += 1
            rank_str += '<choice label="ch{}" value="{}">{}</choice>\n'.format(counter_for_choice_label, counter_for_choice_label,counter_for_choice_label)


    rank_str += '</select>\n</suspend>\n\n'
    return rank_str

