#!/usr/bin/env python3

welcome_message = "Welcome to GitSkilled, a game to help you master Git to the point of automaticity!"

if __name__ == "__main__":
    print(welcome_message)

    answers = {
        "What command do you use to push code to a remote branch?": "git push"
    }

    for question in answers:
        answer = input(question + ": ")
        if answer == answers[question]:
            print("Correct")
        else:
            print("Incorrect, the answer is " + answers[question])