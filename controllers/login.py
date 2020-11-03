#controllers/login.py
import config
from bottle import Bottle, template, request, response, redirect
from verify_email import verify_email
from models.userdb import Userdb

userdb = Userdb()

class Login(Bottle):
  def __init__(self):
    super().__init__()
    self.get('/', callback=self.index)
    self.get('/user', callback=self.getUser)
    self.post('/user', callback=self.postUser)
    self.get('/logout', callback=self.logout)
    
  def index(self):
    config.kdict['blogTitle'] = "ចុះឈ្មោះ"
    return template('login', data=config.kdict)

  def postUser(self):
    username = request.forms.getunicode('fusername')
    password = request.forms.getunicode('fpassword')
    email = request.forms.getunicode('femail')

    checkEmail = verify_email(email)

    if checkEmail and username and password:
      result = userdb.checkUser(username, password, email)
      if result:
        config.kdict['user'] = result
        redirect('/')
      else:
        result = userdb.checkUsername(username)
        if not result:
          userdb.insert(username, password, email, 1, False)
          result = userdb.checkUser(username, password, email)
          config.kdict['user'] = result
          redirect('/')
        else:
          config.kdict['message'] = 'ឈ្មោះ​អ្នក​ប្រើប្រាស់​នេះ​ត្រូវ​បាន​គេប្រើ​រួច​ហើយ​។'
          redirect('/login')
    else:
      if not checkEmail:
        config.kdict['message'] = 'Email របស់​លោក​អ្នក​មិនត្រឹមត្រូវ​ទេ។'
        redirect('/login')
      elif not (username or password):
        config.kdict['message'] = 'ត្រូវ​មាន​ឈ្មោះ​អ្នក​ប្រើប្រាស់​និង​ពាក្យ​សំងាត់​។'
        redirect('/login')

  def getUser(self):
    return 'get user'

  def logout(self):
    config.kdict['user'] = ('ភ្ញៀវ', 'អត់មាន', 1)
    redirect('/')