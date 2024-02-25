import sys
from multi import checkbox
from number import ques_number
from textarea import ques_textarea
from text import ques_text
from single import radio
from MultiGrid import multi_grid
from rank import ques_rank
from SingleGrid import single_grid

quesDictionary = {
    "checkbox": ['[ch]', '[c]', '[cx]'],
    "ques_number": ['[num]', '[int]', '[nm]'],
    "ques_textarea": ['[textarea]', '[TA]', '[ta]'],
    "ques_text": ['[text]', '[txt]', '[TXT]'],
    "single_grid": ['[ssg]', '[SSG]', '[SSGrid]','[SG]','[sg]'],
    "multi_grid": ['[msg]', '[MSG]', '[MSGrid]','[MG]','[mg]'],
    "ques_rank": ['[rank]', '[Rank]', '[rk]','[RK]']
}


def typeOfQues(wholeques):
    # For example: wholeques = ['Q1 What is your company Name?', '1. Google.', '2. Apple.', '3. Microsoft.', '4. Samsung.', '5. Other.', '99. dk']
    # fetch the initial for question type
    ques_initials = wholeques[0]

# matching the initial with the data available in dictionary
    for key, value in quesDictionary.items():
        # Check if the initial matches any of the keys
        if ques_initials in value:
            # If a match is found, call the corresponding function
            if key in globals():
                return globals()[key](wholeques[1:])
    #default Case for radio
    return radio(wholeques)
