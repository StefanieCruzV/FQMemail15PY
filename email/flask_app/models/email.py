from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email= data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET email = %(email)s WHERE id = 1;"
        # los nombres deben ser los de la bd / los valores los del html
        return connectToMySQL('usersHw').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT id, email, created_at, updated_at from users;"
        # los nombres deben ser los de la bd / los valores los del html
        results = connectToMySQL('usersHw').query_db(query)
        emails = []
        for email in results:
            email_data = {
                "id": email["id"],
                "email": email["email"],
                "created_at": email["created_at"],
                "updated_at": email["updated_at"]
            }
            emails.append(cls(email_data))
        return emails 
    
    @staticmethod
    def validate_email( form ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(form['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
