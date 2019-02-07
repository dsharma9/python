#!/usr/bin/env  python3.7

import sys
import time
import os
print("Printint  the file name using two methode. \n 1. By calling sys.argv[0]. \n 2. By calling os.path.basename().")

time.sleep(1)

print(f"The file name using 1st methode is {sys.argv[0]}")
time.sleep(1)

print("The file name using 2nd methode is " + os.path.basename('argv.py'))

