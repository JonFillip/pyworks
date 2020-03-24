from testing_code.survey_class import AnonymousSurvey

# Define a question, and make a survey.
question = "What programming language did you learn first?"
my_survey = AnonymousSurvey(question)

# Show the question, and store the responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break

    my_survey.store_response(response)

# Show the survey results
print(f"\nThank you to everyone who participated in the survey!")
my_survey.show_result()

