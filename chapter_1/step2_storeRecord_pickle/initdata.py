#initialize dta to be store in files, pickles, shelves

# records
bob={'name':'Bob Smith', 'age':42, 'pay': 300, 'job': ('dev','wirte')}
sue={'name': 'Sue Jon', 'age': 45, 'pay':400, 'job':'hw'}
tom={'name': 'tom', 'age': 50, 'pay':00, 'job':None}

#dababase
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] =   tom



if __name__ == '__main__':
	for key in db:
		print(key, '=>\n', db[key])





