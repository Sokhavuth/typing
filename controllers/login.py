#controllers/login.py
import config, os, uuid, pydf, asyncio, time
from pytz import timezone
from datetime import datetime 
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
    self.post('/update', callback=self.updateUser)
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
    level = request.params.getunicode('level')
    username = request.get_cookie('logged-in', secret=kdict['secretKey'])
    if username and level:
      grade = self.userdb.checkUsername(username)
      if (grade[2] < 8) and (kdict['KhmerNumber'][grade[2]] == level):
        self.userdb.updateUser(username)
        grade = self.userdb.checkUsername(username)
        return {'grade':grade[2]}
      elif (grade[2] == 8) and (kdict['KhmerNumber'][grade[2]] == level):
        pdfFile = self.createPdf(username)
        time.sleep(.5)
        return {'grade':grade[2], 'pdf':pdfFile}
      else:
        return {'grade':grade[2]}
      
  def createPdf(self, username):
    kdict = deepcopy(config.kdict)
    id = str(uuid.uuid4().int)
    khtz = timezone('Asia/Phnom_Penh')
    date = datetime.now().astimezone(tz=khtz).strftime('%d%m%Y')
    day = date[:2]
    day = kdict['KhmerNumber'][int(day[0])]+kdict['KhmerNumber'][int(day[1])]
    month = date[2:4]
    month = kdict['KhmerMonth'][int(month)-1]
    year = date[4:]
    print(year)
    year = kdict['KhmerNumber'][int(year[0])]+kdict['KhmerNumber'][int(year[1])]+kdict['KhmerNumber'][int(year[2])]+kdict['KhmerNumber'][int(year[3])]
    date = day+ ' ' + ' ' +month + ' ' + year
    pdfFile = '/static/pdfs/'+id+'.pdf'

    async def generateTemplate():
      template = self.template.substitute(username=username, date=date)
      return template

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
      async def certificateGenerate():
        template = await generateTemplate()
        pdf = pydf.generate_pdf(template, **options)
        with open('public/pdfs/'+id+'.pdf', 'wb') as f:
          f.write(pdf)
          f.close()

      asyncio.run(certificateGenerate())

    else:
      import pdfkit
      template = self.template.substitute(username=username, date=date)
      pdf = pdfkit.from_string(template, False, options=options)
      with open('public/pdfs/'+id+'.pdf', 'wb') as f:
        f.write(pdf)
        f.close()

    return pdfFile