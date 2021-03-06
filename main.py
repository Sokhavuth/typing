#main.py
import os
from controllers.index import Index
from controllers.login import Login
    
app = Index()
login = Login()

app.mount('/login', login)
    
if 'DYNO' in os.environ:
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
else: 
  app.run(host='localhost', port=8000, debug=True, reloader=True)