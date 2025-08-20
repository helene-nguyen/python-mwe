from datetime import timedelta
from pathlib import Path
from typing import Annotated, Literal, Optional

from pydantic import (
    Field,
    HttpUrl,
    PlainSerializer,
    PlainValidator,
    PositiveInt,
    field_validator,
    ValidationError
)

from pydantic_settings import (
    BaseSettings,
    DotEnvSettingsSource,
    EnvSettingsSource,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
    SettingsConfigDict
)

HttpUrlToString = Annotated[HttpUrl, PlainSerializer(str, return_type=str)]
TimedeltaInSeconds = Annotated[
    timedelta, PlainSerializer(lambda v: int(v.total_seconds()), return_type=int)
]
TLPToLower = Annotated[
    Literal["clear", "green", "amber", "amber+strict", "red"],
    PlainValidator(lambda v: v.lower() if isinstance(v, str) else v),
]
LogLevelToLower = Annotated[
    Literal["debug", "info", "warn", "error"],
    PlainValidator(lambda v: v.lower() if isinstance(v, str) else v),
]


class ConfigBaseSettings(BaseSettings):
    """Base class for global config models. To prevent attributes from being modified after initialization."""

    model_config = SettingsConfigDict(
        env_nested_delimiter="_",
        env_nested_max_split=1,
        frozen=True,
        str_strip_whitespace=True,
        str_min_length=1,
    )


class _ConfigLoaderOCTI(ConfigBaseSettings):
    """Interface for loading OpenCTI dedicated configuration."""

    # Config Loader OpenCTI
    url: HttpUrlToString = Field(
        default="http://localhost:8080",
        description="The OpenCTI platform URL.",
    )
    token: str = Field(
        default="f4a01bd1-e5f7-4be8-952a-d1cc34bc529b",
        description="The token of the user who represents the connector in the OpenCTI platform.",
    )


class _ConfigLoaderConnector(ConfigBaseSettings):
    """Interface for loading Connector dedicated configuration."""

    # Config Loader Connector
    id: Optional[str] = Field(
        default='external-import-mwe',
        description="A unique UUIDv4 identifier for this connector instance.",
    )
    type: Optional[str] = Field(
        default="EXTERNAL_IMPORT",
        description="Should always be set to EXTERNAL_IMPORT for this connector.",
    )
    name: Optional[str] = Field(
        default="mwe",
        description="Name of the connector.",
    )
    scope: Optional[str] = Field(
        default="mwe",
        description="The scope or type of data the connector is importing, "
                    "either a MIME type or Stix Object (for information only).",
    )
    log_level: Optional[LogLevelToLower] = Field(
        default="error",
        description="Determines the verbosity of the logs.",
    )
    duration_period: Optional[timedelta] = Field(
        default="PT24H",
        description="Duration between two scheduled runs of the connector (ISO 8601 format).",
    )
    queue_threshold: Optional[PositiveInt] = Field(
        default=None,
        description="Connector queue max size in Mbytes. Default to 500.",
    )
    run_and_terminate: Optional[bool] = Field(
        default=None,
        description="Connector run-and-terminate flag.",
    )
    send_to_queue: Optional[bool] = Field(
        default=None,
        description="Connector send-to-queue flag.",
    )
    send_to_directory: Optional[bool] = Field(
        default=None,
        description="Connector send-to-directory flag.",
    )
    send_to_directory_path: Optional[str] = Field(
        default=None,
        description="Connector send-to-directory path.",
    )
    send_to_directory_retention: Optional[PositiveInt] = Field(
        default=None,
        description="Connector send-to-directory retention in days.",
    )

    @field_validator("type")
    def force_value_for_type_to_be_external_import(cls, value):
        return "EXTERNAL_IMPORT"


class ConfigLoader(ConfigBaseSettings):
    """Interface for loading global configuration settings."""

    opencti: _ConfigLoaderOCTI = _ConfigLoaderOCTI()

    connector: _ConfigLoaderConnector = Field(
        default=_ConfigLoaderConnector(),
        description="Connector configurations.",
    )

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource]:
        env_path = Path(__file__).parents[0] / ".env"
        yaml_path = Path(__file__).parents[0] / "config.yml"

        if env_path.exists():
            return (
                DotEnvSettingsSource(
                    settings_cls,
                    env_file=env_path,
                    env_ignore_empty=True,
                    env_file_encoding="utf-8",
                ),
            )
        elif yaml_path.exists():
            return (
                YamlConfigSettingsSource(
                    settings_cls,
                    yaml_file=yaml_path,
                    yaml_file_encoding="utf-8",
                ),
            )
        else:
            return (
                EnvSettingsSource(
                    settings_cls,
                    env_ignore_empty=True,
                ),
            )


class MainConfig:
    def __init__(self):
        """Initialize the connector with necessary configurations"""
        self.load = self._load_config()

    @staticmethod
    def _load_config() -> ConfigLoader:
        try:

            load_settings = ConfigLoader()
            return load_settings

        except ValidationError as err:
            raise ValueError(err)

        except Exception as err:
            raise ValueError(err)


# print(ConfigLoader.model_json_schema())
