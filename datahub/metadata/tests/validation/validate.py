from typing import Any

from validation import errors


def check_is_not_none(
        filepath: str,
        prop: str,
        value: Any
):
    if value is not None:
        return
    
    raise errors.PropertyNotExistingOrEmptyError(prop, filepath)

def check_string_is_not_none_or_empty(
        filepath: str,
        prop: str,
        value: Any | None
) -> None:
    if isinstance(value, str) and len(value) > 0:
        return
    
    raise errors.PropertyNotExistingOrEmptyError(prop, filepath)


def check_bool_is_not_none(
        filepath: str,
        prop: str,
        value: Any | None
) -> None:
    if isinstance(value, bool):
        return
    
    raise errors.PropertyNotExistingOrEmptyError(prop, filepath)


def check_list_is_not_none(
        filepath: str,
        prop: str,
        value: Any | None
) -> None:
    if isinstance(value, list):
        return

    raise errors.PropertyNotExistingOrEmptyError(prop, filepath)
