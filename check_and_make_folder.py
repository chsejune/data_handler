## check folder from the path and if it does not exist make folder

## tested in python3

## example
import os

path = "result"
if not os.path.exists(path):
	os.mkdir(path)




