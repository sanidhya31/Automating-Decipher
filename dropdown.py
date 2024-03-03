from MiscFunctions import removeDelimiter, rowLabelCheck

def ques_dropdown(wholeques):
    dropdown_str=''
    val_rowLabelCheck, val_OE, val_exc = rowLabelCheck(wholeques)
    first_line = True
    counter_for_row_label = 0
    # For example: wholeques = ['Q1 What is your company Name?', '1. Google.', '2. Apple.', '3. Microsoft.', '4. Samsung.', '5. Other.', '99. dk']
    for eachline in wholeques:
        eachline = eachline.split(' ')
        # ['Q1', 'What', 'is', 'your', 'company', 'Name?']
        # ['1.', 'Google.']
        # ['2.', 'Apple.']
        # and so on
        eachline = removeDelimiter(
            eachline)  # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        if first_line:  # Radio and title tag
            dropdown_str = '<select label="{}">\n'.format(eachline[0])
            dropdown_str += '<title>{}</title>\n'.format(' '.join(eachline[1:]))
            first_line = False
        else:  # all about rows
            counter_for_row_label += 1
            attrs = ('open="1" openSize="25" randomize="0"' if val_OE == counter_for_row_label else '') + (
                'exclusive="1" randomize="0"' if val_exc == counter_for_row_label else '')

            if val_rowLabelCheck == 0:  # doesnt require values
                dropdown_str += '<choice label="ch{}" {}>{}</choice>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 1:  # need values
                dropdown_str += '<choice label="ch{}" value="{}" {}>{}</choice>\n'.format(eachline[0], eachline[0], attrs,
                                                                                ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 2:  # alpha labels found for these rows
                dropdown_str += '<choice label="ch{}" {}>{}</choice>\n'.format(counter_for_row_label, attrs,
                                                                     ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 3:  # no label found for these rows
                dropdown_str += '<choice label="ch{}" {}>{}</choice>\n'.format(counter_for_row_label, attrs, ' '.join(eachline))

    dropdown_str += '</select>\n<suspend/>\n\n'
    return dropdown_str