class AnonymousSurvey:
    """Survey and collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Initiate attribute question. Store a question, and prepare to store
        responses in a list"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Display the question to the users."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Display all the result of the poll."""
        print("Survey results:")
        for response in self.responses:
            print(f"\t- {response.title()}")
