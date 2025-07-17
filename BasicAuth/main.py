from fastapi import FastAPI ,Depends ,HTTPException ,status
from fastapi.security import HTTPBasic ,HTTPBasicCredentials
from typing import Annotated
from config import settings
import bcrypt

app = FastAPI()
auth = HTTPBasic()

username = settings.USERNAME
password = settings.PASSWORD

# Hashing The Password using Bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8') , bcrypt.gensalt())

@app.get('/')
async def sensitive_info(credentials: Annotated[HTTPBasicCredentials , Depends(auth)]):
    check_match = bcrypt.checkpw(
        credentials.password.encode('utf-8'),
        hashed_password 
    )

    if credentials.username == username and check_match:
        return {'body' : 'access granted'}

    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail= "wrong login credentials"
    )