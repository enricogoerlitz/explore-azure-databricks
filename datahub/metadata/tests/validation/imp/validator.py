from validation.imp.base import ImportValidatorInterface
from validation.utils import PipelineValidationResponse
from validation.utils import prepare_pipeline_response


class GlobalValidator:
    def __init__(self, validators: list[ImportValidatorInterface]) -> None:
        self._result: PipelineValidationResponse = None
        self._is_valid = True
        self._validators = validators
        self._error_messages = []
        self._name_version_set = set()
        self._bronze_destination_set = set()
        self._silver_destination_set = set()

    def validate(self) -> PipelineValidationResponse:
        if self._result is not None:
            raise Exception("Was already validated. You can run this method only once.")
        
        for file_validator in self._validators:
            if file_validator.get_doc_ignore_tests_global_duplication_destination():
                continue

            self._check_name_version(file_validator)

            for index in range(0, file_validator.get_table_count()):
                self._check_bronze_destination(file_validator, index)
                self._check_silver_destination(file_validator, index)

        self._result = prepare_pipeline_response(self._is_valid, self._error_messages)
        return self._result

    def _check_name_version(self, file_validator: ImportValidatorInterface) -> None:
        name = file_validator.get_name()
        version = file_validator.get_version()
        name_version_tpl = (name, version)

        if name_version_tpl in self._name_version_set:
            self._is_valid = False
            err = f"The name '{name}' is already existing with the version '{version}'."
            self._error_messages.append(err)
        else:
            self._name_version_set.add(name_version_tpl)

    def _check_bronze_destination(self, file_validator: ImportValidatorInterface, index: int) -> None:
        bronze_destination = file_validator.get_table_bronze_destination(index)
        if bronze_destination in self._bronze_destination_set:
            self._is_valid = False
            err = f"Duplicate value for bronze destination: '{bronze_destination}'."
            self._error_messages.append(err)
        else:
            self._bronze_destination_set.add(bronze_destination)

    def _check_silver_destination(self, file_validator: ImportValidatorInterface, index: int) -> None:
        silver_destination = file_validator.get_table_silver_destination(index)
        if silver_destination in self._silver_destination_set:
            self._is_valid = False
            err = f"Duplicate value for silver destination: '{silver_destination}'."
            self._error_messages.append(err)
        else:
            self._silver_destination_set.add(silver_destination)
