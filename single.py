from MiscFunctions import removeDelimiter, rowLabelCheck

def radio(wholeques):
    radio_str=''
    val_rowLabelCheck,val_OE,val_exc =rowLabelCheck(wholeques)
    first_line=True
    counter_for_row_label=0
    # For example: wholeques = ['Q1 What is your company Name?', '1. Google.', '2. Apple.', '3. Microsoft.', '4. Samsung.', '5. Other.', '99. dk']
    for eachline in wholeques:
        eachline = eachline.split(' ')
        print (eachline)
        # ['Q1', 'What', 'is', 'your', 'company', 'Name?']
        # ['1.', 'Google.']
        # ['2.', 'Apple.']
        # and so on
        eachline = removeDelimiter(eachline) # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        if first_line: #Radio and title tag
            radio_str = '<radio label="{}">\n'.format(eachline[0])
            radio_str += '<title>{}</title>\n'.format(' '.join(eachline[1:]))
            first_line=False
        else: #all about rows
            counter_for_row_label += 1
            attrs = ('open="1" openSize="25" randomize="0"' if val_OE == counter_for_row_label else '') + ('randomize="0"' if val_exc == counter_for_row_label else '')

            if val_rowLabelCheck == 0: #doesnt require values
                radio_str += '<row label="r{}" {}>{}</row>\n'.format(eachline[0],attrs,' '.join(eachline[1:]))
            elif val_rowLabelCheck == 1: #need values
                radio_str += '<row label="r{}" value="{}" {}>{}</row>\n'.format(eachline[0], eachline[0],attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 2: #alpha labels found for these rows
                radio_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label,attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 3: #no label found for these rows
                radio_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label,attrs, ' '.join(eachline))

    radio_str += '</radio>\n<suspend/>\n\n'
    return radio_str








