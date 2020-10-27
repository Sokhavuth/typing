#main.py
import os
from bottle import route, run
    
@route('/')
def main():
    return "Hello World!"
    
if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
else: 
  run(host='localhost', port=8000, debug=True, reloader=True)