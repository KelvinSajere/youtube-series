import subprocess
from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/ping")
def ping(ip: str = Query(...)):

    output = subprocess.getoutput(f"ping -c 1 {ip}")
    return {"result": output}
