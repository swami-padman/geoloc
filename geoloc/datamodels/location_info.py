from typing import Optional

import pydantic

from geoloc.datamodels.base_model import ModelConfig


class CityStateLocationInfo(ModelConfig):
    name: str
    local_names: Optional[dict] = None
    lat: float
    lon: float
    country: str
    state: str


class ZipLocationInfo(ModelConfig):
    name: str
    lat: float
    lon: float
    country: str
    zip: str
