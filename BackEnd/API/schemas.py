# schemas.py
from pydantic import BaseModel, Field, EmailStr # type: ignore
from typing import Optional, List, Literal
from datetime import datetime
from uuid import uuid4
from typing_extensions import Annotated # type: ignore


# `users` tables's schema
class UserBase(BaseModel):
    
    username: str
    email: EmailStr
    role: Optional[Literal['admin', 'user']] = 'user'

class UserRead(UserBase):
    pass

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: Optional[int]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True


# `countries` tables's schema
class CountryBase(BaseModel):
    country_name: str
    iso_code: str
    

class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase):
    pass

class Country(CountryBase):
    id: Optional[int]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True


# `Country_standards` tables's schema
class CountryStandardBase(BaseModel):
    country_id: int
    standard_id: int

class CountryStandardRead(CountryStandardBase):
    pass    

class CountryStandardCreate(CountryStandardBase):
    pass

class CountryStandard(CountryStandardBase):
    id: Optional[int]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True


# # `organization_standards` tables's schema
class OrganizationStandardBase(BaseModel):
    organization_id: int
    standard_id: int

class OrganizationStandardRead(OrganizationStandardBase):
    pass

class OrganizationStandardCreate(OrganizationStandardBase):
    pass

class OrganizationStandard(OrganizationStandardBase):
    id: Optional[int]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True


# # `organizations` tables's schema
class OrganizationBase(BaseModel):
    organization_name: str
    country_id: int
    description: Optional[str]

class OrganizationRead(OrganizationBase):
    pass

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True


# `security_standards` tables's schema
class SecurityStandardBase(BaseModel):
    standard_name: str
    description: Optional[str] = None
    year: Optional[int]
    type: Optional[str]
    OrganizationId: Optional[int]

class SecurityStandardRead(SecurityStandardBase):
    pass

class SecurityStandardCreate(SecurityStandardBase):
    pass

class SecurityStandard(SecurityStandardBase):
    id: Optional[int]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True