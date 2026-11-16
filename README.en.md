# Income with AI

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Renda com IA](guia/assets/banner-en.jpg)](https://inematds.github.io/renda-com-ia/guia/en/)

## What it is

You want to remain useful at work as artificial intelligence takes on more tasks. Renda com IA is a free kit for professionals who want to explore alternatives without making decisions based only on enthusiasm or fear. It compares paths, provides worksheets for talking with potential employers, and organizes a 30-day experience. You can read the guide and fill out the documents in a spreadsheet or text editor; local automated checking is optional. The result is a better-researched hypothesis, with no promise of income or employment.

## User guide

https://inematds.github.io/renda-com-ia/guia/en/

## First use

Download [the ZIP kit](renda-com-ia-kit.zip), extract it, and open kit/COMECE-AQUI.md. Fill out the worksheets in an editor and the CSVs in a spreadsheet. Git, AI, or a service key aren’t required.

Optional check with Python3, from the extracted folder:

```bash
python3 scripts/conferir.py kit/exemplo.csv
```

On Windows: `py -3 scripts/conferir.py kit/exemplo.csv`. Output: `agentes` and `midia` with 6/6 fields. This checks completion, not the accuracy of the data or future income.

For your data, copy kit/modelo.csv as kit/minha-investigacao.csv, fill it out, and replace the path in the command. Codes: 0 complete, 1 missing fields, 2 invalid file.

## Verification

```bash
python3 scripts/testar.py
```

## Limitations and sources

Six hypotheses, with no salary ranking. Fictional example. A 30-day plan is not a qualification timeline. Kit in Portuguese, guide and README in PT/EN/ES. [Sources](FONTES.md).
