from quesType import typeOfQues
from preFormat import initial_Format


#Path to the input txt file
input_file_path = 'C:/Users/sanid/Desktop/input.txt'

#Path to the output txt file
output_file_path = 'C:/Users/sanid/Desktop/output.txt'


list_for_grids=['[ssg]', '[SSG]', '[SSGrid]','[SG]','[sg]','[msg]', '[MSG]', '[MSGrid]','[MG]','[mg]']

output_file = open(output_file_path, "w")
output_file.write("")
# Open the file in read mode
with open(input_file_path, 'r') as file:
    paragraphs = file.readlines()


final_str = ''
paragraphs = ''.join(paragraphs).split('\n') #removes the line breaks from the pulled text
paragraphs = initial_Format(paragraphs)

temp_ar=[]
extra_run_for_grid=True
for i,eachpara in enumerate(paragraphs):

    if eachpara.strip() == '' or i==len(paragraphs)-1:
        # eachpara.strip() == '' looks for the double line break which helps in identification of new question
        # this if cond will fetch the text question by question and pass it to typeOfQues
        # and then it clears the list(temp_ar) so it can be used for another question

        if (temp_ar[0] in list_for_grids) and extra_run_for_grid:
            extra_run_for_grid=False
            temp_ar.append('')
            continue


        print(typeOfQues(temp_ar))
        output_file.write(typeOfQues(temp_ar))
        temp_ar=[]
        extra_run_for_grid = True
    else:
        temp_ar.append(eachpara.strip())





