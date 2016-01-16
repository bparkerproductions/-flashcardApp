import random
import re
import os

class Data:
    """ To store the apps data """
    cards_dict = {}
    user_file = ''


class App:
    def make_flashcard_dict(self):
        """ opens file for reading, splits answer and
        question from each line, adds to cards_dict """

        #get_file = User.get_file_from_user(self)


        with open('some_file.txt','r') as f:
            for line in f:
                split_lines = line.split(',')
                question = split_lines[0].strip()
                answer = split_lines[1].strip()
                Data.cards_dict[question] = answer
        #print(Data.cards_dict)



    def flash_card_loop(self):
        """ Main app loop """
        
        print('Welcome to the Flashcard App.')
        print("You can always type 'exit' in console to close app")

        while True:

            random_question = random.choice(list(Data.cards_dict.keys()))
            get_answer = User.get_answer(self, random_question)

            if not get_answer:
                print("Hope you had fun!")
                return False
            
            App.give_results(self,random_question, get_answer)

    def give_results(self, question, user_answer):
        """ checks if answer was correct or not """
        answer = Data.cards_dict[question]  
        if answer == user_answer:
            print('correct!')
        else:
            print('not quite! Answer was %s' % answer)



class User:
    def get_answer(self, user_question):
        """ grab answer, return if valid, or exit """
        while True:
            answer = input('Question: %s ' % user_question)
            if answer == 'exit':
                return False
            elif User.validate_answer(answer):
                return answer
            else:
                print("Please enter valid input")
                print("Make sure answers dont contain special characters")
                print("make sure answers arent blank")
                


    def validate_answer(answer):
        """ check user's answer to check if it's not blank"""
        if not answer:
            return False

        elif answer.isspace():
            return False

        else:
            return True

    def get_file_from_user(self):
        print('Make sure the file you choose is seperated by commas')
        print('in question/answer format')

        while True:
            selected_file = input('To get started, choose a file\n')
            if os.path.exists(selected_file):
                return selected_file
            else:
                print("file doesn't appear to exist")
                print("Please try again")



class Main:
    """ Main calls the necessary funtions to keep the app running """
    def __init__(self):
        App.make_flashcard_dict(self)
        App.flash_card_loop(self)



if __name__ == '__main__':
    Main()