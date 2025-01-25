from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorResponse:
    filename: str
    error_message: str


class BaseValidationError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class GenericValidationError(Exception):
    def __init__(self, msg: str, filepath: str) -> None:
        msg = f"{filepath}: {msg}"
        super().__init__(msg)


class DocumentVersionNotSupportedError(GenericValidationError):
    def __init__(self, version: str, filepath: str) -> None:
        msg = f"The version '{version}' is not supported."
        super().__init__(msg, filepath)


class InvalidJSONContentError(GenericValidationError):
    def __init__(self, filepath: str) -> None:
        msg = f"Invalid JSON content."
        super().__init__(msg, filepath)


class PropertyNotExistingOrEmptyError(GenericValidationError):
    def __init__(self, prop: str, filepath: str) -> None:
        msg = f"Property '{prop}' not existing or is was empty but is required."
        super().__init__(msg, filepath)
