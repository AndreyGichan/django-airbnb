from supabase import create_client, Client
from uuid import uuid4
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
BUCKET_NAME = os.environ.get("SUPABASE_BUCKET_NAME", "images")

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise RuntimeError("Supabase credentials are missing")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


def upload_image_to_supabase(file, filename: str) -> str:
    ext = filename.rsplit(".", 1)[-1].lower()
    unique_name = f"{uuid4()}.{ext}"

    file_data = file.read()
    supabase.storage.from_(BUCKET_NAME).upload(unique_name, file_data)

    return supabase.storage.from_(BUCKET_NAME).get_public_url(unique_name)
