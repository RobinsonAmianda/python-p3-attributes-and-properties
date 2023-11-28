#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
      self._name = ""
    def get_name (self):
       print("Getting name")
       return self._name
    def set_name (self,name):
       if (type(name) == str) and (len(name) > 0 and len(name) <=25): 
        print(f"Name: {name}")
        self._name = name
       else:
        print("Name must be string between 1 and 25 characters.")
    name = property(get_name,set_name )
#An attempted example
#Dog1 = Dog()
#Dog1.name = "SDF-FT-06" 

class Dog:
    def __init__(self):
       self._breed = ""
    def get_breed(self):
       print("Getting breed name.")
       return self
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            print(f"Breed name : {breed}")
            self._breed = breed
        else:
           print("Breed must be in list of approved breeds.")
    breed = property(get_breed,set_breed)
#An attempted example
#Breed1 = Dog()
#Breed1.breed = "Corgi"
       

       


