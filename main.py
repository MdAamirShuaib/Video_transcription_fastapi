from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import base64
import docx
import shutil
import sys
import time
import requests
from transcribe import *
from assemblyai_data_extraction import json_data_extraction
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="template")
@app.get('/', response_class=HTMLResponse)
async def file_temp(request: Request):
  return templates.TemplateResponse("webpage.html", {'request': request})


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):

  for i in os.listdir("documents/"):
    os.remove("documents/"+i)

  if "transcribed_docs.zip" in os.listdir():
    os.remove("transcribed_docs.zip")

  for file in files:
    token = "a788369fef274a0393624e2fc7a9a70a"
    fname = file.filename

    tid = upload_file(token,file.file)
    result = {}
    print('starting to transcribe the file: [ {} ]'.format(fname))
    while result.get("status") != 'completed':
        print(result.get("status"))
        result = get_text(token, tid)

        # Handeling Errors
        if result.get("status") == 'error':
          shutil.make_archive("transcribed_docs","zip","documents")
          return FileResponse("transcribed_docs.zip")

    df = json_data_extraction(result,fname)
    print('saving transcript...')

    df = df[['spcode','utter']]

    print('Converting files')

    # open an existing document
    doc = docx.Document()

    # add a table to the end and create a reference variable
    # extra row is so we can add the header row
    t = doc.add_table(df.shape[0]+1, df.shape[1])

    # add the header rows.
    for j in range(df.shape[-1]):
        t.cell(0,j).text = df.columns[j]

    # add the rest of the data frame
    for i in range(df.shape[0]):
        for j in range(df.shape[-1]):
            t.cell(i+1,j).text = str(df.values[i,j])

    print('saving transcript...')
    doc.save("documents/"+fname+".docx")

  shutil.make_archive("transcribed_docs","zip","documents")


  return FileResponse("transcribed_docs.zip")
