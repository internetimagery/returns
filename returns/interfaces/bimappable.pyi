import abc
from returns.interfaces import altable as altable, mappable as mappable
from typing import Any

class BiMappableN(mappable.MappableN[_FirstType, _SecondType, _ThirdType], altable.AltableN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta): ...

BiMappable2: Any
BiMappable3: Any
