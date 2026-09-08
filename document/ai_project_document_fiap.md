# Mapa da documentação — FarmTech Fase 5

- O relatório técnico completo de Machine Learning está no notebook, acessível pelo README.
- A entrega de nuvem está no README, com evidências em `assets/aws/`.
- `aws-cotacao.json`: transcrição estruturada dos parâmetros e preços unitários da interface.
- `aws-estimativa.json`: exportação AWS normalizada para JSON UTF-8 válido.
- `other/aws-exportacao-original.json`: bytes originais do download da calculadora.
  A exportação trouxe codificação de byte único e caracteres de controle em travessões;
  a normalização corrige a codificação e os controles, preservando números e configurações.
  Pequenas diferenças anuais da exportação decorrem do arredondamento da calculadora;
  a comparação deste trabalho usa os preços unitários e subtotais mensais.
- `roteiros-videos.md`: demonstrações separadas de até cinco minutos.
- `checklist-entrega.md`: pendências acadêmicas e conferência final.
