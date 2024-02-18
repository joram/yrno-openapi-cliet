# coding: utf-8

"""
    Locationforecast

    Weather forecast for a specified place

    The version of the OpenAPI document: 2.0
    Contact: weatherapi-adm@met.no
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ForecastUnits(BaseModel):
    """
    ForecastUnits
    """ # noqa: E501
    air_pressure_at_sea_level: Optional[StrictStr] = None
    air_temperature: Optional[StrictStr] = None
    air_temperature_max: Optional[StrictStr] = None
    air_temperature_min: Optional[StrictStr] = None
    cloud_area_fraction: Optional[StrictStr] = None
    cloud_area_fraction_high: Optional[StrictStr] = None
    cloud_area_fraction_low: Optional[StrictStr] = None
    cloud_area_fraction_medium: Optional[StrictStr] = None
    dew_point_temperature: Optional[StrictStr] = None
    fog_area_fraction: Optional[StrictStr] = None
    precipitation_amount: Optional[StrictStr] = None
    precipitation_amount_max: Optional[StrictStr] = None
    precipitation_amount_min: Optional[StrictStr] = None
    probability_of_precipitation: Optional[StrictStr] = None
    probability_of_thunder: Optional[StrictStr] = None
    relative_humidity: Optional[StrictStr] = None
    ultraviolet_index_clear_sky_max: Optional[StrictStr] = None
    wind_from_direction: Optional[StrictStr] = None
    wind_speed: Optional[StrictStr] = None
    wind_speed_of_gust: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["air_pressure_at_sea_level", "air_temperature", "air_temperature_max", "air_temperature_min", "cloud_area_fraction", "cloud_area_fraction_high", "cloud_area_fraction_low", "cloud_area_fraction_medium", "dew_point_temperature", "fog_area_fraction", "precipitation_amount", "precipitation_amount_max", "precipitation_amount_min", "probability_of_precipitation", "probability_of_thunder", "relative_humidity", "ultraviolet_index_clear_sky_max", "wind_from_direction", "wind_speed", "wind_speed_of_gust"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ForecastUnits from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ForecastUnits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "air_pressure_at_sea_level": obj.get("air_pressure_at_sea_level"),
            "air_temperature": obj.get("air_temperature"),
            "air_temperature_max": obj.get("air_temperature_max"),
            "air_temperature_min": obj.get("air_temperature_min"),
            "cloud_area_fraction": obj.get("cloud_area_fraction"),
            "cloud_area_fraction_high": obj.get("cloud_area_fraction_high"),
            "cloud_area_fraction_low": obj.get("cloud_area_fraction_low"),
            "cloud_area_fraction_medium": obj.get("cloud_area_fraction_medium"),
            "dew_point_temperature": obj.get("dew_point_temperature"),
            "fog_area_fraction": obj.get("fog_area_fraction"),
            "precipitation_amount": obj.get("precipitation_amount"),
            "precipitation_amount_max": obj.get("precipitation_amount_max"),
            "precipitation_amount_min": obj.get("precipitation_amount_min"),
            "probability_of_precipitation": obj.get("probability_of_precipitation"),
            "probability_of_thunder": obj.get("probability_of_thunder"),
            "relative_humidity": obj.get("relative_humidity"),
            "ultraviolet_index_clear_sky_max": obj.get("ultraviolet_index_clear_sky_max"),
            "wind_from_direction": obj.get("wind_from_direction"),
            "wind_speed": obj.get("wind_speed"),
            "wind_speed_of_gust": obj.get("wind_speed_of_gust")
        })
        return _obj

