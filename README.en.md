# Renda com IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Renda com IA](guia/assets/banner-en.jpg)](https://inematds.github.io/renda-com-ia/guia/en/)

## What It Is

You already know problems, customers, and decisions that a tool alone cannot understand. Renda com IA is a free kit for turning that experience into the design of an operation supported by agents. You see a concrete opportunity, assign roles, prepare a demonstration, and organize an offer. The kit also helps you recognize what can remain yours: methods, expertise, reputation, and autonomy. The documents work in an editor; an optional local generator builds your map on a page.

## See the Opportunity

Your experience can guide an AI team in organizing requests, preparing drafts, and tracking a delivery. You direct and review. The kit helps you move from that vision to a map and an offer; it does not install or run agents.

[Complete guide](https://inematds.github.io/renda-com-ia/guia/en/) · [Videos](https://inematds.github.io/renda-com-ia/videos/)

## Start with Your Vision

Download [the kit](renda-com-ia-kit.zip), extract it, and open kit/COMECE-AQUI.md. Then use kit/visao.md, equipe.md, oferta.md, and algo-seu.md. You can fill in the documents in an editor.

## Optional Local Generator

With Python 3, from inside the extracted folder:

```bash
python3 scripts/montar_operacao.py kit/operacao-exemplo.json --saida exemplo-operacao.md
```

Windows: use py -3 instead of python3. Open exemplo-operacao.md to see the completed map. Copy kit/operacao-modelo.json as kit/minha-operacao.json and fill it in for your case, preserving the keys. Choose a new output name.

The program organizes the document; it does not prove functionality, demand, or income. Examples are fictional. [Sources and limitations](FONTES.md).

## Verification

```bash
python3 scripts/testar_operacao.py
python3 scripts/testar.py
```

## Comparing the Approaches

The first video is preserved: https://www.youtube.com/watch?v=aQoAdOuU_K4 . The second is in production with the vision of possibility and building. [Comparison plan](comparacao/PLANO.md) and [frozen guide A](comparacao/a/guia/). This is an editorial comparison, with different dates and exposure.

[New video: your experience can lead an AI team](https://www.youtube.com/watch?v=zOCYbP3yoR8) · [Player](https://inematds.github.io/renda-com-ia/videos/possibilidades/)
