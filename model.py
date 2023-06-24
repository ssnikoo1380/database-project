import mysql.connector


class user:
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
        user_id_query = """SELECT COUNT(1) user_id FROM users WHERE user_id = %s"""
        input_user_id = (input_user_id, )
        self.usercursor.execute(user_id_query, input_user_id)
        return self.usercursor.fetchall()

    def return_user_pass(self, input_user_id, input_user_pass):
        print(input_user_pass)
        user_pass_query = """SELECT count(1) password FROM users WHERE user_id = %s and password = %s"""
        input_user_pass = (input_user_id, input_user_pass, )
        self.usercursor.execute(user_pass_query, input_user_pass)
        return self.usercursor.fetchall()


class message:
    def create_table(cursor):
        cursor.execute("""CREATE TABLE messages(
                msg_id INT AUTO_INCREMENT NOT NULL,
                text TEXT,
                sender_id INT NOT NULL,
                receiver_id INT NOT NULL,
                is_read BIT,
                FKuser_id INT NOT NULL,
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
