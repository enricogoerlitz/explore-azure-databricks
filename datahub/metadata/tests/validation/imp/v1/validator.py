# flake8: noqa

from validation.utils import PipelineValidationResponse
from validation.imp.v1 import props
from validation.imp import gprops
from validation import errors
from validation import validate
from validation.utils import prepare_pipeline_response
from validation.imp.base import AbstractImportValidator


class ImportValidatorV1(AbstractImportValidator):

    def __init__(self, file_json: dict) -> None:
        self._error_messages: list[str] = []
        self._is_valid = True
        self._filename = file_json.get(gprops.DOC_FILEPATH, "...Filename not set.")

        super().__init__(file_json)

    def get_doc_version(self) -> str:
        return self.json.get(gprops.DOC_VERSION)

    def get_doc_ignore_tests_global_duplication_destination(self) -> bool:
        return self.json.get(gprops.DOC_IGNORE_TESTS_DUPL_DESTINATION_FILE, False)

    def get_name(self) -> str:
        return self.json.get(gprops.NAME)

    def get_version(self) -> str:
        return self.json.get(gprops.VERSION)

    def get_active(self) -> bool:
        return self.json.get(props.IMPORT_SETTINGS, {}) \
                        .get(props.IMPORT_ACTIVE)

    def get_source_system_database(self) -> str:
        return self.json.get(props.IMPORT_SETTINGS, {}) \
                        .get(props.SOURCE_SYSTEM, {}) \
                        .get(props.DATABASE)

    def get_source_system_default_schema(self) -> str:
        return self.json.get(props.IMPORT_SETTINGS, {}) \
                        .get(props.SOURCE_SYSTEM, {}) \
                        .get(props.DEFAULT_SCHEMA)

    def get_datahub_default_schema(self) -> str:
        return self.json.get(props.IMPORT_SETTINGS, {}) \
                        .get(props.DATA_HUB, {}) \
                        .get(props.DEFAULT_SCHEMA)

    def get_table_count(self) -> int:
        tables = self.json.get(props.TABLES, [])
        return len(tables)

    def get_table_run(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        return table.get(props.RUN)

    def get_table_source_schema(self, index: int) -> str:
        table = self._get_table_by_index(index)
        alt_schema = self.get_source_system_default_schema()
        return table.get(props.SOURCE, {}).get(props.SCHEMA, alt_schema)

    def get_table_source_tablename(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        return table.get(props.SOURCE, {}).get(props.TABLENAME)

    def get_table_bronze_schema(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        alt_schema = self.get_datahub_default_schema()
        return table.get(props.BRONZE, {}).get(props.SCHEMA, alt_schema)

    def get_table_bronze_tablename(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        alt_tablename = self.get_table_source_tablename(index)
        return table.get(props.BRONZE, {}).get(props.TABLENAME, alt_tablename)

    def get_table_silver_schema(self, index: int) -> bool:
        table = self._get_table_by_index(index)

        alt_schema = self.get_table_bronze_schema(index)

        return table.get(props.SILVER, {}) \
                    .get(props.NOTEBOOK, {}) \
                    .get(props.SCHEMA, alt_schema)

    def get_table_silver_tablename(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        alt_tablename = self.get_table_bronze_tablename(index)
        return table.get(props.SILVER, {}) \
                    .get(props.NOTEBOOK, {}) \
                    .get(props.TABLENAME, alt_tablename)

    def get_table_silver_nk_columns(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        return table.get(props.SILVER, {}) \
                    .get(props.NOTEBOOK, {}) \
                    .get(props.NK_COLUMNS)

    def get_table_bronze_destination(self, index: int) -> str:
        schema = self._get_schema_with_name(self.get_table_bronze_schema(index))
        tablename = self.get_table_bronze_tablename(index)
        return f"{schema}.{tablename}"

    def get_table_silver_destination(self, index: int) -> str:
        schema = self._get_schema_with_name(self.get_table_silver_schema(index))
        tablename = self.get_table_silver_tablename(index)
        return f"{schema}.{tablename}"

    def get_table_historize(self, index: int) -> bool:
        table = self._get_table_by_index(index)
        return table.get(props.HISTORIZE, False)

    def get_table_deltaload(self, index: int) -> dict | None:
        table = self._get_table_by_index(index)
        return table.get(props.DELTA_LOAD)

    def get_table_deltaload_enable(self, index: int) -> bool | None:
        table = self._get_table_by_index(index)
        return table.get(props.DELTA_LOAD, {}) \
                    .get(props.ENABLE)

    def get_table_deltaload_delta_column(self, index: int) -> str | None:
        table = self._get_table_by_index(index)
        return table.get(props.DELTA_LOAD, {}) \
                    .get(props.DELTA_COLUMN)

    def get_table_deltaload_use_broadcast(self, index: int) -> str | None:
        table = self._get_table_by_index(index)
        return table.get(props.DELTA_LOAD, {}) \
                    .get(props.USE_BROADCAST)

    def validate(self) -> PipelineValidationResponse:
        self._check_name()
        self._check_import_settings()
        self._check_tables()

        return prepare_pipeline_response(self._is_valid, self._error_messages)

    def _check_name(self):
        # CHECK name property is existing and not empty
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=gprops.NAME,
                value=self.get_name()
            )
        )

    def _check_import_settings(self):
        # CHECK importSettings property is exsiting
        imp_settings: dict = self.json.get(props.IMPORT_SETTINGS)
        self._run_check(
            lambda: validate.check_is_not_none(
                filepath=self._filename,
                prop=props.IMPORT_SETTINGS,
                value=imp_settings
            )
        )

        # CHECK active property is existing and is bool
        self._run_check(
            validate.check_bool_is_not_none(
                filepath=self._filename,
                prop=f"{props.IMPORT_SETTINGS}.{props.IMPORT_ACTIVE}",
                value=self.get_active()
            )
        )

        # CHECK importSettings.sourceSystem property is exsiting
        source_system = imp_settings.get(props.SOURCE_SYSTEM)
        self._run_check(
            lambda: validate.check_is_not_none(
                filepath=self._filename,
                prop=props.SOURCE_SYSTEM,
                value=source_system
            )
        )

        # CHECK importSettings.sourceSystem.database property
        # is exsiting and not empty
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.IMPORT_SETTINGS}.{props.SOURCE_SYSTEM}.{props.DATABASE}",
                value=self.get_source_system_database()
            )
        )

        # CHECK importSettings.sourceSystem.defaultSchema property
        # is exsiting and not empty
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.IMPORT_SETTINGS}.{props.SOURCE_SYSTEM}.{props.DEFAULT_SCHEMA}",
                value=self.get_source_system_default_schema()
            )
        )

        # CHECK importSettings.dataHub.defaultSchema property
        # is exsiting and not empty
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.IMPORT_SETTINGS}.{props.DATA_HUB}.{props.DEFAULT_SCHEMA}",
                value=self.get_datahub_default_schema()
            )
        )

    def _check_tables(self):
        # CHECK tables property is existing
        tables: list[dict] = self.json.get(props.TABLES)
        self._run_check(
            lambda: validate.check_list_is_not_none(
                filepath=self._filename,
                prop=props.TABLES,
                value=tables
            )
        )

        # CHECK each table integrety
        for index in range(0, self.get_table_count()):
            self._check_table(index)

    def _check_table(self, index: int):
        self._check_table_root_config(index)
        self._check_table_deltaload_config(index)
        self._check_table_source_config(index)
        self._check_table_bronze_config(index)
        self._check_table_silver_config(index)

    def _check_table_root_config(self, index: int) -> None:
        # CHECK run property is existing and is bool
        self._run_check(
            lambda: validate.check_bool_is_not_none(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.RUN}",
                value=self.get_table_run(index)
            )
        )

        # CHECK historize property is None or bool
        self._run_check(
            lambda: validate.check_bool_is_not_none(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.HISTORIZE}",
                value=self.get_table_historize(index)
            )
        )

    def _check_table_deltaload_config(self, index: int) -> None:
        delta_load_cnf = self.get_table_deltaload(index)
        if delta_load_cnf is None:
            return

        self._run_check(
            lambda: validate.check_bool_is_not_none(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.DELTA_LOAD}.{props.ENABLE}",
                value=self.get_table_deltaload_enable(index)
            )
        )

        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.DELTA_LOAD}.{props.DELTA_COLUMN}",
                value=self.get_table_deltaload_delta_column(index)
            )
        )

        self._run_check(
            lambda: validate.check_bool_is_not_none(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.DELTA_LOAD}.{props.USE_BROADCAST}",
                value=self.get_table_deltaload_use_broadcast(index)
            )
        )

    def _check_table_source_config(self, index: int) -> None:
        # CHECK tables.table[x].source.schema property
        # is exsiting and not empty OR has fallback value
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.SOURCE}.{props.SCHEMA}",
                value=self.get_table_source_schema(index)
            )
        )

        # CHECK tables.table[x].source.tablename property
        # is exsiting and not empty (MUST BE SET!)
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.SOURCE}.{props.TABLENAME}",
                value=self.get_table_source_tablename(index)
            )
        )

    def _check_table_bronze_config(self, index: int) -> None:
        # CHECK tables.table[x].bronze.schema property
        # is exsiting and not empty OR has fallback value
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.BRONZE}.{props.SCHEMA}",
                value=self.get_table_bronze_schema(index)
            )
        )

        # CHECK tables.table[x].bronze.tablename property
        # is exsiting and not empty OR has fallback value
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.BRONZE}.{props.TABLENAME}",
                value=self.get_table_bronze_tablename(index)
            )
        )

    def _check_table_silver_config(self, index: int) -> None:
        # CHECK tables.table[x].silver.schema property
        # is exsiting and not empty OR has fallback value
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.SILVER}.{props.NOTEBOOK}.{props.SCHEMA}",
                value=self.get_table_silver_schema(index)
            )
        )

        # CHECK tables.table[x].silver.tablename property
        # is exsiting and not empty OR has fallback value
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.SILVER}.{props.NOTEBOOK}.{props.TABLENAME}",
                value=self.get_table_silver_tablename(index)
            )
        )

        # CHECK tables.table[x].silver.nk_columns property
        # is exsiting and not empty (MUST BE SET!)
        self._run_check(
            lambda: validate.check_string_is_not_none_or_empty(
                filepath=self._filename,
                prop=f"{props.TABLES}.{props.SILVER}.{props.NOTEBOOK}.{props.NK_COLUMNS}",
                value=self.get_table_silver_nk_columns(index)
            )
        )

    def _get_table_by_index(self, index: int) -> dict:
        tables = self.json.get(props.TABLES)
        if tables is None or index >= len(tables):
            return {}

        return tables[index]

    def _get_schema_with_name(self, schema: str) -> str:
        name = self.get_name()
        return f"{name}_{schema}"

    def _run_check(self, fn) -> None:
        if fn is None:
            return

        try:
            fn()
        except (errors.BaseValidationError,
                Exception) as e:
            self._is_valid = False
            self._error_messages.append(str(e))
