'''
This document mainly deals with the calculation of simple values of some people.
---Author: Season
---Language: Python
---Signature: S and A
              PHJsi
#############
#####---#####
###--   --###
#--S and A--#
###--   --###
#####---#####
#############
~~~~~~~~~~~~~
#############
#####---#####
###--   --###
#---PHJsi---#
###--   --###
#####---#####
#############
'''





from datetime import *



class Person:
    def __init__(self,name:str = "",LifeExperience:list = [],year:int = date.today().year,\
        month:int = date.today().month,\
        day:int = date.today().day) -> None:
        self.born_date = date(year,month,day)
        self.name = name
        self.LifeExperience = LifeExperience
    
    def add(self,*life):
        self.LifeExperience += life
    
    def age(self) -> int:
        return date.today().year - self.born_date.year

class Student(Person):
    def __init__(self,name:str = "",studentID:str = "0",scores:list = [],LifeExperience:list = [],year:int = date.today().year,\
        month:int = date.today().month,\
        day:int = date.today().day) -> None:
        super().__init__(name,LifeExperience, year, month, day)
        self.studentID = studentID
        self.scores = scores

    def add_score(self,*score):
        self.scores += score
    
    def getAve(self):
        return sum(self.scores)/len(self.scores)





if __name__ == "__main__":
    print("Welcome to my library: person.py!")
