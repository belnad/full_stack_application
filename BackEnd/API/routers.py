# routers.py

from passlib.context import CryptContext; # type: ignore
from fastapi import APIRouter, Depends, HTTPException; # type: ignore
from sqlalchemy.orm import Session; # type: ignore
from . import models, schemas; # type: ignore
from .database import get_db;
from .redisClient import get_cached_data, cache_data, delete_cache
from dotenv import load_dotenv # type: ignore

load_dotenv()

router = APIRouter()

redis_router = APIRouter()


##------------------POST-----------------------------CREATE-------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Function for hash the password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)



# users's router
@router.post("/users/", response_model=schemas.UserRead)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,  # Utilisation du mot de passe hached
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# countries's router
@router.post("/countries/", response_model=schemas.CountryRead)
async def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    db_country = db.query(models.Country).filter(models.Country.country_name == country.country_name).first()
    if db_country:
        raise HTTPException(status_code=400, detail="Country already registered")

    new_country = models.Country(
        country_name=country.country_name,
        iso_code=country.iso_code
    )

    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country


#organizations's router
@router.post("/organizations/", response_model=schemas.OrganizationRead)
async def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    db_organization = db.query(models.Organization).filter(models.Organization.organization_name == organization.organization_name).first()
    if db_organization:
        raise HTTPException(status_code=400, detail="Organization already registered")

    new_organization = models.Organization(
        organization_name=organization.organization_name,
        country_id=organization.country_id,
        description=organization.description
    )

    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    return new_organization


# security_standards's router
@router.post("/security_standards/", response_model=schemas.SecurityStandardRead)
async def create_securityStandard(securityStandard: schemas.SecurityStandardCreate, db: Session = Depends(get_db)):
    db_standard = db.query(models.SecurityStandard).filter(models.SecurityStandard.standard_name == securityStandard.standard_name).first()
    if db_standard:
        raise HTTPException(status_code=400, detail="Security standard already registered")

    new_standard = models.Country(
        country_name=securityStandard.standard_name,
        description=securityStandard.description,
        year=securityStandard.year,
        type=securityStandard.type,
        OrganizationId=securityStandard.OrganizationId
    )

    db.add(new_standard)
    db.commit()
    db.refresh(new_standard)
    return new_standard


# organnization_standard's router
@router.post("/organization_standard/", response_model=schemas.OrganizationStandardRead)
async def create_organizationStandard(organizationStandard: schemas.OrganizationStandardCreate, db: Session = Depends(get_db)):

    new_organizationStandard = models.OrganizationStandard(
        organization_id=organizationStandard.organization_id,
        standard_id=organizationStandard.standard_id
    )

    db.add(new_organizationStandard)
    db.commit()
    db.refresh(new_organizationStandard)
    return new_organizationStandard

# country_standard's router
@router.post("/country_standards/", response_model=schemas.CountryStandardRead)
async def create_countryStandard(countryStandard: schemas.CountryStandardCreate, db: Session = Depends(get_db)):

    new_countryStandard = models.CountryStandard(
        country_id=countryStandard.country_id,
        standard_id=countryStandard.standard_id
    )

    db.add(new_countryStandard)
    db.commit()
    db.refresh(new_countryStandard)
    return new_countryStandard

##----------------------POST-----------------------------------CREATE--------------------------

##----------------------GET------------------------------------READ-----------------------------

@router.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@router.get("/countries/", response_model=list[schemas.Country])
async def read_countries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    country = db.query(models.Country).offset(skip).limit(limit).all()
    return country

@router.get("/organizations/", response_model=list[schemas.Organization])
async def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    organization = db.query(models.Organization).offset(skip).limit(limit).all()
    return organization

@router.get("/security_standards/", response_model=list[schemas.SecurityStandard])
async def read_securityStandards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    standard = db.query(models.SecurityStandard).offset(skip).limit(limit).all()
    return standard

@router.get("/organization_standard/", response_model=list[schemas.OrganizationStandard])
async def read_organizationStandards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    organizationStandards = db.query(models.OrganizationStandard).offset(skip).limit(limit).all()
    return organizationStandards

@router.get("/country_standards/", response_model=list[schemas.CountryStandard])
async def read_countryStandards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    countryStandards = db.query(models.CountryStandard).offset(skip).limit(limit).all()
    return countryStandards


##-----------------GET------------------------------------READ-----------------------------

##-----------------PUT------------------------------------REPLACE-----------------------------

##-----------------PUT------------------------------------REPLACE-----------------------------

##-----------------PATCH------------------------------------READ-----------------------------
##-----------------PATCH------------------------------------READ-----------------------------

##-----------------DELETE------------------------------------REMOVE-----------------------------

##-----------------DELETE------------------------------------REMOVE-----------------------------

##-----------------OPTIONS------------------------------------READ-----------------------------
##-----------------OPTIONS------------------------------------READ-----------------------------

##-----------------HEAD------------------------------------READ-----------------------------
##-----------------HEAD------------------------------------READ-----------------------------

# Road to filter
# Road to search
# Road to restrict
# Road for the authentification
# Exemple d'utilisation dans un endpoint
# routers.py