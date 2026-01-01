import logging
import unittest
from pathlib import Path
from zensols.config import ImportIniConfig, ImportConfigFactory
from zensols.db import Bean


if 0:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


class Person(Bean):
    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age

    def get_attr_names(self):
        return 'id name age'.split()


class TestPostgresConnManager(unittest.TestCase):
    def setUp(self):
        self.fac = ImportConfigFactory(ImportIniConfig(Path('test-resources/dbutilpg.conf')))

    def tearDown(self):
        persister = self.fac.instance('inst_pg_db_persister')
        persister.execute_no_read('destroy')

    def test_pg(self):
        persister = self.fac.instance('inst_pg_db_persister', row_factory='dict')
        persister.conn_manager.capture_lastrowid = True
        self.assertEqual(0, persister.get_count())
        self.assertEqual(1, persister.insert_row('paul', 23))
        self.assertEqual(2, persister.insert_row('sue', 33))
        peeps = persister.get()
        self.assertEqual(2, len(peeps))
        self.assertEqual({'id': 1, 'name': 'paul', 'age': 23}, peeps[0])
        self.assertEqual({'id': 2, 'name': 'sue', 'age': 33}, peeps[1])
        persister.row_factory = 'tuple'
        peeps = persister.get()
        self.assertEqual(2, len(peeps))
        self.assertEqual(('paul', 23, 1), peeps[0])
        self.assertEqual(('sue', 33, 2), peeps[1])
        persister.row_factory = Person
        peeps = persister.get()
        self.assertEqual('id: 1, name: paul, age: 23', str(peeps[0]))
        self.assertEqual('id: 2, name: sue, age: 33', str(peeps[1]))
        peep = persister.get_by_id(2)
        self.assertEqual('id: 2, name: sue, age: 33', str(peep))
        new_peeps = (('bob', 42), ('jane', 90),)
        self.assertEqual(4, persister.insert_rows(new_peeps))
        peeps = persister.get()
        self.assertEqual({'id': 3, 'name': 'bob', 'age': 42}, peeps[0].get_attrs())
        self.assertEqual({'id': 4, 'name': 'jane', 'age': 90}, peeps[1].get_attrs())
        bean = Person('kyle', 52)
        self.assertEqual(None, bean.id)
        self.assertEqual(5, persister.insert(bean))
        self.assertEqual(5, bean.id)
        self.assertEqual(((5,),), persister.execute_by_name('people_count', row_factory='tuple'))
        peep = persister.get_by_id(2)
        self.assertEqual('id: 2, name: sue, age: 33', str(peep))
        peep = persister.get_by_id(5)
        self.assertEqual('id: 5, name: kyle, age: 52', str(peep))
        self.assertEqual(None, persister.get_by_id(100))
        self.assertTrue(persister.exists(1))
        self.assertTrue(persister.exists(5))
        self.assertFalse(persister.exists(100))
        peep = persister.get_by_id(2)
        peep.age = 41
        self.assertTrue(2, persister.update(peep))
        peep = persister.get_by_id(2)
        self.assertEqual('id: 2, name: sue, age: 41', str(peep))
        self.assertTrue(persister.exists(2))
        self.assertTrue(2, persister.delete(2))
        self.assertFalse(persister.exists(2))
        self.assertEqual(((4,),), persister.execute_by_name('people_count', row_factory='tuple'))
        self.assertEqual(4, persister.get_count())
        self.assertEqual((1, 3, 4, 5), tuple(persister.get_keys()))
        new_peeps = (Person('jake', 62), Person('christina', 22),)
        self.assertEqual(7, persister.insert_beans(new_peeps))
        peeps = persister.get()
        self.assertEqual({'id': 6, 'name': 'jake', 'age': 62}, peeps[2].get_attrs())
        self.assertEqual({'id': 7, 'name': 'christina', 'age': 22}, peeps[1].get_attrs())

        df = persister.execute_by_name('select_people', row_factory='pandas')
        self.assertEqual(6, len(df))
        self.assertEqual(['name', 'age', 'id'], list(df.columns))
        self.assertEqual('bob christina jake jane kyle paul'.split(),
                         df['name'].tolist())
        self.assertEqual([42, 22, 62, 90, 52, 23], df['age'].tolist())
