"""Regressão dos contratos do CSV: exemplo, vazio, incompleto e malformado."""
import tempfile,unittest
from pathlib import Path
from conferir import conferir,FIELDS
ROOT=Path(__file__).resolve().parent.parent
class Contrato(unittest.TestCase):
 def test_exemplo(self):
  r=conferir(ROOT/'kit/exemplo.csv');self.assertEqual(len(r['caminhos']),2);self.assertTrue(all(x['preenchidos']==6 for x in r['caminhos']))
 def test_modelo(self):
  r=conferir(ROOT/'kit/modelo.csv');self.assertTrue(all(x['faltam']==FIELDS[1:] for x in r['caminhos']))
 def validar_erro(self,txt):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'x.csv';p.write_text(txt)
   with self.assertRaises(ValueError):conferir(p)
 def test_vazio(self):self.validar_erro(','.join(FIELDS)+'\n')
 def test_colunas(self):self.validar_erro(','.join(FIELDS)+'\nagentes,a,b,c,d,e,f,extra\n')
 def test_id(self):self.validar_erro(','.join(FIELDS)+'\nfalso,a,b,c,d,e,continuar\n')
 def test_decisao(self):self.validar_erro(','.join(FIELDS)+'\nagentes,a,b,c,d,e,enriquecer\n')
 def test_duplicado(self):self.validar_erro(','.join(FIELDS)+'\nagentes,a,b,c,d,e,continuar\nagentes,a,b,c,d,e,ajustar\n')
if __name__=='__main__':unittest.main()
