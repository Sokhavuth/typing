import config
from bottle import Bottle, template

class Login(Bottle):
  def __init__(self):
    super().__init__()
    self.route('/', callback=self.hello)

  def hello(self):
    return "Hello from Login"