from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
gauth = GoogleAuth()
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
path = r"C:\User\file"   
for i in os.listdir(path):
   
    fil = drive.CreateFile({'title': i})
    fil.SetContentFile(os.path.join(path, i))
    fil.Upload()
    fil = None