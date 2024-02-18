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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from openapi_client.models.forecast import Forecast
from openapi_client.models.point_geometry import PointGeometry
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class METJSONForecast(BaseModel):
    """
    METJSONForecast
    """ # noqa: E501
    geometry: PointGeometry
    properties: Forecast
    type: StrictStr
    __properties: ClassVar[List[str]] = ["geometry", "properties", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Feature'):
            raise ValueError("must be one of enum values ('Feature')")
        return value

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
        """Create an instance of METJSONForecast from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of METJSONForecast from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "geometry": PointGeometry.from_dict(obj.get("geometry")) if obj.get("geometry") is not None else None,
            "properties": Forecast.from_dict(obj.get("properties")) if obj.get("properties") is not None else None,
            "type": obj.get("type")
        })
        return _obj


