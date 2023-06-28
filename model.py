import mysql.connector
import random
import string


class User:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="26642664",
        database="chat_app"
    )
    usercursor = mydb.cursor()

    def create_table(self):
        self.usercursor.execute("""CREATE TABLE users( 
                user_id VARCHAR(255) NOT NULL, 
                username VARCHAR(255), 
                password VARCHAR(255), 
                is_admin BIT,
                PRIMARY KEY (user_id)
                                            )"""
                                )

    def return_user_id(self, input_user_id):
        user_id_query = """SELECT user_id FROM users WHERE user_id = %s"""
        input_user_id = (input_user_id, )
        self.usercursor.execute(user_id_query, input_user_id)
        return self.usercursor.fetchall()

    def return_user_pass(self, input_user_id):
        user_pass_query = """SELECT password FROM users WHERE user_id = %s"""
        self.usercursor.execute(user_pass_query, (input_user_id, ))
        return self.usercursor.fetchall()

    def create_user(self, information):
        try:
            add_user_query = """INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)"""
            add_user_values = tuple(x for x in information)
            self.usercursor.execute(add_user_query, add_user_values)
            self.mydb.commit()
        except Exception:
            return False
        return True


class Message:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="26642664",
        database="chat_app"
    )
    messagecursor = mydb.cursor()

    def send_message(self, sender, receiver, message):
        try:
            msgcrt_query = "INSERT INTO messages (text, receiver_id, is_read, FKuser_id) VALUES (%s, %s, %s, %s)"
            msgcrt_values = (message, receiver, False, sender)
            self.messagecursor.execute(msgcrt_query, msgcrt_values)
            self.mydb.commit()
        except Exception:
            return False
        return True

    def chat_exists(self, receiver, sender):
        query = "SELECT * FROM messages WHERE receiver_id = %s and FKuser_id = %s"
        values = (receiver, sender)
        self.messagecursor.execute(query, values)
        return True if self.messagecursor.fetchall() else False

    def delete_chat(self, receiver, sender):
        try:
            query = "DELETE FROM messages WHERE receiver_id = %s and FKuser_id = %s"
            values = (receiver, sender)
            self.messagecursor.execute(query, values)
            self.mydb.commit()
        except Exception:
            return False
        return True

    def return_chatlist(self, sender):
        query = "SELECT receiver_id FROM messages WHERE FKuser_id = %s "
        values = (sender, )
        self.messagecursor.execute(query, values)
        return self.messagecursor.fetchall()

    def create_table(self):
        self.messagecursor.execute("""CREATE TABLE messages(
                msg_id INT AUTO_INCREMENT NOT NULL,
                text TEXT,
                receiver_id VARCHAR(255) NOT NULL,
                is_read BIT,
                FKuser_id VARCHAR(255) NOT NULL,
                PRIMARY KEY (msg_id),
                FOREIGN KEY (FKuser_id) REFERENCES users(user_id)

                                                )"""
                                   )


def create_database(cursor):
    cursor.execute("CREATE DATABASE chat_app")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="26642664",
    database="chat_app"
)
mycursor = mydb.cursor()
for x in range(100):
    randint1 = random.choice(range(10))
    randint2 = random.choice(range(10))
    randlst = random.choices(string.ascii_letters, k=random.choice(range(256)))
    randstr = ""
    for char in randlst:
        randstr = randstr + char
    query = "INSERT INTO messages (text, receiver_id, is_read, FKuser_id) VALUES (%s, %s, %s, %s)"
    values = (randstr, "ssn" + str(randint1), False, "ssn" + str(randint2))
    mycursor.execute(query, values)
    mydb.commit()
