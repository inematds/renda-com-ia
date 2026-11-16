# Renda com IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Renda com IA](guia/assets/banner-es.jpg)](https://inematds.github.io/renda-com-ia/guia/es/)

## Qué es

Ya conoces problemas, clientes y decisiones que una herramienta por sí sola no entiende. Renda com IA es un kit gratuito para transformar esa experiencia en el diseño de una operación con apoyo de agentes. Ves una posibilidad concreta, distribuyes los roles, preparas una demostración y organizas una oferta. El kit también ayuda a reconocer lo que puede seguir siendo tuyo: método, experiencia, reputación y autonomía. Los documentos funcionan en un editor; un generador local opcional crea tu mapa en una página.

## Descubre la posibilidad

Tu experiencia puede orientar a un equipo de IA para organizar solicitudes, preparar borradores y acompañar una entrega. Tú diriges y revisas. El kit ayuda a pasar de esa visión a un mapa y una oferta; no instala ni ejecuta agentes.

[Guía completa](https://inematds.github.io/renda-com-ia/guia/es/) · [Videos](https://inematds.github.io/renda-com-ia/videos/)

## Empieza por tu visión

Descarga [el kit](renda-com-ia-kit.zip), extráelo y abre kit/COMECE-AQUI.md. Luego usa kit/visao.md, equipe.md, oferta.md y algo-seu.md. Puedes completar los documentos en un editor.

## Generador local opcional

Con Python 3, dentro de la carpeta extraída:

```bash
python3 scripts/montar_operacao.py kit/operacao-exemplo.json --saida exemplo-operacao.md
```

Windows: usa py -3 en lugar de python3. Abre exemplo-operacao.md para ver el mapa listo. Copia kit/operacao-modelo.json como kit/minha-operacao.json y complétalo para tu caso, conservando las claves. Elige un nombre nuevo para el archivo de salida.

El programa organiza el documento; no comprueba el funcionamiento, la demanda ni los ingresos. Los ejemplos son ficticios. [Fuentes y límites](FONTES.md).

## Verificación

```bash
python3 scripts/testar_operacao.py
python3 scripts/testar.py
```

## Comparación de los enfoques

El primer video se conserva: https://www.youtube.com/watch?v=aQoAdOuU_K4 . El segundo está en producción, con la visión de posibilidad y construcción. [Plan de comparación](comparacao/PLANO.md) y [guía A congelada](comparacao/a/guia/). Es una comparación editorial, con fechas y exposición diferentes.
