from __future__ import division
import json
from datetime import datetime
import time

# total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)


# This function will find your overall grade based on the grades in the grade book.
# This calculates the averages of each category(Homework = worth 20% of grade, Quizzes = worth 20% of grade, and
# Tests = worth 60% of grade)
# what each variable represents:
# hw_your_points = the total number of points you have earned from homework
# hw_total_points = the highest possible number of points you could have gotten from homework
# quiz_your_points = the total number of points you have earned from quizzes
# quiz_total_points = the highest possible number of points you could have gotten from quizzes
# test_your_points = the total number of points you have earned from tests
# test_total_points = the highest possible number of points you could have gotten from tests
def calculate_overall_grade():
    d_store_grade_info = {}
    with open('~/grade_calc.json', 'r') as g:
        dict1 = json.load(g)
    ####
    hw_list = []
    hw_your_points = 0
    hw_total_points = 0
    if dict1.has_key('HW'):
        for a in dict1['HW']:
            hw_your_points = hw_your_points + a[1]
            hw_total_points = hw_total_points + a[2]
    hw_list.append(hw_your_points)
    hw_list.append(hw_total_points)
    #####
    quiz_list = []
    quiz_your_points = 0
    quiz_total_points = 0
    if dict1.has_key('Quiz'):
        for a in dict1['Quiz']:
            quiz_your_points = quiz_your_points + a[1]
            quiz_total_points = quiz_total_points + a[2]
    quiz_list.append(quiz_your_points)
    quiz_list.append(quiz_total_points)
    #####
    test_list = []
    test_your_points = 0
    test_total_points = 0
    if dict1.has_key('Test'):
        for a in dict1['Test']:
            test_your_points = test_your_points + a[1]
            test_total_points = test_total_points + a[2]
    test_list.append(test_your_points)
    test_list.append(test_total_points)
    ###
    d_store_grade_info['HW'] = hw_list
    d_store_grade_info['Quiz'] = quiz_list
    d_store_grade_info['Test'] = test_list
    return d_store_grade_info


# This function lets you input potential grades into your grade book in order to find your potential overall grade
# Each variable represents:
# d_possible_sum = dictionary is which we will temporarily store all of our possible assignment scores(the key is what
# category the assignment falls under and the value is a list. inside of the list, the 1st item is the amount of points
# the user has earned on the assignment and the 2nd item is the total amount of points user could have received on the
# assignment
# d_grade = dictionary which stores all of the points you have earned for the assignment that is already in the grade
# book(the key is the category which the assignment falls under and the value is a list - the first item in the list
# is the sum of all of the points you received for every assignment in that category while the second value in the list
# is the sum of all of the possible points you could received for an assignment within that same category
# test_your_points = sum of all of the potential points you have gotten on tests
# test_total_points = sum of the possible points you could have received on potential tests
# quiz_your_points = sum of all of the potential points you have gotten on quizzes
# quiz_total_points = sum of all the possible points you could have received on potential quizzes
# hw_your_points = sum of all of the potential points you have gotten on homework
# hw_total_points = sum of all the possible points you could have received on potential quizzes
# current_grade = your overall grade with items in the grade book
# hw_grade = hw average
# quiz_grade = quiz average
# test_grade = test average
# total_grade = total overall potential grade
def possible_grade(d_possible_sum):
    d_grade = calculate_overall_grade()
    # this will do calculations for potential grade book items
    test_your_points = 0
    test_total_points = 0
    if d_possible_sum.has_key('Test'):
        for a in d_possible_sum['Test']:
            test_your_points = test_your_points + a[0]
            test_total_points = test_total_points + a[1]
    quiz_your_points = 0
    quiz_total_points = 0
    if d_possible_sum.has_key('Quiz'):
        for a in d_possible_sum['Quiz']:
            quiz_your_points = quiz_your_points + a[0]
            quiz_total_points = quiz_total_points + a[1]
    hw_your_points = 0
    hw_total_points = 0
    if d_possible_sum.has_key('HW'):
        for a in d_possible_sum['HW']:
            hw_your_points = hw_your_points + a[0]
            hw_total_points = hw_total_points + a[1]
    ###########
    current_grade = 0.6*((d_grade['Test'][0]/d_grade['Test'][1])*100)+0.2*((d_grade['Quiz'][0]/d_grade['Quiz'][1])*100)+\
                    0.2*((d_grade['HW'][0]/d_grade['HW'][1])*100)
    print '~'*20
    print 'YOUR CURRENT OVERALL GRADE IS {}%'.format(round(current_grade, 2))
    print '-'*20
    print 'Your current test average is {}%, ' \
          'your quiz average is {}%, and your HW average is {}'.\
        format(round((d_grade['Test'][0]/d_grade['Test'][1])*100,2),
               round((d_grade['Quiz'][0]/d_grade['Quiz'][1])*100,2),round((d_grade['HW'][0]/d_grade['HW'][1])*100,2))
    print '~'*20
    # this part takes values from the actual grade book
    test_your_points= d_grade['Test'][0] + test_your_points
    test_total_points = d_grade['Test'][1] + test_total_points
    quiz_your_points = d_grade['Quiz'][0] + quiz_your_points
    quiz_total_points = d_grade['Quiz'][1] + quiz_total_points
    hw_your_points = hw_your_points + d_grade['HW'][0]
    hw_total_points = hw_total_points + d_grade['HW'][1]
    hw_grade = (hw_your_points/hw_total_points)*100
    quiz_grade = (quiz_your_points/quiz_total_points)*100
    test_grade = (test_your_points/test_total_points)*100
    total_grade = (0.2*hw_grade)+(0.2*quiz_grade)+(0.6*test_grade)
    print 'YOUR POTENTIAL OVERALL GRADE WILL BE {}%'.format(round(total_grade,2))
    print '-'*20
    print 'Your potential test average will be {}%, ' \
          'your potential quiz average will be {}% and your potential ' \
          'hw average will be {}%'.format(round(test_grade,2),round(quiz_grade, 2),round(hw_grade, 2))
    print '~'*20




# This function will allow you to input your grades into the grade book. As input, it takes in the category the grade is
# in (Hw, Quizzes, Tests), the score you received on that assignment, the total score you could have received on
# the assignment, and the dictionary in which all of the grade book items are stored in.
# what each variable represents:
# category = what category the assignment falls under --- each category is assigned to a number so the user doesn't need
#            to type the entire category name
# your_score = what score you received on assignment
# total_score = highest score you could have received(in terms of points)
# ex: Homework assignment worth 10 points and you received 9 points on it. For category you would choose the hw category
# (which corresponds to number 1), your_score = 9, and the total_points = 10. You do not need to worry about the
# dictionary
# list_info_category = an empty list that will take in data -- if our giant dictionary doesn't have
# a key for a specific category, then we will set our data list to empty. This way we can add data to list and then
# create a key for this category and add this list as the value. This also works for assigning a specific value of a
# key to a list
# individual_assignment_data = this is a list for saving data about an individual assignment,like the what day you
# inputted the data in the grade book, the assignment score you received and the highest possible score one could
# receive
# dict_gradebook = dictionary of all of your assignments from every category
def save_assignment_details(category,your_score,total_score,dict_gradebook):
    individual_assignment_data = []
    date = datetime.strftime(datetime.today(), '%m/%d/%Y')
    individual_assignment_data.append(date)
    individual_assignment_data.append(your_score)
    individual_assignment_data.append(total_score)
    if category == 1:
        if dict_gradebook.has_key('HW'):
            list_info_category = dict_gradebook['HW']
            list_info_category.append(individual_assignment_data)
            dict_gradebook['HW'] = list_info_category
        else:
            list_info_category = []
            list_info_category.append(individual_assignment_data)
            dict_gradebook['HW'] = list_info_category
    if category == 2:
        if dict_gradebook.has_key('Quiz'):
            list_info_category = dict_gradebook['Quiz']
            list_info_category.append(individual_assignment_data)
            dict_gradebook['Quiz'] = list_info_category
        else:
            list_info_category = []
            list_info_category.append(individual_assignment_data)
            dict_gradebook['Quiz'] = list_info_category
    if category == 3:
        if dict_gradebook.has_key('Test'):
            list_info_category = dict_gradebook['Test']
            list_info_category.append(individual_assignment_data)
            dict_gradebook['Test'] = list_info_category
        else:
            list_info_category = []
            list_info_category.append(individual_assignment_data)
            dict_gradebook['Test'] = list_info_category




# this next function will tell you what score you need to earn on an upcoming quiz in order to get a grade you want.
# as input, this function will take in the total number of points on your upcoming quiz and the desired overall grade
# you want.
# what each variable represents:
# quiz_points = total number of points on your upcoming quiz
# desired_grade = desired grade after quiz
# hw_your_points = the total number of points you have earned from homework
# hw_total_points = the highest possible number of points you could have gotten from homework
# quiz_your_points = the total number of points you have earned from quizzes
# quiz_total_points = the highest possible number of points you could have gotten from quizzes
# test_your_points = the total number of points you have earned from tests
# test_total_points = the highest possible number of points you could have gotten from tests
# hw_grade = hw average
# quiz_grade = quiz average
# test_grade = test average
def find_grade4_desiredoverall(category,points,desired_grade):
    with open('~/grade_calc.json', 'r') as g:
        dict1 = json.load(g)
    hw_your_points = 0
    hw_total_points = 0
    for a in dict1['HW']:
        hw_your_points = hw_your_points + a[1]
        hw_total_points = hw_total_points + a[2]
    hw_grade = (hw_your_points / hw_total_points) * 100
    #####
    quiz_your_points = 0
    quiz_total_points = 0
    for a in dict1['Quiz']:
        quiz_your_points = quiz_your_points + a[1]
        quiz_total_points = quiz_total_points + a[2]
    quiz_grade = (quiz_your_points / quiz_total_points) * 100
    #####
    test_your_points = 0
    test_total_points = 0
    for a in dict1['Test']:
        test_your_points = test_your_points + a[1]
        test_total_points = test_total_points + a[2]
    test_grade = (test_your_points / test_total_points) * 100
    #################################################
    if category == 'Quiz':
        needed_quiz_avg = (desired_grade - (0.6 * test_grade) - (0.2 * hw_grade)) / 0.2
        w = needed_quiz_avg / 100
        needed_score = w * (points + quiz_total_points) - quiz_your_points
        if needed_score <= quiz_points:
            print 'You will need to get {} points out of {} to get an overall grade of {}%'.format(needed_score,
                                                                                                   quiz_points,
                                                                                                desired_grade)
        else:
            quiz_your_points = quiz_your_points + quiz_points
            quiz_total_points = quiz_total_points + quiz_points
            quiz_grade = (quiz_your_points / quiz_total_points) * 100
            total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
            print 'You will not be able to get a desired grade of {}% with this quiz, but if you get a full score your ' \
                  'grade will be {}%'.format(desired_grade, round(total_grade, 2))
    ###############################################
    if category == 'Test':
        total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
        needed_test_avg = (desired_grade - (0.2 * quiz_grade) - (0.2 * hw_grade)) / 0.6
        w = needed_test_avg / 100
        needed_score = w * (100 + test_total_points) - test_your_points
        if needed_score <= 100:
            print 'You will need to get {} points out of 100 to get an overall grade of {}%'.format(
                round(needed_score, 2), desired_grade)
        else:
            test_your_points = test_your_points + 100
            test_total_points = test_total_points + 100
            test_grade = (test_your_points / test_total_points) * 100
            total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
            print 'You will not be able to get a desired overall grade of {}% with this test, but if you get a full score on your ' \
                  'test, your ' \
                  'grade will be {}%'.format(desired_grade, round(total_grade, 2))














# this is the final combination of all of these functions to create a complete program

r = 1
iter = 1
while r == 1:
    try:
        with open('~/grade_calc.json', 'r') as g:
            dict_grade_book = json.load(g)
        list_choice = ['1-Input Assignment','2-Calculate Current Grade','3-Find Possible Grade',
                           '4-Find Assignment Score Needed For Desired Grade','5-Quit']
        time.sleep(1)
        for a in list_choice:
            print a
        v_choice = input('enter a number from the choices above: ')
        if v_choice == 1:
            print '1 - HW'
            print '2 - Quiz'
            print '3 - Test'
            v_category = input('enter the number for the category you would like to enter an assignment into: ')
            your_score = input('what did you get: ')
            total_score = input('what is the most you could have gotten?: ')
            save_assignment_details(v_category,your_score,total_score,dict_grade_book)
            with open('~/grade_calc.json', 'w+') as g:
                g.truncate()
            with open('~/grade_calc.json', 'w+') as g:
                json.dump(dict_grade_book, g)
        elif v_choice == 2:
            d_grade = calculate_overall_grade()
            test_grade = 0
            quiz_grade = 0
            hw_grade = 0
            if d_grade.has_key('Test'):
                if d_grade['Test'][1] == 0:
                    test_grade = 0
                else:
                    test_grade = 60*(d_grade['Test'][0]/d_grade['Test'][1])
            if d_grade.has_key('Quiz'):
                if d_grade['Quiz'][1] == 0:
                    quiz_grade = 0
                else:
                    quiz_grade = 20*(d_grade['Quiz'][0]/d_grade['Quiz'][1])
            if d_grade.has_key('HW'):
                if d_grade['HW'][1] == 0:
                    hw_grade = 0
                else:
                    hw_grade = 20*(d_grade['HW'][0]/d_grade['HW'][1])
            total_grade = test_grade + quiz_grade + hw_grade
            print 'Your current grade is {}%'.format(round(total_grade,2))


        elif v_choice == 3:
            m = 0
            d_possible_sum = {}
            while m == 0:
                category = input('enter 1 to enter score for quiz, 2 for test, 3 for HW, and 4 to quit: ')
                l_points = []
                if category == 1:
                    worth = input('how many points was this quiz worth: ')
                    points_earned = input('how many points did you receive: ')
                    l_points.append(points_earned)
                    l_points.append(worth)
                    if d_possible_sum.has_key('Quiz'):
                        list_quiz = d_possible_sum['Quiz']
                        list_quiz.append(l_points)
                        d_possible_sum['Quiz'] = list_quiz
                    else:
                        list1_quiz = []
                        list1_quiz.append(l_points)
                        d_possible_sum['Quiz'] = list1_quiz
                    possible_grade(d_possible_sum)
                ####
                elif category == 2:
                    worth = input('how many points was this test worth: ')
                    points_earned = input('how many points did you receive: ')
                    l_points.append(points_earned)
                    l_points.append(worth)
                    if d_possible_sum.has_key('Test'):
                        list_test = d_possible_sum['Test']
                        list_test.append(l_points)
                        d_possible_sum['Test'] = list_test
                    else:
                        list1_test = []
                        list1_test.append(l_points)
                        d_possible_sum['Test'] = list1_test
                    possible_grade(d_possible_sum)
                ####
                elif category == 3:
                    worth = input('how many points was this HW assignment worth: ')
                    points_earned = input('how many points did you receive: ')
                    l_points.append(points_earned)
                    l_points.append(worth)
                    if d_possible_sum.has_key('HW'):
                        list_hw = d_possible_sum['HW']
                        list_hw.append(l_points)
                        d_possible_sum['HW'] = list_hw
                    else:
                        list1_hw = []
                        list1_hw.append(l_points)
                        d_possible_sum['HW'] = list1_hw
                    possible_grade(d_possible_sum)
                else:
                    #possible_grade(d_possible_sum)
                    d_possible_sum = {}
                    m = 38294

        elif v_choice == 4:
            grade_after = input('Enter 1 to find score needed on upcoming quiz to maintain grade or 2 to find score'
                                ' needed on upcoming test to maintain grade: ')
            if grade_after == 1:
                quiz_points = input('enter the number of points on your upcoming quiz: ')
                desired_grade = input('enter desired overall grade(no percentage symbol included): ')
                find_grade4_desiredoverall('Quiz',quiz_points,desired_grade)
                #findgradew_quiz(quiz_points,desired_grade)
            else:
                desired_grade = input('enter desired overall grade(no percentage symbol included): ')
                find_grade4_desiredoverall('Test',100,desired_grade)
                #findgradew_test(desired_grade)
        else:
            r = 300

    except:
        dict_grade_book = {}
        iter = iter + 40
        v_choice = raw_input('Enter I to input assignment or Q to quit: ')
        if v_choice.upper() == 'I':
            print '1 - HW'
            print '2 - Quiz'
            print '3 - Test'
            list1 = []
            v_category = input('enter the number for the category you would like to enter an assignment into: ')
            your_score = input('what did you get: ')
            total_score = input('what is the most you could have gotten?: ')
            save_assignment_details(v_category,your_score,total_score,dict_grade_book)

            with open('~/grade_calc.json', 'w+') as g:
                g.truncate()
            with open('~/grade_calc.json', 'w+') as g:
                json.dump(dict_grade_book,g)
        else:
            r = 2483




























