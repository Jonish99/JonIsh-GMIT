#Create a dictorary for students, each student will have different moudles each could have different grades.
#i.e. dictionary of a dictionary
#top level dict is student, keys are name, modules
#modules contains an array of courses which are each dictionaries
#each module dictionary contains the keys, course name and the grade for the course

#Author:Jon Ishaque

student={
    "name":"Mary",
    #start modules arrar
    "modules":[
        #course 1 new dict
        {
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
print("Student:{}".format(student["name"]))
for module in student["modules"]:
    print("\t{}\t:{}".format(module["courseName"],module["grade"]))