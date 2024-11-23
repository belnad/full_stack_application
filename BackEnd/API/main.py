# main.py


from dotenv import load_dotenv # type: ignore
from .routers import router #type: ignore
from fastapi.middleware.cors import CORSMiddleware
import json
from .database import Base, engine
from starlette_exporter import PrometheusMiddleware, handle_metrics
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from keycloak import KeycloakOpenID
from fastapi import Request
from fastapi.responses import JSONResponse



load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="SecurityNorms API",
    description="Here you can find all existing standards for cybersecurity for each country in the world",
    version="0.0.1",
)

origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Initialiser l'application FastAPI
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# Ajouter le router
app.include_router(router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/realms/newRealm/protocol/openid-connect/token")


keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/",
                                 client_id="newClient",
                                 realm_name="newRealm",
                                 client_secret_key="JcMOVoxxRtdrS1E0bmvERYjnhr2NXQHf")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user_info = keycloak_openid.introspect(token)
        if not user_info.get("active"):
            raise HTTPException(status_code=401, detail="Token is not active")
        return user_info
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

# Route protégée nécessitant une authentification
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        user_info = keycloak_openid.userinfo(token)
        return {"message": f"Hello, {user_info['preferred_username']}"}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")
    
    try:
        token = keycloak_openid.token(grant_type="authorization_code",
                                      code=code,
                                      redirect_uri="http://localhost:3000/callback")
        return JSONResponse({"access_token": token.get("access_token")})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

