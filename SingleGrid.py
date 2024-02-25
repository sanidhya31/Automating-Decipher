# Note:-
# as this function is expecting a grid array I've appended a blank line to segregate between cols and rows
# so it could end throwing error: Index out of range
# get rid of that line break or blank string in this array while calling another function
# needs to be optimized

from MiscFunctions import removeDelimiter, rowLabelCheck

def single_grid(wholeques):
    single_grid_str = ''

    array_rest_of_the_question = []
    array_cols = []
    split_found = False

    for item in wholeques:
        if item == '':
            split_found = True
        elif not split_found:
            array_rest_of_the_question.append(item)
        else:
            array_cols.append(item)

    val_rowLabelCheck,val_OE,val_exc =rowLabelCheck(array_rest_of_the_question)
    val_colLabelCheck, col_val_OE, col_val_exc = rowLabelCheck(array_cols)
    first_line=True
    counter_for_row_label=0
    counter_for_col_label=0

    for eachline in array_rest_of_the_question:
        eachline = eachline.split(' ')

        eachline = removeDelimiter(eachline) # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        if first_line: #Radio and title tag
            single_grid_str = '<radio label="{}">\n'.format(eachline[0])
            single_grid_str += '<title>{}</title>\n'.format(' '.join(eachline[1:]))
            first_line=False
        else: #all about rows
            counter_for_row_label += 1
            attrs = ('open="1" openSize="25" randomize="0" optional="1"' if val_OE == counter_for_row_label else '') + ('randomize="0"' if val_exc == counter_for_row_label else '')

            if val_rowLabelCheck in [0,1]:
                single_grid_str += '<row label="r{}" {}>{}</row>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 2: #alpha labels found for these rows
                single_grid_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 3: #no label found for these rows
                single_grid_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs, ' '.join(eachline))
    single_grid_str += '\n'


    #--------------------------colums

    for eachline in array_cols:
        eachline = eachline.split(' ')
        # ['1.', 'Google.']
        # ['2.', 'Apple.']
        # and so on
        eachline = removeDelimiter(eachline)  # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']


        # all about rows
        counter_for_col_label += 1
        attrs = ('open="1" openSize="25" randomize="0"' if col_val_OE == counter_for_col_label else '') + ('randomize="0" ' if col_val_exc == counter_for_col_label else '')
        if val_colLabelCheck == 0:  # doesnt require values
            single_grid_str += '<col label="c{}" {}>{}</col>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
        elif val_colLabelCheck == 1:  # need values
            single_grid_str += '<col label="c{}" value="{}" {}>{}</col>\n'.format(eachline[0], eachline[0], attrs,
                                                                            ' '.join(eachline[1:]))
        elif val_colLabelCheck == 2:  # alpha labels found for these rows
            single_grid_str += '<col label="c{}" {}>{}</col>\n'.format(counter_for_col_label, attrs,
                                                                 ' '.join(eachline[1:]))
        elif val_colLabelCheck == 3:  # no label found for these rows
            single_grid_str += '<col label="c{}" {}>{}</col>\n'.format(counter_for_col_label, attrs, ' '.join(eachline))

    single_grid_str += '</radio>\n</suspend>\n\n'
    return single_grid_str
