#!/usr/bin/env python3
"""Organiza seu mapa em uma página Markdown. Não instala nem executa agentes."""
import argparse,json,sys
from pathlib import Path
CAMPOS=['nome','para_quem','resultado','experiencia','aprovacao_humana','demonstracao','oferta','fora_do_escopo','algo_seu','proximo_passo']
def validar(d):
 if not isinstance(d,dict):raise ValueError('Use um objeto JSON como kit/operacao-modelo.json.')
 faltam=[k for k in CAMPOS if not isinstance(d.get(k),str) or not d[k].strip()]
 if faltam:raise ValueError('Preencha: '+', '.join(faltam))
 roles=d.get('papeis')
 if not isinstance(roles,list) or not 1<=len(roles)<=8:raise ValueError('papeis deve conter de1a8papéis.')
 for i,r in enumerate(roles,1):
  if not isinstance(r,dict) or any(not isinstance(r.get(k),str) or not r[k].strip() for k in ['nome','recebe','entrega','chama_voce']):raise ValueError(f'Papel{i}: preencha nome, recebe, entrega e chama_voce.')
 return d
def montar(d):
 validar(d)
 linhas=['# '+d['nome'],'','Mapa de uma operação proposta. Este documento não comprova funcionamento, demanda ou renda.','','## O resultado que quero conduzir',d['resultado'],'','**Para quem:** '+d['para_quem'],'','**Experiência que orienta:** '+d['experiencia'],'','## Papéis da equipe']
 for r in d['papeis']:linhas+=['','### '+r['nome'],'- Recebe: '+r['recebe'],'- Entrega: '+r['entrega'],'- Chama você quando: '+r['chama_voce']]
 for title,key in [('Aprovação humana','aprovacao_humana'),('Primeira demonstração','demonstracao'),('Rascunho de oferta','oferta'),('Fora do escopo','fora_do_escopo'),('O que quero construir de meu','algo_seu'),('Próximo movimento','proximo_passo')]:linhas+=['','## '+title,d[key]]
 return '\n'.join(linhas)+'\n'
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('json');p.add_argument('--saida');p.add_argument('--sobrescrever',action='store_true');a=p.parse_args()
 try:
  doc=montar(json.loads(Path(a.json).read_text(encoding='utf-8-sig')))
  if a.saida:
   dest=Path(a.saida)
   if dest.exists() and not a.sobrescrever:raise ValueError('Saída já existe. Escolha outro nome ou use --sobrescrever.')
   dest.write_text(doc,encoding='utf-8');print('Mapa escrito em '+str(dest))
  else:print(doc,end='')
  return 0
 except (ValueError,OSError,UnicodeError) as e:print('ERRO: '+str(e),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
