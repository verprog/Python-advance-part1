import shelve

FILENAME = 'test_db'

# with shelve.open(FILENAME) as db:
#     db['users'] = 'login'

# with shelve.open(FILENAME) as db:
#     print(db['new_key'])
#     print(db.get('new_key1'))
#     print(dict(db.items()))
#     db.clear()
#     print(dict(db.items()))


class UserDB:
    _instances = None
    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super().__new__(cls)
            return cls._instances
        else:
            raise   NameError(f'The objects exists')

    def __init__(self, filename):
        self._filename = filename

    def get_db(self):
        return shelve.open(self._filename)

    def create_user(self, **kwargs):
        with shelve.open(self._filename) as db:
            users = db.get('users')
            if not users:
                db['users']= kwargs
            else:
                users.update(kwargs)
                db['users'] = users

    def get_all_users(self):
        with shelve.open(self._filename) as db:
            return dict(db['users'].items())


db = UserDB(FILENAME)

db.create_user(**{'login': 'password'})
db.create_user(**{'new_login': 'new_password'})
print(db.get_all_users())





