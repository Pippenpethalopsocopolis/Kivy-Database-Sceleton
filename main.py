#This is just a basic sekeleton for a database integretion into a kivy application.
#You change kv file and py file accordance to your needs, like I said, this is just a skeleton for a database integration.
#Made by Berk Öcal, Linkedin: www.linkedin.com/in/berkocall/
#Gmail: berkocal99@gmail.com you can communucate with me via mail or via my linkedin account.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import mysql.connector

Window.size = (400, 600)

class database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",   #You can change this if your username is different
            passwd= "",  #Write your MySQL password here
            database = "second_db"  #Name your database as you wish
            )

    def cdatabaseANDctable(self):
        c = self.mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS second_db")  #If you changed your database name remember to change the "second_db" here too.
        c.execute("""CREATE TABLE if not exists customers(
                    name VARCHAR(25))  
                """)
        self.mydb.commit()
        self.mydb.close()

class MahApp(MDApp, database):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.secondary_palette = "Amber"
        self.theme_cls.material_style = "M2"

        call = database()
        call.mydb
        call.cdatabaseANDctable()

        return Builder.load_file('my.kv')

    def submit(self):
        call = database()
        call.mydb
        c = call.mydb.cursor()
        sql_command = "INSERT INTO customers (name) VALUES (%s)"
        values = (self.root.ids.word_input.text,)
        c.execute(sql_command, values)
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} added.'
        self.root.ids.word_input.text = ''
        call.mydb.commit()
        call.mydb.close()

    def show_records(self):
        call = database()
        call.mydb
        c = call.mydb.cursor()
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        word = ''
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'
        call.mydb.commit()
        call.mydb.close()

MahApp().run()