import os
import shutil

parent_path = r'C:\Users\Hamza\OneDrive\Desktop\Python\pythonProject'
for pyfile in os.listdir(parent_path):
    if pyfile.endswith(".py") and pyfile != "from py to file.py":
        filename = pyfile.replace(".py", "")
        path = os.path.join(parent_path, filename)
        os.mkdir(path)
        print(f"directory {filename} created")
        newPath = shutil.copy(pyfile, path)
        print(f"{pyfile} was sent to path")
        os.remove("".join(pyfile))
