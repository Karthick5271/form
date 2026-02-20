from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from .forms import FileUploadForm
from .google_services import GoogleServiceManager


class FileUploadView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'uploader/upload.html', {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                # Get form data
                name = form.cleaned_data['name']
                employee_id = form.cleaned_data['employee_id']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                
                # Initialize Google services
                google_service = GoogleServiceManager()
                
                # Check for duplicate ID in Google Sheet
                sheet_data = google_service.get_sheet_data()
                for row in sheet_data[1:]:  # Skip header
                    if len(row) > 2 and row[2] == employee_id:
                        messages.error(request, f'Employee ID {employee_id} already exists!')
                        return render(request, 'uploader/upload.html', {'form': form})
                
                # Upload PDF to Drive
                file_url = 'No File'
                pdf_file = request.FILES.get('file')
                if pdf_file:
                    file_id, file_link = google_service.upload_to_drive(pdf_file, pdf_file.name)
                    file_url = f'=HYPERLINK("{file_link}", "{pdf_file.name}")'
                
                # Upload photos to Drive
                photos_url = 'No Photos'
                photos = request.FILES.getlist('photos')
                if photos:
                    if len(photos) > 5:
                        messages.error(request, 'Maximum 5 photos allowed!')
                        return render(request, 'uploader/upload.html', {'form': form})
                    
                    # Create photo folder
                    folder_name = f"{name}_Photos_{employee_id}"
                    folder_id, folder_url = google_service.create_photo_folder(folder_name)
                    
                    # Upload each photo
                    for photo in photos:
                        if photo.size > 5 * 1024 * 1024:  # 5MB
                            messages.error(request, 'Each photo must be less than 5MB!')
                            return render(request, 'uploader/upload.html', {'form': form})
                        google_service.upload_photo_to_folder(photo, photo.name, folder_id)
                    
                    photos_url = f'=HYPERLINK("{folder_url}", "View Photos")'
                
                # Add to Google Sheet ONLY (no database save)
                sheet_data = {
                    'timestamp': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'name': name,
                    'employee_id': employee_id,
                    'phone': phone,
                    'address': address,
                    'file_url': file_url,
                    'photos_url': photos_url
                }
                google_service.add_to_sheet(sheet_data)
                
                messages.success(request, 'Employee added successfully!')
                return redirect('list')
                
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
                return render(request, 'uploader/upload.html', {'form': form})
        
        return render(request, 'uploader/upload.html', {'form': form})


class FileListView(View):
    def get(self, request):
        try:
            google_service = GoogleServiceManager()
            sheet_data = google_service.get_sheet_data()
            
            # Get all files from Drive folder
            drive_files = google_service.get_drive_files_map()
            print(f"DEBUG: Found {len(drive_files)} files in Drive")
            
            # Debug: Print raw sheet data
            print(f"DEBUG: Total rows from Sheet: {len(sheet_data)}")
            for i, row in enumerate(sheet_data[:5]):  # Print first 5 rows
                print(f"DEBUG Row {i}: {row} (length: {len(row)})")
            
            # Skip header row
            employees = []
            if len(sheet_data) > 1:
                # Count duplicate IDs - check ALL rows
                id_counts = {}
                for row in sheet_data[1:]:
                    if len(row) > 2 and row[2]:  # Has ID column and ID is not empty
                        emp_id = row[2]
                        id_counts[emp_id] = id_counts.get(emp_id, 0) + 1
                
                print(f"DEBUG: ID counts: {id_counts}")
                
                # Track occurrence number for each ID
                id_occurrences = {}
                
                for row in sheet_data[1:]:
                    # Handle rows with ANY data (even if just 1 column)
                    if len(row) > 0:
                        # Get all data with safe defaults
                        timestamp = row[0] if len(row) > 0 else ''
                        name = row[1] if len(row) > 1 else ''
                        emp_id = row[2] if len(row) > 2 else ''
                        phone = row[3] if len(row) > 3 else ''
                        address = row[4] if len(row) > 4 else ''
                        file_data = row[5] if len(row) > 5 else 'No File'
                        photos_data = row[6] if len(row) > 6 else 'No Photos'
                        
                        # Only process if we have at least an ID
                        if emp_id:
                            is_duplicate = id_counts.get(emp_id, 0) > 1
                            
                            # Track occurrence number
                            if is_duplicate:
                                id_occurrences[emp_id] = id_occurrences.get(emp_id, 0) + 1
                                occurrence = id_occurrences[emp_id]
                            else:
                                occurrence = None
                            
                            # Extract file info and match with Drive files
                            file_url = None
                            file_name = 'No File'
                            download_url = None
                            
                            if file_data and file_data != 'No File':
                                # Extract filename from HYPERLINK formula or use as-is
                                import re
                                name_match = re.search(r'"([^"]+)"[^"]*$', file_data)
                                if name_match:
                                    file_name = name_match.group(1)
                                else:
                                    file_name = file_data
                                
                                # Try to find file in Drive by name
                                if file_name in drive_files:
                                    file_info = drive_files[file_name]
                                    file_url = file_info['webViewLink']
                                    download_url = file_info.get('webContentLink', file_url)
                                    print(f"DEBUG: Matched file '{file_name}' with URL: {file_url}")
                            
                            # Extract photos folder info
                            photos_url = None
                            photos_name = 'No Photos'
                            
                            if photos_data and photos_data != 'No Photos':
                                # Extract folder name from HYPERLINK formula
                                name_match = re.search(r'"([^"]+)"[^"]*$', photos_data)
                                if name_match:
                                    photos_name = name_match.group(1)
                                else:
                                    photos_name = photos_data
                                
                                # Try to find folder in Drive by name
                                folder_name = f"{name}_Photos_{emp_id}"
                                if folder_name in drive_files:
                                    folder_info = drive_files[folder_name]
                                    if folder_info['isFolder']:
                                        photos_url = folder_info['webViewLink']
                                        print(f"DEBUG: Matched folder '{folder_name}' with URL: {photos_url}")
                            
                            employees.append({
                                'timestamp': timestamp,
                                'name': name,
                                'employee_id': emp_id,
                                'phone': phone,
                                'address': address,
                                'file': file_name,
                                'file_url': file_url,
                                'download_url': download_url,
                                'file_name': file_name,
                                'photos': photos_name,
                                'photos_url': photos_url,
                                'photos_folder_id': drive_files.get(f"{name}_Photos_{emp_id}", {}).get('id'),
                                'is_duplicate': is_duplicate,
                                'occurrence': occurrence,
                                'total_duplicates': id_counts.get(emp_id, 0) if is_duplicate else None
                            })
                        else:
                            print(f"DEBUG: Skipping row with no ID: {row}")
            
            return render(request, 'uploader/list.html', {'employees': employees})
            
        except Exception as e:
            messages.error(request, f'Error loading data: {str(e)}')
            return render(request, 'uploader/list.html', {'employees': []})



class GetPhotosView(View):
    def get(self, request, folder_id):
        try:
            from django.http import JsonResponse
            google_service = GoogleServiceManager()
            
            # Get files from folder
            results = google_service.drive_service.files().list(
                q=f"'{folder_id}' in parents and mimeType contains 'image/'",
                fields='files(id, name, webViewLink, thumbnailLink)',
                pageSize=100
            ).execute()
            
            photos = results.get('files', [])
            
            return JsonResponse({'photos': photos})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
