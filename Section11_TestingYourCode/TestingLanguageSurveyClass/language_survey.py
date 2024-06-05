from survey import AnonymousSurvey

# define a question and make a survey
question = "\nWhat language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# show the question and store responses to the question
language_survey.show_question()
print("Enter 'q' at any time to qit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)
    
# show the survey results
print("Thank you to everyone who participated in the survey!")
language_survey.show_results()

