from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
from django.conf import settings
import io
import os
import pickle


class GoogleServiceManager:
    def __init__(self):
        SCOPES = [
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/spreadsheets'
        ]
        
        creds = None
        token_file = settings.BASE_DIR / 'token.pickle'
        
        # Load saved credentials
        if os.path.exists(token_file):
            with open(token_file, 'rb') as token:
                creds = pickle.load(token)
        
        # If no valid credentials, authenticate
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    settings.GOOGLE_CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials
            with open(token_file, 'wb') as token:
                pickle.dump(creds, token)
        
        self.creds = creds
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        self.sheets_service = build('sheets', 'v4', credentials=self.creds)

    def upload_to_drive(self, file_obj, filename):
        """Upload file to Google Drive"""
        file_metadata = {
            'name': filename,
            'parents': [settings.GOOGLE_DRIVE_FOLDER_ID]
        }
        
        media = MediaIoBaseUpload(
            io.BytesIO(file_obj.read()),
            mimetype=file_obj.content_type,
            resumable=True
        )
        
        file = self.drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        
        # Make file publicly accessible
        self.drive_service.permissions().create(
            fileId=file['id'],
            body={'type': 'anyone', 'role': 'reader'}
        ).execute()
        
        return file['id'], file['webViewLink']

    def create_photo_folder(self, folder_name):
        """Create a folder in Google Drive for photos"""
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [settings.GOOGLE_DRIVE_FOLDER_ID]
        }
        
        folder = self.drive_service.files().create(
            body=file_metadata,
            fields='id, webViewLink'
        ).execute()
        
        # Make folder publicly accessible
        self.drive_service.permissions().create(
            fileId=folder['id'],
            body={'type': 'anyone', 'role': 'reader'}
        ).execute()
        
        return folder['id'], folder['webViewLink']

    def upload_photo_to_folder(self, photo_obj, filename, folder_id):
        """Upload photo to specific folder in Google Drive"""
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        
        media = MediaIoBaseUpload(
            io.BytesIO(photo_obj.read()),
            mimetype=photo_obj.content_type,
            resumable=True
        )
        
        file = self.drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        return file['id']

    def add_to_sheet(self, data):
        """Add data to Google Sheet"""
        values = [[
            data['timestamp'],
            data['name'],
            data['employee_id'],
            data['phone'],
            data['address'],
            data['file_url'],
            data['photos_url']
        ]]
        
        body = {'values': values}
        
        self.sheets_service.spreadsheets().values().append(
            spreadsheetId=settings.GOOGLE_SHEET_ID,
            range='Sheet1!A:G',
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

    def get_sheet_data(self):
        """Get all data from Google Sheet"""
        result = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=settings.GOOGLE_SHEET_ID,
            range='Sheet1!A:G'
        ).execute()
        
        return result.get('values', [])

    def get_drive_files_map(self):
        """Get all files from Drive folder and create a mapping by name"""
        files_map = {}
        
        try:
            # Get all files from the main folder
            results = self.drive_service.files().list(
                q=f"'{settings.GOOGLE_DRIVE_FOLDER_ID}' in parents",
                fields='files(id, name, webViewLink, webContentLink, mimeType)',
                pageSize=1000
            ).execute()
            
            files = results.get('files', [])
            
            for file in files:
                files_map[file['name']] = {
                    'id': file['id'],
                    'webViewLink': file.get('webViewLink', ''),
                    'webContentLink': file.get('webContentLink', ''),
                    'mimeType': file.get('mimeType', ''),
                    'isFolder': file['mimeType'] == 'application/vnd.google-apps.folder'
                }
            
            return files_map
        except Exception as e:
            print(f"Error getting drive files: {e}")
            return {}
