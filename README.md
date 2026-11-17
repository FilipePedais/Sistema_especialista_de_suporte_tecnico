# Sistema Especialista de Suporte Técnico

Projeto didático desenvolvido em Python que simula um sistema de suporte técnico para identificar possíveis problemas de conexão com a internet.

O programa faz algumas perguntas ao usuário, utiliza um modelo de aprendizado de máquina para sugerir uma categoria de problema e aplica regras para apresentar uma possível solução.

## Requisitos

- Python 3.8 ou superior
- pandas
- scikit-learn

## Como instalar

No terminal do VS Code, execute:

```bash
pip install pandas scikit-learn
```

## Como executar

```bash
python main.py
```

Responda às perguntas digitando sim ou não. O sistema também aceita outras formas de resposta, como `s`, `n`, `claro`, `aham`, `positivo`, `negativo`, `yes` e `no`.

## Como funciona

O sistema combina aprendizado de máquina com regras SE... ENTÃO....

| Componente | Onde está no código | O que faz |
|---|---|---|
| Base de dados | `dados` | Armazena exemplos simulados de problemas de internet |
| Fatos | `roteador`, `wifi` e `outro` | Armazena as respostas do usuário |
| Base de conhecimento | Condições `if` e `elif` | Contém as regras SE... ENTÃO... |
| Motor de inferência | Condições dentro de `analisar()` | Verifica as respostas e identifica qual regra deve ser aplicada |
| Interface | `perguntar()` e `main()` | Faz as perguntas e apresenta o resultado |

## Perguntas feitas

| Fato | Pergunta | Valores |
|---|---|---|
| `roteador` | As luzes do roteador estão acesas? | `1` = sim / `0` = não |
| `wifi` | A rede Wi-Fi aparece? | `1` = sim / `0` = não |
| `outro` | Outro aparelho consegue acessar a internet? | `1` = sim / `0` = não |

## Regras do sistema especialista

As regras representam as condições utilizadas pelo sistema para identificar possíveis problemas e apresentar sugestões.

### R1 – Problema no roteador

**SE:** As luzes do roteador não estão acesas (`roteador = 0`).

**ENTÃO:** O sistema identifica uma possível falta de energia ou problema na alimentação do roteador.

**Sugestão:** Confira a tomada e a fonte do roteador.

### R2 – Problema na rede Wi-Fi

**SE:** O roteador está ligado (`roteador = 1`) e a rede Wi-Fi não aparece (`wifi = 0`).

**ENTÃO:** O sistema identifica uma possível falha na transmissão da rede sem fio.

**Sugestão:** Verifique se o Wi-Fi está ativado e reinicie o roteador.

### R3 – Problema no dispositivo

**SE:** O roteador está ligado (`roteador = 1`), a rede Wi-Fi aparece (`wifi = 1`) e outro aparelho consegue acessar a internet (`outro = 1`).

**ENTÃO:** O sistema identifica uma possível falha no dispositivo utilizado pelo usuário.

**Sugestão:** Verifique as configurações de rede do dispositivo que está apresentando o problema.

### R4 – Possível problema no provedor

**SE:** O roteador está ligado (`roteador = 1`), a rede Wi-Fi aparece (`wifi = 1`) e outro aparelho não consegue acessar a internet (`outro = 0`).

**ENTÃO:** O sistema identifica que nenhum dos aparelhos consegue acessar a internet, indicando uma possível falha na conexão ou no provedor.

**Sugestão:** Reinicie o roteador. Se o problema continuar, entre em contato com seu provedor de internet.

## Como as regras são aplicadas

O sistema verifica as respostas do usuário seguindo uma ordem de condições:

```text
Respostas do usuário
        |
        v
   Verifica R1
        |
   Se não atender
        v
   Verifica R2
        |
   Se não atender
        v
   Verifica R3
        |
   Se não atender
        v
   Aplica R4
        |
        v
   Apresenta o resultado
```

A primeira regra compatível com as respostas é aplicada. Por isso, o sistema apresenta uma única sugestão por análise.

## Exemplo de execução

**Entradas:**
- Luzes do roteador acesas: sim
- Rede Wi-Fi aparece: sim
- Outro aparelho acessa a internet: não

**Resultado:**

```text
--- Resultado ---

Modelo identificou: provedor
Regra aplicada: R4

Sugestão:
Reinicie o roteador. Se continuar,
fale com seu provedor.

Essa é uma orientação inicial.
O modelo utiliza exemplos fictícios para fins de estudo.
```

## Aprendizado de máquina

O projeto utiliza o algoritmo `DecisionTreeClassifier`, disponível na biblioteca scikit-learn.

O modelo é treinado com exemplos simulados de problemas de internet. Depois do treinamento, ele recebe as respostas do usuário e prevê uma categoria:

- `roteador`
- `wifi`
- `provedor`
- `dispositivo`

O programa também calcula a acurácia e apresenta a matriz de confusão para avaliar o resultado do modelo.

A previsão do modelo é apresentada separadamente da regra aplicada. Assim, é possível observar a participação do aprendizado de máquina e das regras no diagnóstico.

## Limitações

- Os dados utilizados no treinamento são fictícios e foram criados apenas para fins didáticos.
- O modelo utiliza uma quantidade pequena de exemplos.
- As regras são fixas e foram escritas manualmente.
- O sistema considera apenas alguns problemas básicos de conexão com a internet.
- As sugestões não garantem a identificação da causa real do problema.

## Estrutura do projeto

```text
Sistema_especialista_de_suporte_tecnico/
│
├── main.py
├── README.md
└── requirements.txt
```

## Objetivo do projeto

O objetivo é demonstrar de forma simples como o aprendizado de máquina pode ser combinado com regras de um sistema especialista para analisar informações, identificar possíveis problemas e apresentar sugestões ao usuário.
