#config.py
import sys, asyncio
from models import lesson

if sys.platform == 'win32':
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def setLesson(kdict):
  practice = []
  for v in range(8):
    practice += lesson.__dict__['lesson'+str(v+1)]

  kdict['lesson'] = practice

kdict = {}
kdict['blogTitle'] = "រៀន​វាយ​អក្សរ​ខ្មែរ"
kdict['KhmerNumber'] = {0:'០', 1:'១', 2:'២', 3:'៣', 4:'៤', 5:'៥', 6:'៦', 7:'៧', 8:'៨', 9:'៩'}
kdict['KhmerMonth'] =  ['មករា', 'កុម្ភៈ', 'មិនា', 'មេសា', 'ឧសភា', 'មិថុនា', 'កក្កដា', 'សីហា', 'កញ្ញា', 'តុលា', 'វិច្ឆិកា', 'ធ្នូ']
kdict['message'] = ''
kdict['user'] = ('ភ្ញៀវ', 'អត់មាន', 1, 'អត់មាន')
kdict['secretKey'] = 'h4!#au%8tb_9@oe+c0te=g=u%cfxb8t8fy%7+(gx2+51!t*b+s'

setLesson(kdict)