#config.py
import sys, asyncio

if sys.platform == 'win32':
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

kdict = {}
kdict['blogTitle'] = "រៀន​វាយ​អក្សរ​ខ្មែរ"
kdict['KhmerNumber'] = {0:'០', 1:'១', 2:'២', 3:'៣', 4:'៤', 5:'៥', 6:'៦', 7:'៧', 8:'៨', 9:'៩'}
kdict['message'] = ''