import sqlite3
import sys
import utils
import stud

"""
@Author: Ismail Dawud Ibrahim
@email: ismaildawud96@gmail.com
@Date: 24 / 08 / 2018

This Application is a simple Course Management sYSTEM, WHERE a new user can create an account and add courses
and old users can also login add more coures or drop courses using python and sqlite3.
some useful sql commands:
    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index
"""

conn = sqlite3.connect("cms.db")
cor = conn.cursor()

anConn = sqlite3.connect("studentRecords.db")
anCor = anConn.cursor()

cor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,firstname TEXT NOT NULL, lastname TEXT NOT NULL, Level TEXT NOT NULL)")
    
firtname, lastname= "", ""
level = 0 

print("*** Welcome To Course->Management->System ***") 

status = input("Are a new Student Y/N: ")
if(status.lower() == "y" or status.lower() == "yes"):
    # create new user
    firtname = str(input("Enter Your Firstname: "))
    lastname = str(input("Enter Your Lastname: "))
    level =int( input("Available levels !!! \n 1-FreshMan \n 2-Sophomore \n 3-Junior \n 4-Senior\nEnter Your Level: ") ) 
    
    status = ""
    if(level == 1):
        status = "Freshman"
    elif(level == 2):
        status = "Sophomore"
    elif(level == 3):
        status = "Junior"
    elif(level == 4):
        status = "Senior"
    else:
        sys.exit(0)
    
    utils.create_new_user(firtname, lastname, status)
    print("New User Added Successfully !!!")
    print("These are all Available Courses to choose from !!!") 
    utils.print_all_courses(status) 
    sql = "CREATE TABLE IF NOT EXISTS "+ firtname+"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, course TEXT NOT NULL UNIQUE, cost REAL)"
    anCor.execute(sql)
    courseArr = []
    dt = ""
    print("Please Enter the Id of the course you want to add or 'quit' to Exit: ")
    while dt.lower() != "quit":
        dt =  input(" >>>> ")
        if dt.lower() != "quit":
            courseArr.append(int(dt)) 
    bigK= [] 
    for l in map(stud.enroll_courses, courseArr):
        bigK.append(l)
    for rm in bigK:
        if rm[2].lower() == status.lower():
            stud.insert_new_courses(firtname, rm[0], rm[1])
    
    print("Database updated Sucessfully !!!")
    stud.all_course_info(firtname, lastname) 

elif(status.lower() == "n" or status.lower() == "no"):
    print("PLEASE LOGIN ")

    firstname = str(input("Enter Your Firstname: "))
    lastname = str(input("Enter Your Lastname: "))
    alert = utils.login(firstname, lastname)
    if alert:
        print("You are in our database")  
        print("These are all Available Courses to choose from !!!")
        lev = utils.level(firstname, lastname)
        utils.print_all_courses(lev) 

        sql = "CREATE TABLE IF NOT EXISTS "+ firstname+"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, course TEXT NOT NULL UNIQUE, cost REAL)"
        anCor.execute(sql) 

        addCourses = input("Do you want to add more Courses Yes | No:")
        if(addCourses.lower() == "y" or addCourses.lower() == "yes"):
            courseArr = []
            dt = ""
            print("Please Enter the Id of the course you want to add or 'quit' to Exit: ")
            while dt.lower() != "quit":
                dt =  input(" >>>> ")
                if dt.lower() != "quit":
                    courseArr.append(int(dt)) 
            bigK= [] 
            for l in map(stud.enroll_courses, courseArr):
                bigK.append(l)
            for rm in bigK:
                if rm[2].lower() == lev.lower():
                    stud.insert_new_courses(firstname, rm[0], rm[1])
            print("Database updated Sucessfully !!!")
                    
        elif(addCourses.lower() == "n" or addCourses.lower() == "no"):
            pass
        #else:
            #sys.exit(0) 

        dropCourses = input("Do you want to drop some Courses Yes | No:")
        if(dropCourses.lower() == "y" or dropCourses.lower() == "yes"):

            print("These are all the courese you can drop")
            stud.courses_enrolled_in(firstname)

            courseArr = []
            dt = ""
            print("Please Enter the Id of the course you want to drop or 'quit' to Exit: ")
            while dt.lower() != "quit":
                dt =  input(" >>>> ")
                if dt.lower() != "quit":
                    courseArr.append(int(dt)) 
            
            stud.delete_courses(courseArr, firstname)
            print("Database updated Sucessfully !!!")
        elif(dropCourses.lower() == "n" or dropCourses.lower() == "no"):
            pass
        #else:
           # sys.exit(0) 
         
        stud.all_course_info(firstname, lastname)

    else:
        print("You are NOT in our database")
        print("Restart the program and register as new user")
        #sys.exit(0)  

else:
    print("Invalid Status!!!")
    sys.exit(0)
  
#anCor.close()
anConn.close()

#cor.close()
conn.close()