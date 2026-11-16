# Ingresos con IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Renda com IA](guia/assets/banner-es.jpg)](https://inematds.github.io/renda-com-ia/guia/es/)

## Qué es

Quieres seguir siendo útil en el trabajo mientras la inteligencia artificial asume más tareas. Ingresos con IA es un kit gratuito para profesionales que quieren investigar alternativas sin decidirse solo por el entusiasmo o el miedo. Compara opciones, ofrece fichas para conversar con quienes contratan y organiza una experiencia de 30 días. Puedes leer la guía y completar los documentos en una hoja de cálculo o un editor de texto; la verificación automática local es opcional. El resultado es una hipótesis mejor investigada, sin promesas de ingresos ni de contratación.

## Guía de uso

https://inematds.github.io/renda-com-ia/guia/es/

## Primer uso

Descarga [el kit ZIP](renda-com-ia-kit.zip), extráelo y abre kit/COMECE-AQUI.md. Completa las fichas en un editor y los CSV en una hoja de cálculo. No necesitas Git, IA ni una clave de servicio.

Verificación opcional con Python3, desde la carpeta extraída:

```bash
python3 scripts/conferir.py kit/exemplo.csv
```

En Windows: `py -3 scripts/conferir.py kit/exemplo.csv`. Resultado: agentes y midia con 6/6 campos. Esto verifica que los campos estén completos, no la veracidad de los datos ni los ingresos futuros.

Para tus datos, copia kit/modelo.csv como kit/minha-investigacao.csv, complétalo y reemplaza la ruta en el comando. Códigos: 0 completo, 1 faltan campos, 2 archivo no válido.

## Verificación

```bash
python3 scripts/testar.py
```

## Límites y fuentes

Seis hipótesis, sin clasificación salarial. Ejemplo ficticio. El plan de 30 días no es un plazo de capacitación. Kit en portugués, guía y README en PT/EN/ES. [Fuentes](FONTES.md).
