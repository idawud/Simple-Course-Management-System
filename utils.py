import sqlite3
conn = sqlite3.connect("cms.db")
cor = conn.cursor()
  

def select_all_from_db( ): 
    """ 
     This method prints out all data insertd into the 'ccourse' table of the database
    """
    #cor.execute("SELECT * FROM courses WHERE Level='Freshman' AND cost>=200") 
    #cor.execute("SELECT id,cost,Level FROM courses WHERE Level='Freshman' AND cost>=200") 
    query = "SELECT * FROM courses" 
    print(query)
    cor.execute(query) 
    for row in cor.fetchall():
        print(row)


def create_new_user(firstname, lastname, level):
    """
     This method create a new user by entering his/her credentials given into the 'student' table of the databsse
    """
    cor.execute("INSERT INTO students(firstname, lastname, Level) VALUES (?, ?, ?)",(firstname, lastname, level))
    conn.commit()

def print_all_courses(status ,filtor = ""): 
    """ 
     This method prints outcourses insertd into the 'ccourse' table of the database
    """ 
    query = "SELECT id,course,cost FROM courses WHERE Level='" + status +"'"+ filtor
    #print(query)
    print("Id -> Courses -> Cost")
    cor.execute(query) 
    for row in cor.fetchall():
        print(row)

def login(firstname, lastname):
    """ 
     This method return true if a user is found in the DB else false
    """ 
    query = "SELECT * FROM students WHERE firstname='" + firstname + "' AND lastname='" + lastname +"'" 
    cor.execute(query)  
    if len(cor.fetchall()) == 1:
        return True
    else:
        return False 

def level(firstname, lastname):
    """ 
     This method returns the level a user is from the database. i.e Freshman, Sophomore, Junior or Senior 
    """
    query = "SELECT Level FROM students WHERE firstname='" + firstname + "' AND lastname='" + lastname +"'" 
    cor.execute(query)
    data = cor.fetchall()[0]
    return data[0]