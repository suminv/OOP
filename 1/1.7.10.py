class AppStore:
    def __init__(self):
        self.store = []

    def add_application(self, app):
        self.store.append(app)

    def remove_application(self, app):
        self.store.remove(app)


    def block_application(self, app):
        app.blocked = True


    def total_apps(self):
        return len(self.store)


class Application:
    def __init__(self, name, blocked=True):
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
