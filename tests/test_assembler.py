import os
import unittest
import shutil
from gos.assembler import AssemblyManager
from gos.configuration import Configuration
from tests.test_logging import MockingLoggingHandler

__author__ = 'aganezov'


class AssemblerManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.config = Configuration()
        self.output_dir_name = self.config[Configuration.OUTPUT][Configuration.OUTPUT_DIRECTORY]
        if not os.path.exists(self.output_dir_name):
            os.mkdir(self.output_dir_name)
        self.assembler_manager = AssemblyManager()
        self.assembler_manager.logger.handlers = []
        self.mocking_handler = MockingLoggingHandler()
        self.mocking_handler.reset()
        self.assembler_manager.logger.addHandler(self.mocking_handler)

    def tearDown(self):
        if os.path.exists(self.output_dir_name):
            shutil.rmtree(self.output_dir_name)

    def test_empty_initialization(self):
        manager = AssemblyManager()
        self.assertIsNotNone(manager.config)
        self.assertIsNotNone(manager.logger)

    def test_default_logger_name(self):
        assembler_manager = AssemblyManager()
        self.assertEqual(assembler_manager.logger.name,
                         assembler_manager.config[Configuration.LOGGING][Configuration.LOGGER_NAME])

    def test_logger_format(self):
        assembler_manager = AssemblyManager()
        self.assertEqual(assembler_manager.logger.level,
                         assembler_manager.config[Configuration.LOGGING][Configuration.LOGGING_LEVEL])


if __name__ == '__main__':
    unittest.main()
