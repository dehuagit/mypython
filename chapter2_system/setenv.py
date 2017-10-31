import os
print('setenv...', end=' ')
print(os.environ['USER']) # show current shell variable value


os.environ['USER'] = 'Brian'   # runs os.putenv behind the scenes
os.system('python echoenv.py')


os.environ['USER'] = 'Author'
os.system('python echoenv.py')




