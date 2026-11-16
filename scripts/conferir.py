#!/usr/bin/env python3
"""Confere preenchimento de uma investigação local. Não classifica carreiras."""
import argparse,csv,json,sys
from pathlib import Path
IDS={'agentes','infra','avaliacao','midia','vendas','negocio'}
FIELDS=['id','experiencia','problema','conversa','evidencia','proximo_passo','decisao']
DECISIONS={'continuar','ajustar','abandonar','pesquisar'}
def conferir(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f)
        if reader.fieldnames!=FIELDS: raise ValueError('Cabeçalho incorreto. Use kit/modelo.csv sem mudar as colunas.')
        rows=list(reader)
    if not rows: raise ValueError('Arquivo vazio: preencha pelo menos um caminho.')
    seen=set();result=[]
    for n,r in enumerate(rows,2):
        if None in r or any(v is None for v in r.values()): raise ValueError(f'Linha{n}: número de colunas incorreto. Use aspas em textos com vírgula.')
        r={k:v.strip() for k,v in r.items()};ident=r['id']
        if ident not in IDS:raise ValueError(f'Linha{n}: id desconhecido: {ident}.')
        if ident in seen:raise ValueError(f'Linha{n}: id duplicado: {ident}.')
        seen.add(ident)
        if r['decisao'] and r['decisao'] not in DECISIONS:raise ValueError(f'Linha{n}: decisão inválida. Use continuar, ajustar, abandonar ou pesquisar.')
        missing=[k for k in FIELDS[1:] if not r[k]]
        result.append({'id':ident,'preenchidos':6-len(missing),'total':6,'faltam':missing,'decisao':r['decisao'] or 'pendente'})
    return {'caminhos':result,'aviso':'Confere preenchimento; não verifica a verdade dos dados nem prevê renda.'}
def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('csv');a.add_argument('--json',action='store_true');args=a.parse_args()
    try:r=conferir(args.csv)
    except (ValueError,OSError,UnicodeError,csv.Error) as e:print(f'ERRO: {e}',file=sys.stderr);return 2
    if args.json:print(json.dumps(r,ensure_ascii=False,indent=2))
    else:
        for item in r['caminhos']:print(f"{item['id']}: {item['preenchidos']}/6 campos; decisão={item['decisao']}; faltam={','.join(item['faltam']) or 'nenhum'}")
        print(r['aviso'])
    return 1 if any(x['faltam'] for x in r['caminhos']) else 0
if __name__=='__main__':sys.exit(main())
