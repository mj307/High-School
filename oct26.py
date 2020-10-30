from __future__ import division
import json
from datetime import datetime
import time

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
    with open('~/grade_calc', 'r') as g:
        dict1 = json.load(g)
    ####
    hw_your_points = 0
    hw_total_points = 0
    for a in dict1['HW']:
        hw_your_points = hw_your_points + a[1]
        hw_total_points = hw_total_points + a[2]
    hw_grade = (hw_your_points/ hw_total_points) * 100
    #####
    quiz_your_points = 0
    quiz_total_points = 0
    for a in dict1['Quiz']:
        quiz_your_points = quiz_your_points + a[1]
        quiz_total_points = quiz_total_points + a[2]
    quiz_grade = (quiz_your_points/ quiz_total_points) * 100
    #####
    test_your_points = 0
    test_total_points = 0
    for a in dict1['Test']:
        test_your_points = test_your_points + a[1]
        test_total_points = test_total_points + a[2]
    test_grade = (test_your_points/ test_total_points) * 100
    total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
    print 'Your overall grade is {}'.format(round(total_grade,2))


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


# This function will let you know your overall grade for a potential quiz score.
# what each variable represents:
# points_received = the number of points you think you earned on the quiz
# possible_points = the total number of points you could have gotten on the quiz
# hw_your_points = the total number of points you have earned from homework
# hw_total_points = the highest possible number of points you could have gotten from homework
# quiz_your_points = the total number of points you have earned from quizzes
# quiz_total_points = the highest possible number of points you could have gotten from quizzes
# test_your_points = the total number of points you have earned from tests
# test_total_points = the highest possible number of points you could have gotten from tests
def ff_quiz(points_received,possible_points):
    with open('~/grade_calc', 'r') as g:
        dict1 = json.load(g)
    ####
    hw_your_points = 0
    hw_total_points = 0
    for a in dict1['HW']:
        hw_your_points = hw_your_points + a[1]
        hw_total_points = hw_total_points + a[2]
    hw_grade = (hw_your_points / hw_total_points) * 100
    #####
    test_your_points = 0
    test_total_points = 0
    for a in dict1['Test']:
        test_your_points = test_your_points + a[1]
        test_total_points = test_total_points + a[2]
    test_grade = (test_your_points / test_total_points) * 100
    ####
    quiz_your_points = 0
    quiz_total_points = 0
    for a in dict1['Quiz']:
        quiz_your_points = quiz_your_points + a[1]
        quiz_total_points = quiz_total_points + a[2]
    quiz_grade = (quiz_your_points / quiz_total_points) * 100
    total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
    print 'This is your current grade: {}'.format(round(total_grade, 2))
    print 'Your hw average is {}, your quiz average is {} and your test average is {}'.format(hw_grade, round(quiz_grade, 2),                                                                                      round(test_grade, 2))
    ####
    quiz_your_points = quiz_your_points + points_received
    quiz_total_points = quiz_total_points + possible_points
    quiz_grade = (quiz_your_points / quiz_total_points) * 100
    total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
    print 'This is your new overall grade: {}'.format(round(total_grade, 2))
    print 'Your new hw average is {}, your new quiz average is {} and your new test average is {}'.format(hw_grade,
                                                                                                    round(quiz_grade,
                                                                                                          2),
                                                                                                    round(test_grade,
                                                                                                          2))


# This function does the same job as the previous function, except it calculates your overall grade for a potential
# test score.
# what each variable represents:
# points_received = the number of points you think you earned on the test
# possible_points = the total number of points you could have gotten on the quiz
# hw_your_points = the total number of points you have earned from homework
# hw_total_points = the highest possible number of points you could have gotten from homework
# quiz_your_points = the total number of points you have earned from quizzes
# quiz_total_points = the highest possible number of points you could have gotten from quizzes
# test_your_points = the total number of points you have earned from tests
# test_total_points = the highest possible number of points you could have gotten from tests
def ff_test(points_received):
    with open('~/grade_calc', 'r') as g:
        dict1 = json.load(g)
    ####
    hw_your_points = 0
    hw_total_points = 0
    for a in dict1['HW']:
        hw_your_points = hw_your_points + a[1]
        hw_total_points = hw_total_points + a[2]
    hw_grade = (hw_your_points / hw_total_points) * 100
    ####
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

    total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
    print 'This is your current grade: {}'.format(round(total_grade, 2))
    print 'Your hw average is {}, your quiz average is {} and your test average is {}'.format(hw_grade, round(quiz_grade, 2),
                                                                                        round(test_grade, 2))
    test_your_points = test_your_points + points_received
    total3 = test_total_points + 100
    test_grade = (test_your_points / total3) * 100
    total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
    print 'This is your new grade: {}'.format(round(total_grade, 2))
    print 'Your new hw average is {}, your new quiz average is {} and your new test average is {}'.format(hw_grade,
                                                                                                    round(quiz_grade,
                                                                                                          2),
                                                                                                    round(test_grade,
                                                                                                          2))


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
def findgradew_quiz(quiz_points,desired_grade):
    with open('~/grade_calc', 'r') as g:
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
    needed_quiz_avg = (desired_grade - (0.6*test_grade) - (0.2*hw_grade))/0.2
    w = needed_quiz_avg/100
    needed_score = w*(quiz_points+quiz_total_points) - quiz_your_points
    if needed_score <= quiz_points:
        print 'You will need to get {} points out of {} to get an overall grade of {}%'.format(needed_score,
                                                                                              quiz_points, desired_grade)
    else:
        quiz_your_points = quiz_your_points+quiz_points
        quiz_total_points = quiz_total_points+quiz_points
        quiz_grade = (quiz_your_points/quiz_total_points)*100
        total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
        print 'You will not be able to get a desired grade of {}% with this quiz, but if you get a full score your ' \
              'grade will be {}%'.format(desired_grade,round(total_grade,2))


# This next function will tell you what score you need to earn on an upcoming test in order to get a grade you want.
# as input, this function will take the desired overall grade you want. All tests are out of 100 points, so we don't
# need to take the number of points as an input.
# what each variable represents:
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
def findgradew_test(desired_grade):
    with open('~/grade_calc', 'r') as g:
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
    #########
    total_grade = (0.6 * test_grade) + (0.2 * quiz_grade) + (0.2 * hw_grade)
    needed_test_avg = (desired_grade - (0.2 * quiz_grade) - (0.2 * hw_grade)) / 0.6
    w = needed_test_avg / 100
    needed_score = w * (100 + test_total_points) - test_your_points
    if needed_score <= 100:
        print 'You will need to get {} points out of 100 to get an overall grade of {}%'.format(round(needed_score, 2),
                                                                                                desired_grade)
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
        with open('~/grade_calc', 'r') as g:
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
                with open('~/grade_calc', 'w+') as g:
                    g.truncate()
                with open('~/grade_calc', 'w+') as g:
                    json.dump(dict_grade_book, g)

            elif v_choice == 2:
                calculate_overall_grade()

            elif v_choice == 3:
                q_or_t = input('Choose 1 for possible grade after quiz and 2 for possible grade after test: ')
                if q_or_t == 1:
                    points_received = input('enter the number points you received: ')
                    possible_points = input('enter the number of points you could have received: ')
                    ff_quiz(points_received,possible_points)
                else:
                    points_received = input('enter the number points you received: ')
                    ff_test(points_received)
            elif v_choice == 4:
                grade_after = input('Enter 1 to find score needed on upcoming quiz to maintain grade or 2 to find score'
                                    'needed on upcoming test to maintain grade: ')
                if grade_after == 1:
                    quiz_points = input('enter the number of points on your upcoming quiz: ')
                    desired_grade = input('enter desired grade: ')
                    findgradew_quiz(quiz_points,desired_grade)
                else:
                    desired_grade = input('enter desired grade: ')
                    findgradew_test(desired_grade)
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

            with open('~/grade_calc', 'w+') as g:
                g.truncate()
            with open('~/grade_calc', 'w+') as g:
                json.dump(dict_grade_book,g)
        else:
            r = 2483




























