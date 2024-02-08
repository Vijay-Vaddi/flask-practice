#  typically can do autherization storage inside models wher user class is. 

class  User():

    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"User ID: {self.id}"
