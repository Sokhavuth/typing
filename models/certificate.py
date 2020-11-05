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
    <title>លិខិតបញ្ជាក់សមត្ថភាព</title>
    
    <style>
    #site img{
      width: 100%;
    }
    </style>
    
  </head>
  <body>
    <div id="site">
    <img src="https://1.bp.blogspot.com/-8jdjiuIHskY/X6PstG7tj4I/AAAAAAABqrQ/qejGd8RDwiU0GDWzswRJZbZ38igY8koBQCLcBGAsYHQ/s0/pyproject.png" />
    </div>
  </body>
</html>
'''