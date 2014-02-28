import bottle
import pymongo

@bottle.route('/')
def index():
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.test
    name = db.names
    item = name.find_one()
    return '<b>Hello %s!</b>' % item['nombre'].upper()
    
bottle.run(host='localhost', port=8080)