import csv
import uuid
from pathlib import Path
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()
UPLOAD_DIR = Path("./csv")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/upload")
async def upload_csv(file: UploadFile):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Nur CSV-Dateien sind erlaubt")

    if file.size == 0:
        raise HTTPException(status_code=400, detail="Die hochgeladene Datei ist leer (0 Bytes).")

    file_id = f"{uuid.uuid4()}_{file.filename}"
    file_path = UPLOAD_DIR / file_id

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    return {"message": "Datei gespeichert", "filename": file_id}


@app.get("/files")
def list_files():
    files = [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]
    return {"files": files}

@app.get("/files/{filename}")
def get_file(filename: str):
    safe_filename = Path(filename).name
    file_path = UPLOAD_DIR / safe_filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Datei wurde nicht gefunden.")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        dialect = csv.Sniffer().sniff(content[:1024])
        f.seek(0)

        reader = csv.reader(f, dialect=dialect)
        headers = next(reader)
        data = list(reader)

    return {"headers": headers, "data": data}
@app.get("/")
def get_frontend():
    return FileResponse("templates/index.html")