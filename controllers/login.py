#controllers/login.py
import config
from bottle import Bottle, template, request, redirect
from verify_email import verify_email
from models.userdb import Userdb

userdb = Userdb()

class Login(Bottle):
  def __init__(self):
    super().__init__()
    self.get('/', callback=self.index)
    self.get('/user', callback=self.getUser)
    self.post('/user', callback=self.postUser)
    self.get('/signup', callback=self.getSignup)
    self.post('/signup', callback=self.postSignup)

  def index(self):
    config.kdict['blogTitle'] = "ចុះឈ្មោះ"
    return template('login', data=config.kdict)

  def postUser(self):
    username = request.forms.getunicode('fusername')
    password = request.forms.getunicode('fpassword')
    email = request.forms.getunicode('femail')

    if verify_email(email):
      return 'post user'
    else:
      config.kdict['message'] = 'Email របស់​លោក​អ្នក​មិនត្រឹមត្រូវ​ទេ។'
      redirect('/login')

  def getUser(self):
    return 'get user'

  def getSignup(self):
    return 'get signUp'

  def postSignup(self):
    return 'post signup'
