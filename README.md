# Django File Management System with AWS S3 Integration

This is a simple Django-based file management system that allows users to upload, organize, and download files. It provides features like user authentication, file upload, file listing, and file download, with integration to AWS S3 for file storage.

## Features

- **User Authentication:** Users can sign up, log in, and log out to access the file management system. Only authenticated users can upload and download files.
- **File Upload:** Authenticated users can upload files to the system.
- **File Listing:** Users can view a list of files they have uploaded.
- **File Download:** Users can download files they have uploaded.

## Installation

1. Create and Activate Virtual Environment:
   -python3 -m venv env
   -source env/bin/activate


2. Clone the repository:
   -git clone https://github.com/kksain/File_Management.git
   -cd core

3. Install dependencies:
  -pip install -r requirements.txt

4. Set up database migrations:
  -python manage.py makemigrations
  -python manage.py migrate

5. Set up AWS S3:
   - Create an AWS account if you don't have one already.
   - Create an S3 bucket to store the uploaded files.
   - Configure AWS credentials (access key and secret key) either using environment variables or AWS CLI.
   - Update `settings.py` file with your AWS S3 bucket name and credentials.


6. Run the development server:
   -python manage.py runserver
