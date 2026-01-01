import logging
import unittest
from pathlib import Path
from zensols.util import Failure
from zensols.config import ConfigFactory
from zensols.cli import CliHarness
from zensols.dbutilpg import Application, ApplicationFactory


if 0:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


class TestBase(unittest.TestCase):
    def _get_harness(self) -> CliHarness:
        return ApplicationFactory.create_harness()

    def _get_config_factory(self) -> ConfigFactory:
        harn: CliHarness = self._get_harness()
        return harn.get_config_factory(
            '-c test-resources/dbutilpg.conf --level=err')

    def _get_application(self) -> Application:
        harn: CliHarness = self._get_harness()
        app: Application = harn.get_application(
            '-c test-resources/dbutilpg.conf --level=err')
        if isinstance(app, Failure):
            app.rethrow()
        return app


class TestApplication(TestBase):
    def setUp(self):
        self.app: Application = self._get_application()

    def test_somedata(self):
        app = self.app
        self.assertEqual(Application, type(app))
        res: int = app.run()
        self.assertEqual(123, res)
