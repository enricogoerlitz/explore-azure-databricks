import unittest
import pathlib

from validation.imp.handler import ImportValidationHandler


OSPATH_IMPORT_METADATA = "./datahub/metadata/meta/pipelines/import"


class ApplicationServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.import_handler = ImportValidationHandler(
            path=pathlib.Path(OSPATH_IMPORT_METADATA)
        )

        self.raise_error = False

    def test_pipeline(self):
        self.assertFalse(self.raise_error, "Test should not raise an error.")

    def test_import_files(self):
        result = self.import_handler.validate()
        self.assertTrue(result.is_valid, str(result.error))


if __name__ == "__main__":
    unittest.main()
