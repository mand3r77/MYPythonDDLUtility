import os

path= 'c:/fuck/this/test/app/shit'
try:
    os.makedirs(path)
except OSError as exc:  # Python >2.5
    if  not exc.errno:
        print("pass")
    else:
        print('failure')
        raise
    
