
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  
upload_file_list = ["C:\Users\cheta\Desktop\black.jpg"]
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': }]})
	gfile.SetContentFile(upload_file)
	gfile.Upload() 
