# Renda com IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Renda com IA](guia/assets/banner.jpg)](https://inematds.github.io/renda-com-ia/guia/)

## O que é

Você quer continuar útil no trabalho enquanto a inteligência artificial assume mais tarefas. Renda com IA é um kit gratuito para profissionais que querem investigar alternativas sem decidir só pelo entusiasmo ou pelo medo. Ele compara caminhos, oferece fichas para conversar com quem contrata e organiza uma experiência de 30 dias. Você pode ler o guia e preencher os documentos numa planilha ou editor de texto; a conferência automática local é opcional. O resultado é uma hipótese mais bem investigada, sem promessa de renda ou contratação.

## Guia de uso

https://inematds.github.io/renda-com-ia/guia/

## Primeiro uso

Baixe [o kit ZIP](renda-com-ia-kit.zip), extraia e abra kit/COMECE-AQUI.md. Preencha as fichas num editor e os CSVs numa planilha. Não precisa de Git, IA ou chave de serviço.

Conferência opcional com Python3, a partir da pasta extraída:

```bash
python3 scripts/conferir.py kit/exemplo.csv
```

No Windows: `py -3 scripts/conferir.py kit/exemplo.csv`. Saída: agentes e midia com 6/6 campos. Isso confere preenchimento, não a verdade dos dados nem renda futura.

Para seus dados, copie kit/modelo.csv como kit/minha-investigacao.csv, preencha e substitua o caminho no comando. Códigos: 0 completo, 1 faltam campos, 2 arquivo inválido.

## Verificação

```bash
python3 scripts/testar.py
```

## Limites e fontes

Seis hipóteses, sem ranking salarial. Exemplo fictício. Plano de 30 dias não é prazo de qualificação. Kit em português, guia e README em PT/EN/ES. [Fontes](FONTES.md).
