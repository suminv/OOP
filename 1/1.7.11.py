class Viber:
    db_messages = []

    @classmethod
    def add_message(cls, msg):
        cls.db_messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.db_messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num: int):
        return cls.db_messages[-num:]

    @classmethod
    def total_messages(cls):
        return len(cls.db_messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
