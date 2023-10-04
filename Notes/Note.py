from pip._internal.utils import datetime


class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now()
