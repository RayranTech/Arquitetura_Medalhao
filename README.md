🏅 Arquitetura Medalhão – Projeto de Dados

Este projeto implementa o padrão Arquitetura Medalhão (Medallion Architecture) para organização e processamento de dados, estruturado em camadas Bronze, Silver e Gold, garantindo qualidade, governança e escalabilidade no pipeline de dados.

📂 Estrutura de Pastas
.
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── ETL/
│   ├── extraction/
│   ├── transform/
│   └── load/
│
└── excel/
    └── modelo_vendas.xlsx

🥉 Bronze – Dados Brutos

Camada responsável pelo armazenamento dos dados brutos (raw data).

Dados ingeridos exatamente como foram recebidos

Sem transformações significativas

Pode conter inconsistências

Mantém histórico original

📌 Objetivo: Garantir rastreabilidade e preservar a integridade dos dados de origem.

🥈 Silver – Dados Tratados

Camada intermediária onde os dados passam por tratamento.

Limpeza de dados

Remoção de duplicidades

Tratamento de valores nulos

Padronização de tipos e formatos

Aplicação de regras de negócio iniciais

📌 Objetivo: Garantir consistência e qualidade para análises futuras.

🥇 Gold – Dados Refinados

Camada analítica com dados modelados para consumo.

Agregações

Indicadores de desempenho (KPIs)

Estrutura otimizada para consultas

Modelagem orientada ao negócio

📌 Objetivo: Disponibilizar dados estratégicos e prontos para consumo analítico.

📊 Excel – Dados Prontos para Uso

A pasta excel/ contém o arquivo final com:

Dados limpos

Estrutura organizada

Tipagem correta

Pronto para análise

Uso direto em dashboards, relatórios ou tomada de decisão

Essa camada representa o produto final do pipeline, sendo a interface de consumo para usuários de negócio.

📌 Objetivo: Entregar dados confiáveis, organizados e prontos para uso imediato.

🔄 ETL

A pasta ETL/ organiza o fluxo do pipeline:

📥 Extraction

Responsável por extrair dados das fontes originais.

🔄 Transform

Aplica regras de limpeza, padronização e modelagem.

📤 Load

Carrega os dados nas respectivas camadas:
Bronze → Silver → Gold → Excel

🔁 Fluxo Completo
Fonte de Dados
      ↓
Extraction
      ↓
Bronze (Raw)
      ↓
Transform
      ↓
Silver (Tratado)
      ↓
Transform (Modelagem)
      ↓
Gold (Refinado)
      ↓
Excel (Pronto para Uso)

🎯 Benefícios da Arquitetura

Separação clara de responsabilidades

Alta rastreabilidade

Escalabilidade

Organização modular

Entrega confiável para área de negócio
