from fastapi import FastAPI

app = FastAPI()

token=object

@app.get('/auth_data')
async def auth_data(username:str, password:str):
    pass

