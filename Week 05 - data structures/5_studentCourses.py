#A program that create a dictionary for students, each student will have different modules, each module could have different grades.
#i.e. dictionary of a dictionary
#top level dicionary is student, keys are name, modules
#module dictionaryies contains an array of courses which are each dictionaries
#each module dictionary contains the keys, course name and the grade for the course


#Author:Jon Ishaque
#Create dictionary
student={
    #key value/pair: key = name, value ="Mary"
    "name":"Mary",
    #start modules array with 3 module dictionaries
    "modules":[
        #course 1 new dict. each module dictionary has two key value pairs. In this module: 1. key=courseName, value ="Programming",2 key=grade, value =:45
        #
        {
        #key/value pair: key=courseName, value 
        "courseName":"Programming","grade":45
        },
        #course 2 new dict
        {"courseName":"History","grade":99
        },
        #course 3 new dict
        {"courseName":"Applied Databases","grade":89
        }
    ]
}
#out put key value pair for student dictionary
print("Student:{}".format(student["name"]))
#for each module in modules, print the two key value pairs for each dictionary 'module'. coursname/value, grade/value
for module in student["modules"]:
    print("\t{}\t:{}".format(module["courseName"],module["grade"]))