import random, os
from google.cloud import storage

def upload_file(file):
    filename, file_extension = os.path.splitext(file.filename)

    storage_client = storage.Client()
    bucket = storage_client.get_bucket('cosmos-369.appspot.com')

    file_name = 'wedday/' + str(random.getrandbits(128)) + file_extension
    blob = bucket.blob(file_name)
    blob.upload_from_string(
        file.read(),
        content_type = file.content_type
    )

    blob.make_public()
    return file_name

def storeIntoDB(data):
    return data

# 驗證參數
def valid_param(form, columns):
    for column in columns:
        if column not in form:
            return False

        if not form[column].strip():
            return False

    return True


