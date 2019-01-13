import time
from models import Model


def format_time(unix_timestamp):
    f = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(unix_timestamp)
    formatted = time.strftime(f, value)
    return formatted


class Todo(Model):
    def __init__(self, form):
        super().__init__(form)
        self.content = form['content']
        self.user_id = form.get('user_id', None)
        self.created_time = form.get('created_time', -1)
        self.updated_time = form.get('updated_time', -1)

    @classmethod
    def add(cls, form, user_id):
        t = Todo(form)
        t.user_id = user_id
        t.created_time = format_time(time.time())
        t.updated_time = t.created_time
        t.save()
        return t

    @classmethod
    def update(cls, data_id, **kwargs):
        t = cls.find_by(id=data_id)

        for k, v in kwargs.items():
            if hasattr(t, k):
                setattr(t, k, v)

        t.updated_time = format_time(time.time())

        t.save()
        return t