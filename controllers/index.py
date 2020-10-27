from bottle import Bottle

class Index(Bottle):
    def __init__(self):
        super(Index, self).__init__()
        self.route('/', callback=self.index)

    def index(self):
        return "Welcome to Khmer Web Blogger!"

