import sqlite3

class User:
    db_name = 'users.db'

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def initialize_db(cls):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            conn.commit()

    def save(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email) VALUES (?, ?)
            ''', (self.username, self.email))
            conn.commit()

    @classmethod
    def get_users(cls):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
        return users

    @classmethod
    def get_user(cls, user_id):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
        return user

    @classmethod
    def delete_user(cls, user_id):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()

    @classmethod
    def update_user(cls, user_id, username=None, email=None):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            if username:
                cursor.execute('UPDATE users SET username = ? WHERE id = ?', (username, user_id))
            if email:
                cursor.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
            conn.commit

User.initialize_db()


new_user = User('JohnDoe', 'john@.com')
new_user.save()


users = User.get_users()
print(users)


user = User.get_user(1)
print(user)


User.update_user(1, username='messi')


User.delete_user(1)
