import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
import io
from googleapiclient.errors import HttpError

scope = ['https://www.googleapis.com/auth/drive']
service_account_json_key = 'credentials.json'
credentials = service_account.Credentials.from_service_account_file(
                              filename = service_account_json_key, 
                              scopes = scope)
service = build('drive', 'v3', credentials = credentials)

# Call the Drive v3 API
results = service.files().list(pageSize = 1000,
                               fields = 'nextPageToken, files(id, name, mimeType, size, modifiedTime)', 
                               q = 'name contains "FantaSbori_Mercato.xlsx"').execute()
# get the results
items = results.get('files', [])

print(items)

request_file = service.files().get_media(fileId = 'FantaSbori_Mercato.xlsx')


# file = io.BytesIO()
# downloader = MediaIoBaseDownload(file, request_file)
# done = False
# while done is False:
#     status, done = downloader.next_chunk()
#     print(F'Download {int(status.progress() * 100)}.')




# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()

# drive = GoogleDrive(gauth)