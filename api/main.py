from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Multi-Agent Temporal Template"}

@app.post("/run")
def run():
    return {"workflow_id":"demo-001","status":"started"}
