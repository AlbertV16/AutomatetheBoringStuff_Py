import shutil, sys, pyperclip, os

sys.argv # ['third_party_copy.py', 'filename']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['third_party_copy.py', 'filename'] 
    filename = sys.argv[1]
else:
    filename = pyperclip.paste()

shutil.copytree(os.path.join('d:\\Canopy\\User\\Lib\\site-packages', filename), os.path.join('d:\\Albert\\Python\\Lib\\site-packages', filename))
