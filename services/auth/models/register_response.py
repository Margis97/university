from pydantic import BaseModel, ConfigDict


class RegisterResponse(BaseModel):
    model_config = ConfigDict(extra='forbid')

    detail: str
