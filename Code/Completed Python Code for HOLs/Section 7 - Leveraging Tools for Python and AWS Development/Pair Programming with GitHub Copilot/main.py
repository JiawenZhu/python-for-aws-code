import os
import boto3
from datetime import datetime

def upload_files_to_s3(bucket, bucket_subfolder, files):
    s3 = boto3.client('s3')

    try:
        for file in files:
            local_file_path = f'../units-sold/{file}'

            file = append_date_to_filename(file)

            s3.upload_file(local_file_path, bucket, f'{bucket_subfolder}/{file}')
            print(f'File {file} uploaded to s3://{bucket}/{bucket_subfolder}/{file}')
    except Exception as e:
        print('Error uploading files to S3')
        raise e

def append_date_to_filename(file):
    # Get current date
    date = datetime.today().strftime('%Y-%m-%d')

    # Split filename and extension
    filename, extension = os.path.splitext(file)

    # Append date to filename
    filename = f'{filename}_{date}'

    # Join filename and extension
    file = f'{filename}{extension}'

    return file

if __name__ == '__main__':
    bucket = 'YOUR-BUCKET-NAME'
    bucket_subfolder = 'units-sold'

    # If the ../units-sold folder has files print a message
    if os.listdir('../units-sold'):
        print('Files found in ../units-sold folder')
        units_sold_files = os.listdir('../units-sold')

        # Upload files to s3
        upload_files_to_s3(bucket, bucket_subfolder, units_sold_files)

    else:
        print('No files found in ../units-sold folder')