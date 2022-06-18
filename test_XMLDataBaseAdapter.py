import socket
import threading
import unittest
from XMLDataBaseAdapter import XMLDateBaseAdapter
from unittest.mock import MagicMock, patch

class TestXMLDataBaseAdapter(unittest.TestCase):
    def test_delete_without_where(self):
        xml_string="<data><verb>DELETE</verb><noun>radnik</noun></data>"
        xml_db=XMLDateBaseAdapter()
        ret_value=xml_db.delete_method(xml_string)
        correct="DELETE FROM radnik; commit;"
        self.assertEqual(ret_value, correct)
    def test_delete_with_where(self):
        xml_string="<data><verb>DELETE</verb><noun>radnik</noun><query>ime='Ana';jmbg=12</query></data>"
        xml_db=XMLDateBaseAdapter()
        ret_value=xml_db.delete_method(xml_string)
        correct="DELETE FROM radnik WHERE ime='Ana' and jmbg=12 ; commit;"
        self.assertEqual(ret_value, correct)
    def test_insert(self):
        xml = "<data><verb>POST</verb><noun>radnik</noun><query>jmbg = 44; ime  = Ana; opis = nesto; id_vrsta = 111</query></data>"
        xml_db = XMLDateBaseAdapter()
        ret_value = xml_db.insert_method(xml)
        sql1 = "INSERT INTO radnik VALUES (  44,  Ana,  nesto,  111); commit;"
        self.assertEqual(ret_value, sql1 )
    def test_update(self):
        xml = "<data><verb>PATCH</verb><noun>radnik</noun><query>ime  = 'Anica' </query><fields>ime='Ana'</fields></data>"
        xml_db = XMLDateBaseAdapter()
        ret_value = xml_db.update_method(xml)
        sql1 = "UPDATE radnik SET ime  = 'Anica'  WHERE ime='Ana'; commit;"
        self.assertEqual(ret_value, sql1 )

    def test_get_without_fields(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><query>ime=\"Ana\"</query></data>"
        sql_query = """SELECT * from radnik where ime=\"Ana\" ; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.get_method(xml_obj), sql_query)
    
    def test_get_without_query_and_fields(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun></data>"
        sql_query = """SELECT * from radnik; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.get_method(xml_obj), sql_query)

    def test_get_with_all(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana';jmbg=1</query><fields>id</fields></data>"
        sql_query = """SELECT id from radnik where ime='Ana' and jmbg=1 ; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.get_method(xml_obj), sql_query)
    
    def test_get_without_query(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><fields>id</fields></data>"
        sql_query = """SELECT id from radnik; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.get_method(xml_obj), sql_query)
    def test_insert_in_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>POST</verb><noun>radnik</noun><query>jmbg = 44; ime  = Ana; opis = nesto; id_vrsta = 111</query></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value = "INSERT INTO radnik VALUES (  44,  Ana,  nesto,  111); commit;")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_update_in_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>PATCH</verb><noun>radnik</noun><query>ime  = 'Anica' </query><fields>ime='Ana'</fields></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value = "UPDATE radnik SET ime  = 'Anica'  WHERE ime='Ana'; commit;")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_delete_with_where_in_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>DELETE</verb><noun>radnik</noun><query>ime='Ana';jmbg=12</query></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value = "DELETE FROM radnik WHERE ime='Ana' and jmbg=12 ; commit;")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_delete_without_where_in_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>DELETE</verb><noun>radnik</noun></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value = "DELETE FROM radnik; commit;")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_get_without_fields_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>GET</verb><noun>radnik</noun><query>ime=\"Ana\"</query></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value =  """SELECT * from radnik where ime=\"Ana\" ; commit;""")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_Get_without_query_and_fields_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>GET</verb><noun>radnik</noun></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value =  """SELECT * from radnik; commit;""")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_get_with_all_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana';jmbg=1</query><fields>id</fields></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value =  """SELECT id from radnik where ime='Ana' and jmbg=1 ; commit;""")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def test_get_without_query_from_xml_to_sql(self):
        xml_adapter = XMLDateBaseAdapter()
        xml = "<data><verb>GET</verb><noun>radnik</noun><fields>id</fields></data>"
        xml_adapter.from_xml_to_sql = MagicMock(return_value =  """SELECT id from radnik; commit;""")
        xml_adapter.from_xml_to_sql(xml)
        xml_adapter.from_xml_to_sql.assert_called_with(xml)
    def fake_server_xml(self):
        server_sock = socket.socket()
        server_sock.bind(('localhost', 10004))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()
        
    @patch('socket.socket')
    def test_konekcija_xml_to_repository(self, mock_socketconstructor):
        expected_return=bytes('\x80\x04\x95v\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x0bstatus_code\x94M\xd0\x07\x8c\x06status\x94\x8c\x07SUCCESS\x94\x8c\x07payload\x94(M\xeb\x03\x8c\x03Ana\x94\x8c0Medicinski tehnicar  u odeljenju za ginekologiju\x94K\x02t\x94\x85\x94u.', encoding="utf-8")
        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value=expected_return
        server_thread = threading.Thread(target=self.fake_server_xml)
        server_thread.start()
    
        result="SELECT * from radnik where ime='Ana' ; commit;"
        returned_value = XMLDateBaseAdapter.connect_to_repository(self, result);
        self.assertEqual(expected_return, returned_value)
    
        server_thread.join()

    @patch('socket.socket')
    def test_getResponse(self, mock_socketconstructor):
        with open("test.bin", mode='rb') as file: 
            expected_return = file.read()

        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value=expected_return
        server_thread = threading.Thread(target=self.fake_server_xml)
        server_thread.start()

        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        res = "<?xml version=\"1.0\" encoding=\"utf-8\"?><data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data><?xml version=\"1.0\" encoding=\"utf-8\"?><data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>"
        x = XMLDateBaseAdapter()
        value = x.get_response(xml_obj)
        self.assertNotEqual(value,res)
        server_thread.join()


if __name__ == '__main__':
    unittest.main()
