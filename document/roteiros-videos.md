# Roteiros de apresentação

Gravar dois vídeos separados, cada um com até 5 minutos, usando tela e sua própria
explicação. Os roteiros orientam a demonstração; ensaie para entender e explicar os
resultados. Publicar no YouTube como **não listado** e testar os links sem estar logado.
Não filmar tokens, contas pessoais ou dados de outros projetos.

## Vídeo 1 — Machine Learning

Duração planejada: 4min40s.

| Tempo | Tela | Explicação sugerida |
|---|---|---|
| 0:00–0:25 | README e título do notebook | Apresentar nome, RM, FarmTech e previsão de rendimento. |
| 0:25–1:05 | Seções 2 e 3 | Mostrar 156 linhas, quatro culturas e 39 cenários. Explicar por que o mesmo clima fica inteiro no treino ou no teste. Apontar a dúvida de unidades, preservadas no CSV. |
| 1:05–1:40 | Gráficos da seção 4 | Mostrar que culturas têm escalas muito diferentes. Isso motiva a referência de média por cultura. |
| 1:40–2:35 | Seção 5 | Nomear os cinco algoritmos, mostrar o pipeline e a tabela de validação. A escolha usa RMSE de CV; o teste fica reservado. |
| 2:35–3:15 | Seção 6 | Mostrar Random Forest, RMSE 4.730,49 e redução de 12,8% contra a referência. R² global de 0,995 não significa 99,5% de acerto: cacau tem R² negativo no teste. |
| 3:15–4:00 | Seções 7 e 8 | Mostrar três clusters, silhueta de aproximadamente 0,399 e forte sobreposição de produtividade. Nenhum outlier IQR de rendimento; 13 cenários sinalizados pelo limiar heurístico do Isolation Forest. Nenhum removido. |
| 4:00–4:25 | Executar a célula de inferência | Mostrar cultura e quatro entradas e o resultado numérico. A linha é uma demonstração do teste, não sensor real. |
| 4:25–4:40 | Conclusão | Citar a amostra pequena, unidades e falta de datas/solo/manejo. Novas safras são necessárias para validar uso real. |

Antes de gravar, execute o notebook completo. Na gravação, exiba as saídas já calculadas
e rode a célula de inferência; não é necessário consumir o vídeo esperando todos os grids.

## Vídeo 2 — Computação em nuvem

Duração planejada: 4min30s.

Abra o link salvo no README. As duas linhas da calculadora são cenários alternativos.

| Tempo | Tela | Explicação sugerida |
|---|---|---|
| 0:00–0:25 | README, Entrega 2 | Apresentar API para sensores e os requisitos: Linux, 2 vCPUs, 1 GiB, até 5 Gigabit e 50 GB. |
| 0:25–1:25 | Editar cenário da Virgínia na calculadora | Mostrar us-east-1, Linux, uma t4g.micro, 2 vCPUs/1 GiB/rede. Seleção Sob demanda, uso 100%. Destacar ARM64. |
| 1:25–2:05 | Abrir EBS e Mostrar cálculos | Mostrar Magnético (geração anterior), 50 GB, sem snapshots. EC2: 0,0084 × 730 = 6,132; disco: 0,05 × 50 = 2,50; subtotal 8,63. |
| 2:05–2:50 | Cenário de São Paulo | Mostrar sa-east-1 e parâmetros iguais. EC2: 0,0134 × 730 = 9,782; disco: 0,12 × 50 = 6,00; subtotal 15,78. |
| 2:50–3:20 | Tabela e gráfico no README | Virgínia economiza US$ 7,15/mês. O total 24,41 da calculadora soma as duas alternativas, não uma implantação escolhida. |
| 3:20–3:55 | Justificativa e arquitetura | Escolher São Paulo diante da restrição de armazenar no exterior. Explicar hipótese de menor latência, sem alegar medição. Backups e logs também ficam no Brasil. |
| 3:55–4:30 | Limites da estimativa | Não inclui I/O magnético, IPv4, tráfego, impostos e outros itens. 100% de uso significa ligada 730h, não CPU ilimitada. Não houve implantação real; 1 GiB precisa ser testado. |

Use Cancelar ao sair das telas de edição se quiser preservar a estimativa salva.
Não use a coluna de Savings Plans para explicar o preço On-Demand.

## Publicação

1. Exporte cada vídeo com áudio inteligível e números legíveis; confira a duração.
2. No YouTube, escolha **não listado**.
3. Substitua os dois campos de vídeo no README por links reais.
4. Verifique cada vídeo em janela anônima.
5. Faça a revisão final e o último commit antes do envio e do prazo.
