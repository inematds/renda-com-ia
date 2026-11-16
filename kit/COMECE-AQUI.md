# Você já tem experiência. Agora pode desenhar sua equipe de IA.

Aquela ideia que esbarra no seu tempo ou na falta de equipe pode ganhar forma. O Renda com IA ajuda você a enxergar uma entrega maior, organizar a execução e começar a construir algo seu.

## Primeiro, veja a possibilidade
Abra visao.md. Descreva uma cena em que o cliente chega com um problema e sua operação entrega algo útil. A experiência que você já tem orienta essa cena.

## Depois, dê forma à sua operação
1. equipe.md: distribua os papéis e escreva quando cada um precisa de você.
2. operacao-exemplo.json: veja uma operação de manutenção fictícia já preenchida.
3. oferta.md: transforme a demonstração num rascunho de oferta.
4. algo-seu.md: registre método, repertório, reputação e autonomia que quer construir.
5. plano-30-dias.md: escolha os primeiros movimentos.

Você pode preencher os documentos num editor. Não precisa de API ou de várias assinaturas.

## Quer gerar o mapa em uma página?
Python3 é opcional. A partir da pasta extraída renda-com-ia:
python3 scripts/montar_operacao.py kit/operacao-exemplo.json --saida exemplo-operacao.md

No Windows: py -3 no lugar de python3.
Abra exemplo-operacao.md: você verá resultado, papéis, aprovação humana, demonstração, oferta e próximo passo.
Para o seu caso, copie operacao-modelo.json como minha-operacao.json na pasta kit, preencha sem mudar as chaves e use esse caminho no comando. Escolha um nome de saída novo; --sobrescrever só se quiser substituir um arquivo seu.

O gerador organiza o documento. Não instala agentes, não executa tarefas nem envia dados. Na demonstração, use exemplos fictícios. Conectar sistemas reais é uma etapa posterior com permissões e conhecimento adequados.

## Materiais de apoio
caminhos.csv ajuda a reconhecer aplicações do seu repertório; entrevista.md e ficha.md ajudam a investigar o problema. O conferidor antigo scripts/conferir.py continua disponível para o CSV de investigação, separado do mapa JSON.

Comece pelo que gostaria de tornar possível. Use os testes para chegar lá.
