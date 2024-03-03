from MiscFunctions import removeDelimiter, rowLabelCheck

def multi_grid(wholeques):
    multi_grid_str = ''

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

    val_rowLabelCheck, val_OE, val_exc = rowLabelCheck(array_rest_of_the_question)
    val_colLabelCheck, col_val_OE, col_val_exc = rowLabelCheck(array_cols)
    first_line = True
    counter_for_row_label = 0
    counter_for_col_label = 0

    for eachline in array_rest_of_the_question:
        eachline = eachline.split(' ')

        eachline = removeDelimiter(
            eachline)  # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        if first_line:  # Radio and title tag
            multi_grid_str = '<checkbox atleast="1" label="{}">\n'.format(eachline[0])
            multi_grid_str += '<title>{}</title>\n'.format(' '.join(eachline[1:]))
            first_line = False
        else:  # all about rows
            counter_for_row_label += 1
            attrs = ('open="1" openSize="25" randomize="0" optional="1"' if val_OE == counter_for_row_label else '') + (
                'exclusive="1" randomize="0"' if val_exc == counter_for_row_label else '')

            if val_rowLabelCheck in [0, 1]:
                multi_grid_str += '<row label="r{}" {}>{}</row>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 2:  # alpha labels found for these rows
                multi_grid_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs,
                                                                           ' '.join(eachline[1:]))
            elif val_rowLabelCheck == 3:  # no label found for these rows
                multi_grid_str += '<row label="r{}" {}>{}</row>\n'.format(counter_for_row_label, attrs,
                                                                           ' '.join(eachline))
    multi_grid_str += '\n'

    # --------------------------columns

    for eachline in array_cols:
        eachline = eachline.split(' ')
        # ['1.', 'Google.']
        # ['2.', 'Apple.']
        # and so on
        eachline = removeDelimiter(
            eachline)  # before - ['1.', 'Google.'] or ['1)', 'Google.'] --->  # after - ['1', 'Google.'] or ['1', 'Google.']

        # all about rows
        counter_for_col_label += 1
        attrs = ('open="1" openSize="25" randomize="0"' if col_val_OE == counter_for_col_label else '') + (
            'randomize="0" ' if col_val_exc == counter_for_col_label else '')
        if val_colLabelCheck == 0:  # doesnt require values
            multi_grid_str += '<col label="c{}" {}>{}</col>\n'.format(eachline[0], attrs, ' '.join(eachline[1:]))
        elif val_colLabelCheck == 1:  # need values
            multi_grid_str += '<col label="c{}" value="{}" {}>{}</col>\n'.format(eachline[0], eachline[0], attrs,
                                                                                  ' '.join(eachline[1:]))
        elif val_colLabelCheck == 2:  # alpha labels found for these rows
            multi_grid_str += '<col label="c{}" {}>{}</col>\n'.format(counter_for_col_label, attrs,
                                                                       ' '.join(eachline[1:]))
        elif val_colLabelCheck == 3:  # no label found for these rows
            multi_grid_str += '<col label="c{}" {}>{}</col>\n'.format(counter_for_col_label, attrs, ' '.join(eachline))

    multi_grid_str += '</checkbox>\n<suspend/>\n\n'
    return multi_grid_str
