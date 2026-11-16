import copy,json,unittest
from pathlib import Path
from montar_operacao import montar,validar
EX=json.loads((Path(__file__).resolve().parent.parent/'kit/operacao-exemplo.json').read_text())
class Operacao(unittest.TestCase):
 def test_exemplo(self):
  s=montar(EX);self.assertIn('Aprovação humana',s);self.assertIn(EX['fora_do_escopo'],s)
 def test_sem_revisao(self):
  d=copy.deepcopy(EX);d['aprovacao_humana']=''
  with self.assertRaises(ValueError):validar(d)
 def test_papel_sem_gatilho(self):
  d=copy.deepcopy(EX);del d['papeis'][0]['chama_voce']
  with self.assertRaises(ValueError):validar(d)
 def test_sem_papeis(self):
  d=copy.deepcopy(EX);d['papeis']=[]
  with self.assertRaises(ValueError):validar(d)
 def test_nao_objeto(self):
  with self.assertRaises(ValueError):validar([])
 def test_modelo_incompleto(self):
  d=json.loads((Path(__file__).resolve().parent.parent/'kit/operacao-modelo.json').read_text())
  with self.assertRaises(ValueError):validar(d)
if __name__=='__main__':unittest.main()
