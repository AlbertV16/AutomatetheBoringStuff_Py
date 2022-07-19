import os

os.chdir('d:\\albert\\python')

for filename in os.listdir():
    if filename.endswith('txt'):
        # os.unlink(filename) # comment out to do dry run before deleting
        print(filename)
