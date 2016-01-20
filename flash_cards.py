import random
import re
import os
import sys

#all console prints/options for east editing
#function name is print followed by function name in which print statement
#occurs

def print_flashcard_loop():
    """printing for App.flash_card_loop"""
    print("~~~~~~~~~~~~~~~~~~")
    print('Welcome to the Flashcard App.')
    print("You can always type 'exit' in console to close app")
    print("type options to access additional features\n")

def print_get_answer():
    print("~~~~~~~~~~~~~~~~~~")
    print("Please enter valid input")
    print("Make sure answers dont contain special characters")
    print("make sure answers arent blank\n")

def print_get_file_from_user():
    print("~~~~~~~~~~~~~~~~~~")
    print('Make sure the file you choose is seperated by commas')
    print('in question/answer format\n')

def print_give_options():
    print("~~~~~~~~~~~~~~~~~~")
    print("OPTIONS:\tCOMMAND")
    print("q/a format: change_format")
    print("change file: change_file")

def print_get_format():
    print("~~~~~~~~~~~~~~~~~~")
    print('FORMAT:')
    print('select by question or answer')
    print('leave blank for default (question format)\n')

def print_make_flashcard_dict():
    print("~~~~~~~~~~~~~~~~~~")
    print("You can either import a file or")
    print("Make a custom set from CLI")
    print("type [file] or [custom]")
    print("leave blank for default [custom]\n")

class App:

    #class variables
    cards_dict = {}

    #generated question/answers, and user guess
    random_question = ''
    random_answer = ''
    flashcard = ''
    get_answer = ''

    #options
    format = ''
    options = False


    def make_flashcard_dict(self):
        """ opens file for reading, splits answer and
        question from each line, adds to cards_dict """

        print_make_flashcard_dict()
        file_or_manual = input()
        if file_or_manual == 'file':
            get_file = User.get_file_from_user(self)

            with open(get_file,'r') as f:
                for line in f:
                    split_lines = line.split(',')
                    question = split_lines[0].strip()
                    answer = split_lines[1].strip()
                    App.cards_dict[question] = answer
        elif file_or_manual == 'manual':
            User.make_custom_dict(self)
        else: #default
            User.make_custom_dict(self)


    def flash_card_loop(self):
        """ Main app loop """

        print_flashcard_loop()
        User.get_format(self)

        while True:
            App.random_question = random.choice(list(App.cards_dict.keys()))
            App.random_answer = App.cards_dict[App.random_question]
            App.set_flashcard(self)

            App.get_answer = User.get_answer(self)

            if App.get_answer == 'options':
                v = User.give_options(self)
            elif not App.get_answer:
                print("Hope you had fun!")
                return False
            else:
                App.give_results(self)


    def give_results(self):
        """ checks if answer was correct or not """
        question = App.random_question

        if App.format == 'q':
            answer = App.random_answer
        if App.format == 'a':
            answer = App.random_question

        if answer.lower() == App.get_answer.lower():
            print('correct!\n')
        else:
            print('not quite! Answer was %s\n' % answer)

    def set_flashcard(self):
        """ sets the side to show(Q or A) when prompting user """
        if App.format == 'a':
            App.flashcard = App.random_answer
        if App.format == 'q':
            App.flashcard = App.random_question


class User:
    def get_answer(self):
        """ grab answer, return if valid, or exit """
        while True:
            answer = input('Question: %s ' % App.flashcard)

            if answer == 'exit':
                return False

            elif answer == 'options':
                return answer

            elif User.validate_answer(answer):
                return answer

            else:
                print_get_answer()
                

    def validate_answer(answer):
        """ check user's answer to check if it's not blank"""
        if not answer:
            return False

        elif answer.isspace():
            return False

        else:
            return True


    def get_file_from_user(self):
        print_get_file_from_user()

        while True:
            selected_file = input("File: ")
            if os.path.exists(selected_file):
                return selected_file
            else:
                print("file doesn't appear to exist")
                print("Please try again\n")


    def get_format(self):
        print_get_format()
        user_format = input()
        if user_format == 'question':
            App.format = 'q'
        elif user_format == 'answer':
            App.format = 'a'
        else:
            App.format = 'q' #default


    def give_options(self):
        print_give_options()
        user_option = input()

        if user_option == 'change_format':
            User.get_format(self)
            App.set_flashcard(self)

        elif user_option == 'change_file':
            App.cards_dict = {}
            App.make_flashcard_dict(self)
            return False

    def make_custom_dict(self):
        """ user creates own flashcard dict """
        print('custom')


class Main:
    """ Main calls the necessary funtions to keep the app running """
    def __init__(self):
        App.make_flashcard_dict(self)
        App.flash_card_loop(self)



if __name__ == '__main__':
    Main()