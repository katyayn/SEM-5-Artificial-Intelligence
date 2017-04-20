iparens = iter('(){}[]<>')
parens = dict(zip(iparens, iparens))
closing = parens.values()



print("Reading from Katyayn.txt")


file = open("katyayn.txt",'r')

data = []



# COUNTERS_ORIGINAL_TEXT

variable_a_counter_original = 0
variable_b_counter_original = 0
constant_2_counter_original = 0

operator_plus_counter_original = 0
operator_minus_counter_original = 0
operator_multiply_counter_original = 0
operator_divide_counter_original = 0
operator_exponential_counter_original = 0

# COUNTER_GIVEN_TEXT

variable_a_counter_given = 0
variable_b_counter_given = 0
constant_2_counter_given = 0

operator_plus_counter_given = 0
operator_minus_counter_given = 0
operator_multiply_counter_given = 0
operator_divide_counter_given = 0
operator_exponential_counter_given = 0



#GRADES

balanced_bracket_grade=0
same_number_of_operators_grade=0
same_number_of_variable_grade=0
same_number_of_constant_2_grade=0
#reversed_operand_grade=0
exact_string_match_grade=0


#FUNCTIONS


def balanced(work_string):
    stack = []
    for c in work_string:
        d = parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack



def counter_original(work_string):

    change_string=work_string

    for c in range(2,len(change_string)):
        if change_string[c] == 'a':
            global variable_a_counter_original
            variable_a_counter_original += 1
        if change_string[c] == 'b':
            global variable_b_counter_original
            variable_b_counter_original += 1

        if change_string[c] == '2':
            global constant_2_counter_original
            constant_2_counter_original += 1

        if change_string[c] == '+':
            global operator_plus_counter_original
            operator_plus_counter_original += 1
        if change_string[c] == '-':
            global operator_minus_counter_original
            operator_minus_counter_original += 1
        if change_string[c] == '*':
            global operator_multiply_counter_original
            operator_multiply_counter_original += 1
        if change_string[c] == '/':
            global operator_divide_counter_original
            operator_divide_counter_original += 1
        if change_string[c] == '^':
            global operator_exponential_counter_original
            operator_exponential_counter_original += 1




def counter_given(work_string):

    change_string=work_string

    for c in range(0,len(change_string)):
        if change_string[c] == 'a':
            global variable_a_counter_given
            variable_a_counter_given += 1
        if change_string[c] == 'b':
            global variable_b_counter_given
            variable_b_counter_given += 1

        if change_string[c] == '2':
            global constant_2_counter_given
            constant_2_counter_given += 1

        if change_string[c] == '+':
            global operator_plus_counter_given
            operator_plus_counter_given += 1
        if change_string[c] == '-':
            global operator_minus_counter_given
            operator_minus_counter_given += 1
        if change_string[c] == '*':
            global operator_multiply_counter_given
            operator_multiply_counter_given += 1
        if change_string[c] == '/':
            global operator_divide_counter_given
            operator_divide_counter_given += 1
        if change_string[c] == '^':
            global operator_exponential_counter_given
            operator_exponential_counter_given += 1




def print_original_counter_values():
    print("variable_a_counter_original              :\t", variable_a_counter_original)
    print("variable_b_counter_original              :\t", variable_b_counter_original)
    print("constant_2_counter_original              :\t", constant_2_counter_original)
    print("operator_plus_counter_original           :\t", operator_plus_counter_original)
    print("operator_minus_counter_original          :\t", operator_minus_counter_original)
    print("operator_multiply_counter_original       :\t", operator_multiply_counter_original)
    print("operator_divide_counter_original         :\t", operator_divide_counter_original)
    print("operator_exponential_counter_original    :\t", operator_exponential_counter_original)


def print_given_counter_values():
    print("variable_a_counter_given                 :\t", variable_a_counter_given)
    print("variable_b_counter_given                 :\t", variable_b_counter_given)
    print("constant_2_counter_given                 :\t", constant_2_counter_given)
    print("operator_plus_counter_given              :\t", operator_plus_counter_given)
    print("operator_minus_counter_given             :\t", operator_minus_counter_given)
    print("operator_multiply_counter_given          :\t", operator_multiply_counter_given)
    print("operator_divide_counter_given            :\t", operator_divide_counter_given)
    print("operator_exponential_counter_given       :\t", operator_exponential_counter_given)


def calculate_variable_grade():
    difference_a = variable_a_counter_original-variable_a_counter_given
    if (difference_a<0):
        difference_a *= -1

    difference_b = variable_b_counter_original-variable_b_counter_given
    if (difference_b < 0):
        difference_b *= -1

    total_a = variable_a_counter_original+variable_a_counter_given
    total_b = variable_b_counter_original + variable_b_counter_given

    grade_variable_a = 10
    grade_variable_b = 10

    if(total_a > 0):
        grade_variable_a = float(10 - (difference_a * 10 / total_a))

    if (total_b > 0):
        grade_variable_b = float(10 - (difference_b * 10 / total_b))

    return float((grade_variable_a+grade_variable_b)/2)



def calculate_operator_grade():
    difference_plus = operator_plus_counter_original-operator_plus_counter_given
    if(difference_plus<0):
        difference_plus *= -1

    difference_minus = operator_minus_counter_original-operator_minus_counter_given
    if(difference_minus<0):
        difference_minus *= -1

    difference_multiply = operator_multiply_counter_original - operator_multiply_counter_given
    if (difference_multiply < 0):
        difference_multiply *= -1

    difference_divide = operator_divide_counter_original - operator_divide_counter_given
    if (difference_divide < 0):
        difference_divide *= -1

    difference_exponential = operator_exponential_counter_original - operator_exponential_counter_given
    if (difference_exponential < 0):
        difference_exponential *= -1

    total_plus = operator_plus_counter_original+operator_plus_counter_given
    total_minus = operator_minus_counter_original+operator_minus_counter_given
    total_multiply = operator_multiply_counter_original + operator_multiply_counter_given
    total_divide = operator_divide_counter_original - operator_divide_counter_given
    total_exponential = operator_exponential_counter_original - operator_exponential_counter_given

    grade_operator_plus = 10
    grade_operator_minus = 10
    grade_operator_multiply = 10
    grade_operator_divide = 10
    grade_operator_exponential = 10

    if (total_plus > 0):
        grade_operator_plus = float(10-(difference_plus*10/total_plus))

    if (total_minus > 0):
        grade_operator_minus = float(10-(difference_minus*10/total_minus))

    if (total_multiply > 0):
        grade_operator_multiply = float(10-(difference_multiply*10/total_multiply))

    if (total_divide > 0):
        grade_operator_divide = float(10-(difference_divide*10/total_divide))

    if (total_exponential > 0):
        grade_operator_exponential = float(10-(difference_exponential*10/total_exponential))

    return float((grade_operator_plus+grade_operator_minus+grade_operator_multiply+grade_operator_divide+grade_operator_exponential)/5)



def calculate_constant_2_grade():
    difference_constant_2 = constant_2_counter_original-constant_2_counter_given
    if (difference_constant_2<0):
        difference_constant_2 *= -1

    total_constant_2=constant_2_counter_original+constant_2_counter_given

    grade_constant_2 = 10

    if(total_constant_2 > 0):
        grade_constant_2 = float(10-(difference_constant_2*10/total_constant_2))

    return  float(grade_constant_2)


"""
def check_reversed_operand(original_string,given_string):

    o=0
    front_original=[]
    back_original=[]
    check_string=[]

    for i in range(2,len(original_string)):
        if(original_string[i] == '-' or original_string[i] == '/' or original_string[i] == '^'):

            print("\n\nFound : ",original_string[i],"\n\n")

            j=i
            while(original_string[j+1]!='('):
                front_original.append=original_string[j]
                j-=1
                o+=1

            print("\n\nThe Front Original is :", front_original)

            j=i
            o=0
            while(original_string[j-1]!=')'):
                back_original.append=original_string[j]
                j+=1
                o+=1

            o=0

            print("\n\nThe Back Original is :", back_original)

            for k in range(0,len(given_string)):

                if(front_original[0]==given_string[k]):
                    if(given_string[k+len(front_original)]==original_string[i]):
                        for l in range(k,len(front_original)):
                            check_string.append=given_string[l]
                            o+=1
                        if(front_original==check_string):
                            o=0
                            for l in range(k+len(front_original),k+len(front_original)+len(back_original)):
                                check_string.append=given_string[l]
                                o+=1
                            if(back_original==check_string):
                                global reversed_operand_grade
                                reversed_operand_grade=10






"""



for line in file:
    data.append(line.strip().split()) #data now contains the contents of katyayn.txt in 2-D array data[i][0]

answer_number = int(input("\n\nEnter the answer number(1to5):\t"))
answer_given = input("\n\nEnter your answer:\t")

for i in range(0,answer_number):

    content_in_data = data[i][0]

    if ord(content_in_data[0])-48 == answer_number:

        # COUNTERS_ORIGINAL_TEXT

        variable_a_counter_original = 0
        variable_b_counter_original = 0
        constant_2_counter_original = 0

        operator_plus_counter_original = 0
        operator_minus_counter_original = 0
        operator_multiply_counter_original = 0
        operator_divide_counter_original = 0
        operator_exponential_counter_original = 0

        # COUNTER_GIVEN_TEXT

        variable_a_counter_given = 0
        variable_b_counter_given = 0
        constant_2_counter_given = 0

        operator_plus_counter_given = 0
        operator_minus_counter_given = 0
        operator_multiply_counter_given = 0
        operator_divide_counter_given = 0
        operator_exponential_counter_given = 0

        flag=0

        if balanced(answer_given)==True:
            print("The Brackets are balanced in the answer given")
            balanced_bracket_grade = 10
        else:
            print("The Brackets are NOT balanced in the answer given")
            balanced_bracket_grade = 0



        counter_original(content_in_data)
        print_original_counter_values()

        counter_given(answer_given)
        print_given_counter_values()

        same_number_of_operators_grade = calculate_operator_grade()
        same_number_of_variable_grade = calculate_variable_grade()
        same_number_of_constant_2_grade = calculate_constant_2_grade()
        #check_reversed_operand(content_in_data,answer_given)

        tentative_grade=0

        print("Balanced Bracket Grade:\t", balanced_bracket_grade)
        print("Same variable Grade:\t", same_number_of_variable_grade)
        print("Same constant Grade:\t", same_number_of_constant_2_grade)
        print("Same operator Grade:\t", same_number_of_operators_grade)
        #print("Reversed operand Grade", reversed_operand_grade)
        float(tentative_grade)

        tentative_grade= float((same_number_of_constant_2_grade+same_number_of_operators_grade+same_number_of_variable_grade+balanced_bracket_grade)/4)

        print("\n\nThe Tentative Grade of Numerical similarity is:\t ", tentative_grade)

        copy_content_in_data=content_in_data
        copy_answer_given=answer_given

        for i in range(0,len(copy_answer_given)):
            if(content_in_data[i+2]==answer_given[i]):
                flag=1
                #exact_string_match_grade=10
            else:
                #exact_string_match_grade=0
                flag=0
                break

        if(flag):
            exact_string_match_grade = 10


        else:
            exact_string_match_grade=0


        print("Exact String Match grade:\t",exact_string_match_grade)

        final_grade=float(((4*tentative_grade)+exact_string_match_grade)/5)

        print("Final Grade", final_grade)



