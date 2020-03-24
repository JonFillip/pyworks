class Employee:
    """Accept and evaluate an employee salary raise system."""
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the attributes first_name, last_name, annual_salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.responses = []

    def prompt_info(self):
        """Prompt the employee for the first and last names and their annual
        salary """
        print(self.first_name)
        print(self.last_name)
        print(self.annual_salary)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def give_raise(self, amount=5000):
        """Raise the annual salary of the employee by $5000 or any value"""
        self.annual_salary += amount
