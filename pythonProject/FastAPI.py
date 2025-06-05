from fastapi import FastAPI, UploadFile, File, Form
from typing import List
import uvicorn
from Visual import return_graphs

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
            results.append({"filename": file.filename, "status": "success","result" : result})
        except Exception as e:
            results.append({"filename": file.filename, "status": "error", "message": str(e)})
    return results

@app.post("/alerts")
async def alerts(file):
    return
if __name__ == "__main__":
    uvicorn.run("FastAPI:app",host="127.0.0.1",port=8000,reload=True)

