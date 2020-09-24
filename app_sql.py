import os
import unittest
import pymysql
from func_sql_1 import clear_screen, print_list
from db_func import db,update, query

#===================================

mydb = db()

get_all_people = "SELECT * FROM person"
get_all_drinks = "SELECT * FROM drink"
get_all_people_with_prefs= """
SELECT person.id, person.name
FROM person
LEFT Join drink ON drink.id = person.name;
"""

people = query(mydb, get_all_people)
drinks = query(mydb, get_all_drinks)
prefs = query(mydb, get_all_people_with_prefs)

mycursor = mydb.cursor()

def save (people_drinks_prefs):
    update(mydb, people_drinks_prefs)

def create_pref():
    people = query(mydb, get_all_people)
    print_list(people,"people")

    try:
        person_id = int(input("choose a person: "))
    except:
        print("Please try again")
    drinks = query(mydb, get_all_drinks)
    print_list(drinks,"Drinks")
    try:
        drink_id = int(input("choose a drink: "))
    except:
        print("Please try again")
    add_fav_drink = f"UPDATE person SET drink = {drink_id} WHERE id = {person_id}"
    mycursor.execute(add_fav_drink)
    mydb.commit()
    mycursor.close()

def insert_person(data):
    query = "INSERT INTO person (name) VALUES (%s)"
    recordTuple = (data)
    mycursor.execute(query,recordTuple)
    mydb.commit()
    mycursor.close()

def insert_drink(data):
    query = "INSERT INTO drink (drink_name) VALUES (%s)"
    recordTuple = (data)
    mycursor.execute(query,recordTuple)
    mydb.commit()
    mycursor.close()


#create new person
# name = "Abdul"
# create_person = f"INSERT INTO person (name) VALUES('{name}')"
#REPLACE FUNC = create_person_or_drink


# update(mydb, add_fav_drink)

menu = """
Please choose an option:
[1] List All People
[2] List All Drinks
[3] List All Preferences
[4] Create Person
[5] Create Drink
[6] Create Preference
[0] Exit
"""


# prefs = {}

def app():
    while True:
        option = None
        exit_option = 0
        try:
            option = int(input(menu))
        except ValueError:
            print('Please enter a number')



        if option == 1:
            print_list(people, "people")  # Show list of ppl
            
        elif option == 2:
            print_list(drinks, "drinks")  # Show list of drinks
        
        elif option == 3:
            print_list(prefs, "prefs")  # Show list of prefs
        
        elif option == 4:
            name= input("please enter name: ")
            insert_person([(name)])

        elif option == 5:
            drink_1= input("please enter drink name: ")
            insert_person([(drink_1)])

        elif option == 6:

            create_pref()
            print_list(prefs, "pref")

        elif option == exit_option:
            print ("Bye!")
            break

if __name__ == '__main__':
    app()