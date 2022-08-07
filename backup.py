import os
import time
import shutil
import sys


# ver ultima modificacao de um arquivo
def last_modified(path):
    return time.ctime(os.path.getmtime(path))



