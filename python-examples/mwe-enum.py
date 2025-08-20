from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import json


class TLPEnum(str, Enum):
    CLEAR = "clear"
    GREEN = "green"
    AMBER = "amber"
    AMBER_STRICT = "amber+strict"
    RED = "red"


class MyModel(BaseModel):
    log_level: Optional[TLPEnum] = Field(
        alias="CONNECTOR_LOG_LEVEL",
        default="error",
        description="Determines the verbosity of the logs.",
    )

    @field_validator("log_level", mode="before")
    @classmethod
    def normalize_log_level(cls, v):
        if isinstance(v, str):
            v = v.lower()
        if v is None:
            return v
        try:
            return TLPEnum(v)
        except ValueError:
            raise ValueError(f"{v!r} is not a valid TLP value")


m = MyModel(log_level="GREEN")  # Works, normalized to "green"
print(m.log_level)  # TLPEnum.GREEN
print(json.dumps(MyModel.model_json_schema(), indent=2))  # Shows enum for log_level