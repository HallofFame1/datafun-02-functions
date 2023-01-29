# """
# Helen Hammond,January 24, 2023, Module 2-Functions and Statistics

# """
# import datetime
# from enum import Enum


# class Species(Enum):
#     MAN = 1
#     LADY = 2
#     ELF = 3
#     ORC = 4


# class PyBuddy:
#     """ PyBuddy class for creating a study buddy."""

#     def __init__(self, name, species, num_legs, weight_kgs, country, is_available, skill_list):
#         """ Built-in method to create a new instance."""
#         self.name = name
#         self.species = species
#         self.num_legs = num_legs
#         self.weight_kgs = weight_kgs
#         self.country=country
#         self.is_available = is_available
#         self.skill_list = skill_list
#         self.create_date = datetime.datetime.now()

#     def __str__(self):
#         """Built-in method to return a string describing this instance"""
#         s0 = f"I'm {self.name}.\n"
#         s1 = f"I'm a {self.species} with {self.num_legs} legs.\n"
#         s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
#         s3 = f"I've been alive for {self.get_age_string()}.\n"

#         if self.is_available:
#             s4 = "I'm available for tutoring.\n"
#         else:
#             s4 = "I'm already helping others learn Python.\n"

#         s5 = "I know:\n"

#         s6 = ""
#         for skill in self.skill_list:
#             s6 = s6 + f"  - {skill}\n"

#         s = s0 + s1 + s2 + s3 + s4 + s5 + s6
#         return s

#     def get_age_string(self):
#         """Return the age as a string."""
#         start = self.create_date
#         end = datetime.datetime.now()
#         duration = end - start
#         ageString = str(duration)
#         return ageString

#     def display_welcome(self):
#         print()
#         print("Welcome, I'm Helen and I'm good in python.\n")
#         # print using our built-in to string method
#         print(self.__str__())

#         final_message = """

#         You'll need curiousity, the ability to search the web,
#         and the tenacity and resourcefulness
#         to solve all kinds of challenges.

#         Let's get started!

#         """
#         print(final_message)


# # -------------------------------------------------------------
# # Call some functions and execute code!

# # if this is the main file being run

# if __name__ == "__main__":
#     # Create an instance of a PyBuddy
#     alice = PyBuddy(
#         "Helen",
#         Species.LADY,
#         2,
#         40.123456,
#         "United States",
#         True,
#         ["Git", "GitHub", "Python", "Markdown", "VS Code"],
#     )

#     # Call the buddy's welcome() method
#     alice.display_welcome()


#     # Create another instance of a PyBuddy
#     # using named arguments so it's clear what we're doing
#     rex = PyBuddy(
#         name="Robert",
#         species=Species.MAN,
#         num_legs=2,
#         weight_kgs=40.437241,
#         country="United States",
#         is_available=True,
#         skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
#     )

#     rex.display_welcome()
