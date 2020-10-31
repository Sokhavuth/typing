#controllers/index.py
import config
from bottle import Bottle, template, static_file
from models import lesson

class Index(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/static/images/<filename>', callback=self.loadImage)
        self.route('/static/styles/<filename>', callback=self.loadStyle)
        self.route('/static/scripts/<filename>', callback=self.loadScript)
        self.route('/static/fonts/<filename>', callback=self.loadFont)
        self.route('/static/sounds/<filename>', callback=self.loadSound)

        self.route('/', callback=self.index)
        self.route('/lesson/<id:int>', callback=self.lesson)
        self.route('/practice/<id:int>', callback=self.practice)

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

    def index(self):
        config.kdict['blogTitle'] = "រៀន​វាយ​អក្សរ​ខ្មែរ"
        config.kdict['lesson'] = lesson.lesson1
        return template('index', data=config.kdict)

    def lesson(self, id):
        config.kdict['blogTitle'] = 'មេរៀន​ទី '+config.kdict['KhmerNumber'][id]
        config.kdict['lesson'] = lesson.__dict__['lesson'+str(id)]
        return template('lesson', data=config.kdict)

    def practice(self, id):
        config.kdict['blogTitle'] = 'លំហាត់ទី '+config.kdict['KhmerNumber'][id]
        practice = []
        for v in range(id):
            practice += lesson.__dict__['lesson'+str(v+1)]

        config.kdict['lesson'] = practice
        return template('practice', data=config.kdict)