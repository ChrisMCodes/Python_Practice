#!/usr/bin/env python3

# borrowed from the Google IT Automation course

def new_directory(directory, filename):
  '''checks if the specified directory exists, creates it if not, and places the desired file in it. Returns contents of directory'''
  # before creating a new directory, checks to see if it already exists
  exists = os.path.isdir(directory)
  # creates it if not
  if not exists:
    os.mkdir(directory)
  # creates the new file inside of the new directory
  os.chdir(directory)
  with open(filename, "w") as file:
    message = input("What would you like to write to the file? ")
    new_file = file.write(message)
  # returns to the cwd
  os.chdir("..")
  # returns the list of files in the new directory
  return os.listdir(directory)
