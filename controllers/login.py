#controllers/login.py
import config, pdfkit, uuid, os
from copy import deepcopy
from bottle import Bottle, template, request, response, redirect
from verify_email import verify_email
from models import userdb

class Login(Bottle):
  def __init__(self):
    super().__init__()
    self.get('/', callback=self.index)
    self.post('/user', callback=self.postUser)
    self.get('/logout', callback=self.logout)
    self.post('/update', callback=self.updateUser)
    self.get('/pdf', callback=self.createPdf)

    self.userdb = userdb.Userdb()
    
  def index(self):
    kdict = deepcopy(config.kdict)
    kdict['blogTitle'] = "ចុះឈ្មោះ"
    return template('login', data=kdict)

  def postUser(self):
    kdict = deepcopy(config.kdict)
    username = request.forms.getunicode('fusername')
    password = request.forms.getunicode('fpassword')
    email = request.forms.getunicode('femail')

    checkEmail = verify_email(email)

    if checkEmail and username and password:
      result = self.userdb.checkUser(username, password, email)
      if result:
        response.set_cookie('logged-in', result[0], path='/', secret=kdict['secretKey'])
        redirect('/')
      else:
        result = self.userdb.checkUsername(username)
        if not result:
          response.set_cookie('logged-in', username, path='/', secret=kdict['secretKey'])
          self.userdb.insert(username, password, email, 1, False)
          redirect('/')
        else:
          kdict['message'] = 'ឈ្មោះ​អ្នក​ប្រើប្រាស់​នេះ​ត្រូវ​បាន​គេប្រើ​រួច​ហើយ​។'
          return template('login', data=kdict)
    else:
      if not checkEmail:
        kdict['message'] = 'Email របស់​លោក​អ្នក​មិនត្រឹមត្រូវ​ទេ។'
        return template('login', data=kdict)
      elif not (username or password):
        kdict['message'] = 'ត្រូវ​មាន​ឈ្មោះ​អ្នក​ប្រើប្រាស់​និង​ពាក្យ​សំងាត់​។'
        return template('login', data=kdict)

  def logout(self):
    kdict = deepcopy(config.kdict)
    username = request.get_cookie('logged-in', secret=kdict['secretKey'])
    if username:
      self.userdb.deleteUser(username)
      
    response.delete_cookie('logged-in', path='/', secret=kdict['secretKey'])
    redirect('/')

  def updateUser(self):
    kdict = deepcopy(config.kdict)
    username = request.get_cookie('logged-in', secret=kdict['secretKey'])
    if username:
      self.userdb.updateUser(username)
      grade = self.userdb.checkUsername(username)
      return {'grade':grade[2]}

  def createPdf(sefl):
    id = str(uuid.uuid4().int)
    if 'DYNO' in os.environ:
      config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
      pdfkit.from_url('http://google.com', 'public/pdfs/'+id+'.pdf', configuration=config)
    else:
      pdfkit.from_url('http://google.com', 'public/pdfs/'+id+'.pdf')

    return '<script>window.location="/static/pdfs/'+id+'.pdf"</script>'