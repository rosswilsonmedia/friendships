from ..config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELECT * FROM users"
        results=connectToMySQL('friendships_schema').query_db(query)
        all_users=[]
        for user in results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def get_all_friendships(cls):
        query="SELECT * FROM users "\
            "JOIN friendships ON users.id=friendships.user_id "\
            "JOIN users AS friends ON friendships.friend_id=friends.id"
        results=connectToMySQL('friendships_schema').query_db(query)
        return results

    @classmethod
    def create_user(cls, data):
        query="INSERT INTO users (first_name, last_name, created_at, updated_at) "\
            "VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        user_id=connectToMySQL('friendships_schema').query_db(query, data)
        return user_id

    @classmethod
    def create_friendship(cls, data):
        query="INSERT INTO friendships (user_id, friend_id, created_at, updated_at) "\
            "VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());"
        friendship_id=connectToMySQL('friendships_schema').query_db(query, data)
        return friendship_id