"""
Survey Project
7/9/19
"""

import json
questions = {
    "name": "What is your name? ",
    "age": "What is your age? ",
    "water": "Did you drink enough water today? (y/n) ",
    "family_size": "How many people are in your family? ",
}


def run_survey():
    user_data = []
    user = "y"
    while user == "y":
        print()
        answer = {}


        for i in questions:
            answerU = input(questions[i])
            if i == "age" or i == "family_size":
                while not answerU.isnumeric():
                    print("That is not a valid number. Try again.\n")
                    answerU = input(questions[i])
            elif i == "water":
                while not (answerU == "y" or answerU == "n"):
                    print("invaild repsonse. Note: answers must be lowercase.\n")
                    answerU = input(questions[i])

            answer[i] = answerU


        user_data.append(answer)

        user = input("Would you like to add another user? (y/n) ").lower()
        while not (user == "y" or user == "n"):
            print("invalid repsonse. try again.\n")
            user = input("Would you like to add another user? (y/n) ").lower()

    return user_data

def save_with_json(filename, user_data):
    with open(filename, 'w') as open_file:
        open_file.write("[\n")

        index = 0
        for i in user_data:
            json.dump(i, open_file)
            if index == (len(user_data) - 1):
                open_file.write("\n")
            else:
                open_file.write(",\n")
            index += 1
        open_file.write("]")
        # use dump() not dumps(), becuase s means string and it will
        #   just turn it into a json string

def main():
    print("_______________SURVEY TIME_______________")
    data = run_survey()
    save_with_json("survey_data.txt", data)

main()
