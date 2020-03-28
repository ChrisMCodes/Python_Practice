def create_python_script(filename):
  '''can be executed to create a new python script in the current directory. Returns file size'''
  import os
  shebang = "#!/usr/bin/env python3"
  with open(filename, "w") as file:
    add_stuff = file.write(shebang)
  filesize = os.path.getsize(filename) 
  return(filesize)


