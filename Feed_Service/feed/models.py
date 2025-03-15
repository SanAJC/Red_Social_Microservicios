import datetime
from mongoengine import Document, IntField, StringField, DateTimeField

class Post(Document):
    meta = {'collection': 'posts'}
    user_id = IntField(required=True) 
    content = StringField(required=True, max_length=280)  
    created_at = DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return f"Post by {self.user_id} at {self.created_at}"

