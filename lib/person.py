#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self):
      self._name = ""
    def get_name (self):
       print("Getting name")
       return self._name
    def set_name (self,name):
       if (type(name) == str) and (len(name) > 0 and len(name) <=25): 
        print(f"Name: {name.title()}")
        self._name = name
       else:
        print("Name must be string between 1 and 25 characters.")
    name = property(get_name,set_name )
#An attempted example
#name1 = Person()
#name1.name = "moringa"

class Person:
  def __init__(self):
    self._job = ""
  def get_job(self):
    print("Getting job post")
    return self
  def set_job(self,job):
    if job in APPROVED_JOBS:
        print(f"Available job : {job}") 
        self._job = job
    else:
      print("Job must be in list of approved jobs.")
  job = property(get_job,set_job)

#An attempted example
#job1 = Person()
#job1.job = "Sales"