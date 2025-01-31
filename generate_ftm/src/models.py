from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal, ClassVar, Any
from datetime import date, datetime
from pydantic.json import timedelta_isoformat


class EntityType(Enum):
    vessel = "vessel"
    person = "person"
    organization = "organization"
    company = "company"
    aircraft = "aircraft"


class ListedEntity(BaseModel):
    """An entity that is listed on a sanction list, often with aliases and other information, and a reason for listing"""

    individual_id: Optional[int] = Field(default=None, init=False)
    entity_counter: ClassVar[int] = 0
    entity_type: EntityType = Field(description="type of entity")
    name: str = Field(description="name of entity")

    event_type: Optional[Literal["listing", "delisting"]] = Field(
        default=None,
        description="Whether this entity is said to be added or removed from the list",
    )
    event_reason: Optional[str] = Field(
        default=None,
        description=(
            "A single phrase that compeletes this sentence: 'The stated reason for including this entity on the list is ...'"
            "If there is no stated reason, return None. A date or location is not a reason."
        ),
    )
    event_date: Optional[date] = Field(
        default=None, description="date of the listing or delisting of the entity"
    )
    legal_base: Optional[str] = Field(
        default=None,
        description=(
            "the legal texts referred to; amended or corrected, Be precise, and if you don't know, don't say anything."
            "The legal base should be a single phrase that compeletes this sentence: 'The listing authority included in this entity because it ...'"
        ),
    )

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            date: lambda d: d.isoformat() if d else None,
            datetime: lambda dt: dt.isoformat() if dt else None,
        },
    )

    def model_post_init(self, __context: Any) -> None:
        self.individual_id = self.__class__.entity_counter
        self.__class__.entity_counter += 1


class AdditionalInfo(BaseModel):
    address: Optional[str] = Field(
        default=None, description="adress(es) associated with the entity"
    )
    telephone: Optional[str] = Field(default=None, description="telephone associated")
    email: Optional[str] = Field(default=None, description="email associated")
    website: Optional[str] = Field(default=None, description="website associated")
    associated_individual: Optional[str] = Field(
        default=None, description="associated ownership"
    )
    associated_other: Optional[str] = Field(
        default=None, description="other associated entities like governments etc"
    )
    aliases: Optional[list[str]] = Field(default=None, description="aliases for entity")


class PersonAdditionalInfo(BaseModel):
    """Additional information about the entity, to be added to the entity on a separate run."""

    nationality: Optional[str] = Field(default=None, description="nationality")
    gender: Optional[Literal["m", "f", "d"]] = Field(
        default=None, description="gender of the person"
    )
    passport_id: Optional[int] = Field(default=None, description="id of passport")
    DOB: Optional[date] = Field(default=None, description="date of birth")
    POB: Optional[str] = Field(default=None, description="place of birth")
    citizenship: Optional[str] = Field(default=None, description="citizenship")


class CompanyAdditionalInfo(BaseModel):
    business_id: Optional[str] = Field(default=None, description="business id")
    place_registry: Optional[str] = Field(
        default=None,
        description="place the entity is registered if a business of company",
    )
    """
    iso_nationality: Optional[str] = Field(
        default=None,
        description="iso 3 codes created from address, citizenship and registry country names",
    )
    iso_citizenship: Optional[str] = Field(
        default=None,
        description="iso 3 codes created from address, citizenship and registry country names",
    )
    iso_pob: Optional[str] = Field(
        default=None,
        description="iso 3 codes created from address, citizenship and registry country names",
    )
    iso_registry: Optional[str] = Field(
        default=None,
        description="iso 3 codes created from address, citizenship and registry country names",
    )
    iso_address: Optional[str] = Field(
        default=None,
        description="iso 3 codes created from address, citizenship and registry country names",
    )
    """
