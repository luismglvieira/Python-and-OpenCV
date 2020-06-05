# -*- coding: utf-8 -*-

def student(name='Unknown name', age=0):
    print("name: ", name)
    print("age: ", age)
    
student('luis')
print()
def student(name, age, *marks):
    print("name: ", name)
    print("age: ", age)
    #print("marks: ", marks)
    for x in marks:
        print(x)
    
student('luis', 28, 95, 70, 80, 50)
print()
def student(name, age, **marks):
    print("name: ", name)
    print("age: ", age)
    #print("marks: ", marks)
    for key, value in marks.items():
        print(key,': ', value)
    
student('luis', 28, english = 95, math = 70, physics = 80, biology = 50)