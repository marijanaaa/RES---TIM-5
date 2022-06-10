import unittest
from Repository import Repository
class TestRepository(unittest.TestCase):
    def test_DoQuery_2000(self):
        rep = Repository()
        sql_query = '''SELECT * from radnik'''
        ret = rep.doQuery(sql_query)
        response = {'status_code': 2000, 'status': 'SUCCESS', 'payload': ((1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2), (3323, 'Sara', 'Doktorka u odeljenju za oftamologiju', 1), (4556, 'Milena', 'Doktorka u odeljenju za pulmologiju', 1), (4566, 'Petar', 'Medicinski tehnicar  u odeljenju za pedijatriju', 2), (8978, 'Dragan', 'Doktor u odeljenju za dermatologiju', 1), (9699, 'Ivana', 'Medicinski tehnicar  u odeljenju za kardiologiju', 2))}
        self.assertEqual(ret, response)
    
    def test_DoQuery_3000(self):
        rep = Repository()
        sql_query = '''SELECT * from bl'''
        ret = rep.doQuery(sql_query)
        response = {'status_code': 3000, 'status': 'REJECTED', 'payload': "Table 'bolnica.bl' doesn't exist"}
        self.assertEqual(ret, response)

    def test_DoQuery_5000(self):
        rep = Repository()
        sql_query = '''SELECT * from radnik=; commit;'''
        ret = rep.doQuery(sql_query)
        response = {'status_code': 5000, 'status': 'BAD_FORMAT', 'payload': "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '=; commit' at line 1"}
        self.assertEqual(ret, response)

if __name__ == '__main__':
    unittest.main()
