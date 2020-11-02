#controllers/login.py
import config
from bottle import Bottle, template, static_file
#from models import lesson

class Login(Bottle):
    def __init__(self):
      super().__init__()
      self.route('/', callback=self.index)
      self.get('/user', callback=self.getUser)
      self.post('/user', callback=self.postUser)

    def index(self):
      config.kdict['blogTitle'] = "ចុះឈ្មោះ"
      return template('login', data=config.kdict)

    def postUser(self):
      return 'post user'

    def getUser(self):
      return 'get user'