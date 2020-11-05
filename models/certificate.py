#models/certificate.py
from string import Template

class Certificate(Template):
  def __init__(self):
    return super().__init__(template)


template = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Title</title>
    
    <style>
    /*Your css code here*/
    </style>
    <script>
    //Your JavaScript code here
    </script>
  </head>
  <body>
    <p>ជំរាបសួ</p>
  </body>
</html>
'''