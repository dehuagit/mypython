from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1000
db['sue'] = sue
db['tom'] = tom
db.close()
