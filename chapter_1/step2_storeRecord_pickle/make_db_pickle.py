from initdata import db
import pickle

dbfile = open('people-pickle', 'wb') # binarymode file
pickle.dump(db, dbfile)
dbfile.close()
