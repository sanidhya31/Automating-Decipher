# row_label[:] = [] ---> code to clear the list as .clear() function doesnt work for py 2.37
# about lambda function


removables = ['.', ')', '}']
Other_Specify = ['Other, please specify:', 'Please Specify', '(Please Specify)', '(please specify)', 'Specify)',
                 'Other (please specify)', '(Please', 'specify', 'Specify']
anchor = ['None', 'none', 'None of the above']


def removeDelimiter(eachline):
    # before - ['1.', 'Google.'] or ['1)', 'Google.']
    # after - ['1', 'Google.'] or ['1', 'Google.']
    if eachline[0][-1] in removables:
        eachline[0] = eachline[0][:-1]
    return eachline


def rowLabelCheck(wholeques):
    row_label = []
    val_rowLabel = None
    OE = None
    exc = None
    first_line = True
    all_numeric = lambda lst: all(item.isdigit() for item in lst)
    all_single_alpha = lambda lst: all(len(item) == 1 and item.isalpha() for item in lst)
    # For example: wholeques = ['Q1 What is your company Name?', '1. Google.', '2. Apple.', '3. Microsoft.', '4. Samsung.', '5. Other.', '99. dk']

    for index, eachline in enumerate(wholeques):
        eachline = eachline.split(' ')

        if first_line:
            first_line = False

        else:
            eachline = removeDelimiter(eachline)
            row_label.append(eachline[0])

    if len(row_label) > 0:
        # sorted row labels
        if row_label == sorted(row_label) and row_label[0] == '1':
            val_rowLabel = 0

        # unsorted rowlabels needs value
        elif all_numeric(row_label) and (
                () or (row_label != sorted(row_label) and row_label[0] == '1') or (row_label[0] != '1') or (
                all(row_label[i] - row_label[i - 1] == 1 for i in range(1, len(row_label))))):
            val_rowLabel = 1

        # aplha row labels
        elif all_single_alpha(row_label):
            val_rowLabel = 2

        # mostly when no row labels provided
        else:
            val_rowLabel = 3

    for i, eachline in enumerate(wholeques):
        eachline = eachline.split(' ')
        if i == 0:
            continue
        else:
            # code for Other specify
            if val_rowLabel in [0, 1, 2]:
                # print("val_rowLabel %s" % val_rowLabel)
                # print (' '.join(eachline[1:]))
                OE = i if (' '.join(eachline[
                                    1:])) in Other_Specify else 0  # if specify found return the line number # if not found return 0
                exc = i if (' '.join(eachline[1:])) in anchor else 0
            else:
                # print("val_rowLabel %s" % val_rowLabel)
                # print (' '.join(eachline).strip())
                OE = i if (' '.join(
                    eachline)) in Other_Specify else 0  # if specify found return the line number # if not found return 0
                exc = i if (' '.join(eachline)) in anchor else 0


    return val_rowLabel, OE, exc
