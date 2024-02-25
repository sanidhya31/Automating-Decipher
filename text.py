from MiscFunctions import removeDelimiter, rowLabelCheck


def ques_text(wholeques):
    text_str = ''
    val_row_label_check, val_OE, val_exc =rowLabelCheck(wholeques)
    first_line=True
    counter_for_row_label=0
    # For example: wholeques = ['[question type]','Q1 What is your company Name?', '1. Google.', '2. Apple.', '3. Microsoft.', '4. Samsung.', '5. Other.', '99. dk']
    for eachline in wholeques:
        eachline = eachline.split(' ')
        # ['[cx]'] or # ['[checkbox]']
        # ['Q1', 'What', 'is', 'your', 'company', 'Name?']
        # ['1.', 'Google.']
        # ['2.', 'Apple.']
        # and so on
        eachline = removeDelimiter(eachline)
        # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        if first_line:  #Radio and title tag
            text_str = '<text label="{}" size="60" optional="0">\n'.format(eachline[0])
            text_str += '<title>{}</title>\n'.format(' '.join(eachline[1:]))
            first_line=False
        else: #all about rows
            counter_for_row_label += 1
            attrs = ('randomize="0" ' if val_exc == counter_for_row_label else '')

            if val_row_label_check in [0, 1]:
                text_str += '<row label="r{}" {}>{}</row>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
            elif val_row_label_check == 2: #alpha labels found for these rows
                text_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs, ' '.join(eachline[1:]))
            elif val_row_label_check == 3: #no label found for these rows
                text_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs, ' '.join(eachline))

    text_str += '</text>\n</suspend>\n'
    return text_str








