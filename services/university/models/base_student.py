from pydantic import BaseModel, ConfigDict, EmailStr


class DegreeEnum:
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DOCTORATE = "Doctorate"


class BaseStudent(BaseModel):
    model_config = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
    help(ConfigDict)

    first_name: str
    last_name: str
    email: EmailStr
    degree: DegreeEnum
    phone: str
    group_id: int
