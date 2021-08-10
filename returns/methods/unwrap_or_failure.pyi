from returns.interfaces.unwrappable import Unwrappable as Unwrappable
from typing import Union

def unwrap_or_failure(container: Unwrappable[_FirstType, _SecondType]) -> Union[_FirstType, _SecondType]: ...
