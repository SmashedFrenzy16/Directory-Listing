import os

for name in os.listdir('.'):
  
  if os.path.isfile(name):
    
    print("File: ")
  
  elif os.path.isdir(name):
    
    print("Directory: ")
    
  elif os.path.islink(name):
    
    print("Link: ")
    
  else:
    
    print("Unknown: {}".format(name))
