#controllers/login.py
import config, os, uuid, pydf, webbrowser
from copy import deepcopy
from bottle import Bottle, template, request, response, redirect
from verify_email import verify_email
from models import userdb
from models.certificate import Certificate

class Login(Bottle):
  def __init__(self):
    super().__init__()
    self.get('/', callback=self.index)
    self.post('/user', callback=self.postUser)
    self.get('/update', callback=self.updateUser)
    self.get('/logout', callback=self.logout)

    self.userdb = userdb.Userdb()
    self.template = Certificate()
    
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
      grade = self.userdb.checkUsername(username)
      if grade[2] < 8:
        self.userdb.updateUser(username)
        return {'grade':grade[2]}
      elif grade[2] == 8:
        pdfFile = self.createPdf(username)
        return {'grade':grade[2], 'pdf':pdfFile}
      else:
        return {'grade':grade[2]}
      
  def createPdf(self, username=0):
    id = str(uuid.uuid4().int)
    rootPath = os.getcwd()+'/public/pdfs/'
    pdfFile = '/static/pdfs/' + id+'.pdf'
    template = self.template.substitute()
    options = {
      'page-size': 'Letter',
      'margin-top': '0',
      'margin-right': '0',
      'margin-bottom': '0',
      'margin-left': '0',
      'encoding': "UTF-8",
      'orientation': 'Landscape'
    }
    
    if 'DYNO' in os.environ:
      pdf = pydf.generate_pdf(template)
      print(pdf)
      with open(rootPath + id+'.pdf', 'wb') as f:
        f.write(pdf)
        f.close()

    else:
      import pdfkit
      pdf = pdfkit.from_string(template, False, options=options)
      with open(rootPath + id+'.pdf', 'wb') as f:
        f.write(pdf)
        f.close()

    return pdfFile
    
 