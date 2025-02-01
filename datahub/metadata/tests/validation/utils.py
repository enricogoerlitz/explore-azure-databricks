import pathlib
import json

from typing import Union
from dataclasses import dataclass

from validation import errors
from validation.imp import gprops


@dataclass(frozen=True)
class PipelineValidationResponse:
    is_valid: bool
    error: errors.BaseValidationError | None


def prepare_pipeline_response(
        is_valid: bool,
        error_messages: list[str],
        use_prefix: bool = False
) -> PipelineValidationResponse:
    prep_err = None
    if not is_valid:
        prep_err = "\n\nValidationErrors:\n" if use_prefix else ""
        for err in error_messages:
            prep_err += err if err.startswith("  -") else f"  - {err}\n"

        prep_err = errors.BaseValidationError(prep_err)

    return PipelineValidationResponse(is_valid, prep_err)

        
def read_json_files(path: pathlib.Path, expected_prefix: str):
    for file in path.iterdir():
        if (
            not file.is_file() or
            not file.name.startswith(expected_prefix) or
            not file.name.endswith(".json")
        ):
            continue
        
        with open(file, "r", encoding="utf-8") as f:
            try:
                json_data = json.load(f)
                json_data[gprops.DOC_FILEPATH] = file.absolute().name
                yield json_data, file.name

            except json.JSONDecodeError:
                raise errors.InvalidJSONContentError(file.name)
