#controllers/index.py
import config
from copy import deepcopy
from bottle import Bottle, template, static_file, request
from models import lesson, userdb

class Index(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/static/images/<filename>', callback=self.loadImage)
        self.route('/static/styles/<filename>', callback=self.loadStyle)
        self.route('/static/scripts/<filename>', callback=self.loadScript)
        self.route('/static/fonts/<filename>', callback=self.loadFont)
        self.route('/static/sounds/<filename>', callback=self.loadSound)
        self.route('/static/pdfs/<filename>', callback=self.loadPdf)

        self.route('/', callback=self.index)
        self.route('/lesson/<id:int>', callback=self.lesson)
        self.route('/practice/<id:int>', callback=self.practice)

        self.userdb = userdb.Userdb()

    def loadImage(self, filename):
        return static_file(filename, root='./public/images')

    def loadStyle(self, filename):
        return static_file(filename, root='./public/css')

    def loadScript(self, filename):
        return static_file(filename, root='./public/js')

    def loadFont(self, filename):
        return static_file(filename, root='./public/fonts')

    def loadSound(self, filename):
        return static_file(filename, root='./public/sounds')

    def loadPdf(self, filename):
        return static_file(filename, root='./public/pdfs')

    def checkLoggedIn(self, kdict):
        username = request.get_cookie('logged-in', secret=kdict['secretKey'])
        if username:
            result = self.userdb.checkUsername(username)
            kdict['user'] = result
            kdict['username'] = username
        else:
            kdict['username'] = None

    def index(self):
        kdict = deepcopy(config.kdict)
        kdict['blogTitle'] = "រៀន​វាយ​អក្សរ​ខ្មែរ"
        self.checkLoggedIn(kdict)
        return template('index', data=kdict)

    def lesson(self, id):
        kdict = deepcopy(config.kdict)
        kdict['blogTitle'] = 'មេរៀន​ទី '+kdict['KhmerNumber'][id]
        self.checkLoggedIn(kdict)
        kdict['lesson'] = lesson.__dict__['lesson'+str(id)]
        return template('lesson', data=kdict)

    def practice(self, id):
        kdict = deepcopy(config.kdict)
        kdict['blogTitle'] = 'លំហាត់ទី '+kdict['KhmerNumber'][id]
        self.checkLoggedIn(kdict)
        if kdict['username']:
            id = kdict['user'][2]

        practice = []
        for v in range(id):
            practice += lesson.__dict__['lesson'+str(v+1)]

        kdict['lesson'] = practice
        return template('practice', data=kdict)