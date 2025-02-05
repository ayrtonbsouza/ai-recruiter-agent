from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

service = build("drive", "v3",credentials=credentials)

# Folder Id: 1fUo7o5Pnmvi5CkbFXsaV_o5PJHN3XwkK

folder_id = "1fUo7o5Pnmvi5CkbFXsaV_o5PJHN3XwkK"

results = (
  service.files()
  .list(
    q=f"'{folder_id}' in parents",
    fields='files(id, name)'
  ).execute()
)

files = results.get("files", [])

if not files:
  print("No files found.")
else:
  for file in files:
    requests = service.files().get_media(fileId=file["id"])
    file_path = f"./curriculums/{file['name']}"
    with open(file_path, "wb") as file:
      downloader = MediaIoBaseDownload(file, requests)
      done = False
      while not done:
        status, done = downloader.next_chunk()
