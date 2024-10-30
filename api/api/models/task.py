from datetime import datetime

class Task:
    def __init__(self, title, description, status):
        self.id = None
        self.title = title
        self.description = description
        self.status = status 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return { 
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "status" : self.status,
            "created_at" : self.created_at.isoformat(),
            "updated_at" : self.updated_at.isoformat()
        }