import sqlite3

conn = sqlite3.connect("cms.db")
cor = conn.cursor()

anConn = sqlite3.connect("studentRecords.db")
anCor = anConn.cursor()


def enroll_courses(fil):
    """ 
     This method returns the course,cost and level from the courses table of the cms database 
    """
    query = "SELECT course,cost,level FROM courses WHERE id ="+str(fil)  
    cor.execute(query) 
    data = cor.fetchall()[0]
    return data

def insert_new_courses(firstname, course, cost): 
    """
     This method insert data into the studentsRecord database 
    """
    query = "INSERT INTO "+ str(firstname)+"(course,cost) VALUES (?, ?)"
    anCor.execute( query, (course, cost))
    anConn.commit()

def delete_courses(data,firstname):
    """ 
     This method DELETE a set of row(s) from the studentsRecord database 
    """
    for dt in data:
        query = "DELETE FROM "+ firstname+" WHERE id=" +str(dt) 
        anCor.execute(query)
        anConn.commit()

def courses_enrolled_in(firstname):
    """ 
     This method prints all information relating to a specific student 
     with the firstname
    """
    query = "SELECT * FROM "+ str(firstname)
    anCor.execute(query) 
    print("Id -> Courses -> Cost")
    for dt in anCor.fetchall():
        print(dt) 

def all_course_info(firstname, lastname):
    """ 
     This method print all the information on a user thus far,
     i.e. Courses ,cost, fullname & the total amount of all courses 
    """
    print("Your fullname is: " + str(firstname) + " "+ str(lastname))
    query = "SELECT * FROM "+ str(firstname)
    anCor.execute(query)
    price = 0
    for dt in anCor.fetchall():
        price = price + dt[2]
 
    print("You are Enrolled to the following Course(s): ")
    print("Id => Course => Cost")
    anCor.execute(query)
    for dt in anCor.fetchall():
        print(str(dt[0]) + "   " + str(dt[1]) + " " + str(dt[2]))

    print("The Total Amount is: $"+str(round(price,2)))
    print("\nThank You!!! \nHappy Learning")
