from abc import ABC, abstractmethod

from validation.utils import PipelineValidationResponse


class ImportValidatorInterface(ABC):
    
    @abstractmethod
    def validate(self) -> PipelineValidationResponse: pass

    @abstractmethod
    def get_doc_version(self) -> str: pass

    @abstractmethod
    def get_doc_ignore_tests_global_duplication_destination(self) -> bool: pass

    @abstractmethod
    def get_version(self) -> str: pass

    @abstractmethod
    def get_name(self) -> str: pass

    @abstractmethod
    def get_active(self) -> bool: pass

    @abstractmethod
    def get_source_system_database(self) -> str: pass

    @abstractmethod
    def get_source_system_default_schema(self) -> str: pass

    @abstractmethod
    def get_datahub_default_schema(self) -> str: pass

    @abstractmethod
    def get_table_count(self) -> int: pass

    @abstractmethod
    def get_table_run(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_source_schema(self, index: int) -> str: pass

    @abstractmethod
    def get_table_source_tablename(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_bronze_schema(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_bronze_tablename(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_silver_schema(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_silver_tablename(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_silver_nk_columns(self, index: int) -> str: pass

    @abstractmethod
    def get_table_bronze_destination(self, index: int) -> str: pass

    @abstractmethod
    def get_table_silver_destination(self, index: int) -> str: pass

    @abstractmethod
    def get_table_historize(self, index: int) -> str: pass

    @abstractmethod
    def get_table_deltaload(self, index: int) -> dict | None: pass

    @abstractmethod
    def get_table_deltaload_enable(self, index: int) -> bool: pass

    @abstractmethod
    def get_table_deltaload_delta_column(self, index: int) -> str: pass

    @abstractmethod
    def get_table_deltaload_use_broadcast(self, index: int) -> str: pass


class AbstractImportValidator(ImportValidatorInterface):

    def __init__(self, file_json: dict) -> None:
        super().__init__()

        self._json = file_json

    @property
    def json(self):
        return self._json
