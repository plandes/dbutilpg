import logging
from zensols.actioncli import ClassImporter
from zensols.dbutilpg import AppConfig

logger = logging.getLogger(__name__)


def instance(name, info=(), debug=()):
    conf = AppConfig('resources/dbutilpg.conf')
    for l in debug:
        logging.getLogger(f'zensols.dbutilpg.{l}').setLevel(logging.DEBUG)
    for l in info:
        logging.getLogger(f'zensols.dbutilpg.{l}').setLevel(logging.INFO)
    return ClassImporter(name).instance(conf)


def tmp():
    app = instance('zensols.dbutilpg.app.MainApplication', debug='app'.split())
    app.tmp()


def main():
    logging.basicConfig(level=logging.WARNING)
    run = 1
    {1: tmp,
     }[run]()


main()
