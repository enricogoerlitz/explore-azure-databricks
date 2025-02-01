import pathlib
import json

from validation.imp.validator import GlobalValidator
from validation.imp import gprops
from validation.imp.v1.validator import ImportValidatorV1
from validation import errors
from validation.imp.base import ImportValidatorInterface
from validation.utils import (
    PipelineValidationResponse,
    prepare_pipeline_response,
    read_json_files
)


FILEPREFIX = "metadata.import."
FILESUFFIX = ".json"


def get_filevalidator(file_json: dict, filepath: str) -> ImportValidatorInterface:
    doc_version = file_json.get(gprops.DOC_VERSION)
    match doc_version:
        case "v1":
            return ImportValidatorV1(file_json)

        case _:
            raise errors.DocumentVersionNotSupportedError(doc_version, filepath)


class ImportValidationHandler:
    def __init__(self, path: pathlib.Path) -> None:
        self._path = path

    def validate(self) -> PipelineValidationResponse:
        is_valid = True
        error_messages = []
        try:
            file_validators = [
                get_filevalidator(json_file, filepath)
                for json_file, filepath in read_json_files(self._path, FILEPREFIX)
                if not json_file.get(gprops.DOC_IGNORE_TESTS_ENTIRE_FILE, False)
            ]
            global_validator = GlobalValidator(file_validators)

            # VALIDATE EACH FILE ITSELF
            for file_validator in file_validators:
                result = file_validator.validate()

                if not result.is_valid:
                    is_valid = False
                    error_messages.append(str(result.error))

            # VALIDATE GLOBAL INTEGRITY
            global_result = global_validator.validate()
            if not global_result.is_valid:
                is_valid = False
                error_messages.append(str(global_result.error))

            return prepare_pipeline_response(is_valid, error_messages, use_prefix=True)

        except Exception as e:
            return prepare_pipeline_response(False, [str(e)], use_prefix=True)
