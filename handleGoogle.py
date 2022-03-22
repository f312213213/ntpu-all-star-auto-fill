import io
import shutil

from firebase_admin import credentials, storage, firestore, initialize_app
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseDownload
from uuid import uuid4
from PIL import Image, ExifTags

SCOPES = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/drive.file']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
drive_service = build('drive', 'v3', credentials=creds)
cred = credentials.Certificate('ntpu-all-star-firebase-adminsdk-yq6fs-cda9dd2d3d.json')
initialize_app(cred, {'storageBucket': 'ntpu-all-star.appspot.com'})
db = firestore.client()


def getSheet():
    print('Downloading response sheets.')
    name = ['bg', 'bb', 'v']
    sheetID = ['1H9LzBL9GPOVCw-yI4tZ8d9Vgw-4L_s1xrPqnWi0_c1A', '1phbjO8N2BIMHYblbdKK0jDWfGJugF4yBRmHf7xh6shQ',
               '1FSxKlCWyavoD9hmStz0S9_smD8m3VAxEcvdl4thuDDc']
    for num in range(0, 3):
        request = drive_service.files().export(fileId=sheetID[num],
                                               mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        fh.seek(0)
        with open(f'{name[num]}.xlsx', 'wb') as f:
            shutil.copyfileobj(fh, f, length=131072)
    print('Got all response sheets.')


def uploadCandidates(player: object, gender: str, sport: str, volleyball_role: str):
    new_token = uuid4()
    downloadGoogleDrivePhoto(player['photoURL'], str(new_token))
    compressPicture(f'{str(new_token)}.jpeg')
    url = uploadPicture(f'{str(new_token)}.jpeg', new_token)
    newCandidateData = {
        'username': str(player['name']),
        'uid': str(new_token),
        'photoURL': str(url),
        'voteCount': 0,
        'introduction': str(player['introduction'])
    }
    if sport == 'basketball':
        doc_ref = db.collection(u'basketball').document(f'{gender}').collection(u'candidates').add(newCandidateData)
        return
    if sport == 'volleyball':
        doc_ref = db.collection(u'volleyball').document(f'{gender}').collection(f'{volleyball_role}').add(
            newCandidateData)
        return


def downloadGoogleDrivePhoto(fileID: str, local_filename: str):
    request = drive_service.files().get_media(fileId=fileID)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    fh.seek(0)
    with open(f'{local_filename}.jpeg', 'wb') as f:
        shutil.copyfileobj(fh, f, length=131072)


def uploadPicture(name: str, new_token: str):
    print(f'Uploading {name}')
    bucket = storage.bucket()
    metadata = {"firebaseStorageDownloadTokens": new_token}

    fileName = name
    blob = bucket.blob(fileName)
    blob.metadata = metadata
    blob.upload_from_filename(fileName)
    blob.make_public()
    return blob.public_url


def compressPicture(name: str):
    print(f'Compressing {name}')
    image = Image.open(name)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation': break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except:
        pass
    image.save(name, quality=65, subsampling=0)
