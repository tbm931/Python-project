from fastapi import FastAPI, UploadFile, File, Form
from typing import List
import uvicorn

from Visual import return_graphs, return_issues

app = FastAPI()

@app.post("/analyze")
async def analyze(files: List[UploadFile] = File(...),path: str = Form("")):
    file_data_list = []
    results = []
    for file in files:
        contents = await file.read()
        code = contents.decode('utf-8')
        filename = file.filename
        file_data_list.append((code, filename))
    try:
        result = return_graphs(file_data_list,path)
        results.append({"status": "success","result" : result})
    except Exception as e:
        results.append({"status": "error", "message": str(e)})
    return results

@app.post("/alerts")
async def alerts(files: List[UploadFile] = File(...)):
    file_data_list = []
    results = []
    for file in files:
        contents = await file.read()
        code = contents.decode('utf-8')
        filename = file.filename
        file_data_list.append((code, filename))
    for (co,filen) in file_data_list:
        try:
            message = return_issues(co,filen)
            results.append((filen,message))
        except Exception as e:
            return f"There is an error in file: {filename}. the error is: {e}"
    return results
if __name__ == "__main__":
    uvicorn.run("FastAPI:app",host="127.0.0.1",port=8000,reload=True)

