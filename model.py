import mysql.connector
import random
import string
import datetime
import time


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

    def return_user_id(self, input_user_ids):
        user_id_query = """SELECT user_id FROM users WHERE user_id = %s"""
        input_user_ids = input_user_ids.split()
        user_ids = []
        for input_user_id in input_user_ids:
            input_user_id = (input_user_id, )
            self.usercursor.execute(user_id_query, input_user_id)
            query_reult = self.usercursor.fetchall()
            if query_reult:
                user_ids.append(query_reult)
        return user_ids

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

    def is_admin(self, user_id):
        query = "SELECT user_id FROM users WHERE user_id = %s and %s IN (SELECT user_id FROM users WHERE is_admin = %s)"
        values = (user_id, user_id, 1)
        self.usercursor.execute(query, values)
        return True if self.usercursor.fetchall() else False


class Message:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="26642664",
        database="chat_app"
    )
    messagecursor = mydb.cursor()

    def send_message(self, sender, receivers, message):
        if message:
            try:
                msgcrt_query = "INSERT INTO messages (text, receiver_id, is_read, date, FKuser_id) VALUES (%s, %s, %s, %s, %s)"
                receivers = receivers.split()
                msgcrt_values = [(message, receiver, False,
                                  datetime.datetime.now(), sender) for receiver in receivers]
                self.messagecursor.executemany(msgcrt_query, msgcrt_values)
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
        query = "SELECT receiver_id, FKuser_id FROM messages WHERE FKuser_id = %s or receiver_id = %s"
        values = (sender, sender)
        self.messagecursor.execute(query, values)
        chatlist = []
        for chat in self.messagecursor.fetchall():
            chatlist.append(chat[0] if chat[0] != sender else chat[1])
        return chatlist

    def return_chat(self, sender, receiver):
        query = "SELECT text, FKuser_id FROM messages WHERE (FKuser_id = %s or receiver_id = %s) and (receiver_id = %s or FKuser_id = %s) ORDER BY date"
        values = (sender, sender, receiver, receiver)
        self.messagecursor.execute(query, values)
        return self.messagecursor.fetchall()

    def seen(self, sender, receiver):
        try:
            query = "UPDATE messages SET is_read = %s WHERE is_read = %s and receiver_id = %s and FKuser_id = %s"
            # setting receiver_id equal to my id so that
            # the is_read field of every message from the person that im chatting with becomes true
            values = (1, 0, sender, receiver)
            self.messagecursor.execute(query, values)
            mydb.commit()
        except Exception:
            return False
        return True

    def message_list(self):
        self.messagecursor.execute("SELECT * FROM messages")
        return self.messagecursor.fetchall()

    def create_table(self):
        self.messagecursor.execute("""CREATE TABLE messages(
                msg_id INT AUTO_INCREMENT NOT NULL,
                text TEXT,
                receiver_id VARCHAR(255) NOT NULL,
                is_read BIT,
                date DATETIME,
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
message = Message()
message.send_message("ssn", ("ssn9", "ssn8", "ssn7"), "hello")
# for x in range(1000000):
#     randint1 = random.choice([x for x in range(10)] + ["", ])
#     randint2 = random.choice([x for x in range(10)] + ["", ])
#     randlst = random.choices(string.ascii_letters, k=random.choice(range(256)))
#     randstr = ""
#     for char in randlst:
#         randstr = randstr + char
#     message.send_message("ssn" + str(randint2), "ssn" + str(randint1), randstr)
