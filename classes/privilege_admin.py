"""This stores the Privilege and Admin classes of the User class"""
from classes.user_admin import *


class Privileges:
    """Write code that defines attributes amd methods for admin privileges."""

    def __init__(self, privileges):
        """Initialize the attribute for Privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the Admin user"""
        print(f"Admin features:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    """Build a child class from User and represent aspects of the User that
    are specific to the Administrator."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the attributes of the parent class. Then add the new
        attributes specific to Admin"""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privilege = Privileges(privileges=[
            "add post",
            "delete post",
            "ban user",
            "edit account settings",
        ])
