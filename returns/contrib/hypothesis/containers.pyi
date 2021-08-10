from hypothesis import strategies as st
from returns.primitives.laws import Lawful as Lawful
from typing import Callable, Type

def strategy_from_container(container_type: Type[Lawful], *, use_init: bool=...) -> Callable[[type], st.SearchStrategy]: ...
