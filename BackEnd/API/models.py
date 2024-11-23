# models.py

import enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, TIMESTAMP, text, Text # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .database import Base
from dotenv import load_dotenv # type: ignore
import os


load_dotenv()  # Charge le fichier .env
# `users` tables's model
class RoleUser(enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50))
    email = Column(String(100), unique=True)
    password_hash = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=True)
    role = Column(Enum(RoleUser), default=RoleUser.user, nullable=True)


# `Countries` tables's model
class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country_name = Column(String(150), index=True)
    iso_code = Column(String(3), unique=True, index=True)


# `organization` tables's model
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organization_name = Column(String(150), index=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", nullable=True)

# `security_standards` tables's model
class SecurityStandard(Base):
    __tablename__ = "security_standards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    standard_name = Column(String(150), index=True)
    description = Column(Text, nullable=True)
    year = Column(Integer, index=True, nullable=True)
    type = Column(Text, index=True, nullable=True)
    organisationId = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    organization = relationship("Organization")

# `Organization_standard` tables's model
class OrganizationStandard(Base):
    __tablename__ = "organization_standard"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organisation_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    standard_id = Column(Integer, ForeignKey("security_standards.id"), nullable=True)

    organization = relationship("Organization")
    security_standard = relationship("SecurityStandard")

# `Country_standard` tables's model
class CountryStandard(Base):
    __tablename__ = "country_standards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=True)
    standard_id = Column(Integer, ForeignKey("security_standards.id"), nullable=True)

    countries = relationship("Country")
    security_standard = relationship("SecurityStandard")