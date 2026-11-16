# Renda com IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Renda com IA](guia/assets/banner.jpg)](https://inematds.github.io/renda-com-ia/guia/)

## O que é

Você já conhece problemas, clientes e decisões que uma ferramenta sozinha não entende. Renda com IA é um kit gratuito para transformar essa experiência no desenho de uma operação apoiada por agentes. Você vê uma possibilidade concreta, distribui os papéis, prepara uma demonstração e organiza uma oferta. O kit também ajuda a reconhecer o que pode continuar seu: método, repertório, reputação e autonomia. Os documentos funcionam em um editor; um gerador local opcional monta seu mapa em uma página.

## Veja a possibilidade

Sua experiência pode orientar uma equipe de IA para organizar pedidos, preparar rascunhos e acompanhar uma entrega. Você dirige e revisa. O kit ajuda a passar dessa visão a um mapa e a uma oferta; não instala nem executa agentes.

[Guia completo](https://inematds.github.io/renda-com-ia/guia/) · [Vídeos](https://inematds.github.io/renda-com-ia/videos/)

## Comece pela sua visão

Baixe [o kit](renda-com-ia-kit.zip), extraia e abra kit/COMECE-AQUI.md. Depois use kit/visao.md, equipe.md, oferta.md e algo-seu.md. Você pode preencher os documentos num editor.

## Gerador local opcional

Com Python 3, dentro da pasta extraída:

```bash
python3 scripts/montar_operacao.py kit/operacao-exemplo.json --saida exemplo-operacao.md
```

Windows: py -3 no lugar de python3. Abra exemplo-operacao.md para ver o mapa pronto. Copie kit/operacao-modelo.json como kit/minha-operacao.json e preencha para seu caso, preservando as chaves. Escolha um nome de saída novo.

O programa organiza o documento; não comprova funcionamento, demanda ou renda. Exemplos são fictícios. [Fontes e limites](FONTES.md).

## Verificação

```bash
python3 scripts/testar_operacao.py
python3 scripts/testar.py
```

## Comparação das abordagens

O primeiro vídeo está preservado: https://www.youtube.com/watch?v=aQoAdOuU_K4 . O segundo está em produção com a visão de possibilidade e construção. [Plano de comparação](comparacao/PLANO.md) e [guia A congelado](comparacao/a/guia/). É comparação editorial, com datas e exposição diferentes.

[Novo vídeo: sua experiência pode dirigir uma equipe de IA](https://www.youtube.com/watch?v=zOCYbP3yoR8) · [Player](https://inematds.github.io/renda-com-ia/videos/possibilidades/)
