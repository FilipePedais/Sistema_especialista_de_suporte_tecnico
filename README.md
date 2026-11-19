# Suporte Técnico

Um projeto simples em Python que faz perguntas sobre a conexão com a internet, sugere uma possível causa e apresenta dicas para resolver o problema.

O programa combina um modelo de aprendizado de máquina com regras de diagnóstico. A ideia é ajudar a investigar problemas comuns, não substituir o suporte do provedor.

## Requisitos

- Python 3.8 ou superior
- pandas
- scikit-learn

## Instalação

No terminal, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Como executar

Na pasta do projeto, rode:

```bash
python main.py
```

Responda às perguntas com `s` ou `sim` para sim e `n` ou `não` para não. Maiúsculas e acentos são aceitos. Se a resposta não for reconhecida, o programa pede para tentar novamente.

### Sair a qualquer momento

Digite `exit` ou `sair` em qualquer pergunta para encerrar o programa.

## Perguntas

O programa pergunta sobre:

- As luzes do roteador estão acesas?
- O nome da rede Wi-Fi aparece?
- Outro aparelho consegue acessar a internet?
- A internet está muito lenta?
- Você está usando cabo de rede?
- Se estiver usando cabo, ele está conectado direitinho?
- A internet parou de funcionar de repente?
- Você consegue acessar algum site?
- A internet cai e volta várias vezes?
- Você já tentou reiniciar o roteador?

A pergunta sobre o cabo só aparece quando a resposta sobre o uso de cabo é sim.

## Como funciona

### Modelo de aprendizado de máquina

O `DecisionTreeClassifier`, do scikit-learn, é treinado com exemplos simulados que estão no próprio código. Com as respostas sobre o roteador, a rede Wi-Fi e outro aparelho, ele sugere uma categoria:

- `roteador`
- `wifi`
- `provedor`
- `dispositivo`

Essa sugestão aparece como **“Minha ideia”** no resultado.

### Regras de diagnóstico

Além da sugestão do modelo, o programa verifica as respostas e pode apresentar uma ou mais regras:

| Regra | Quando se aplica | Sugestão |
|---|---|---|
| R1 - Roteador desligado | As luzes do roteador não estão acesas. | Confira a tomada, a fonte e a energia do roteador. |
| R2 - Problema na rede Wi-Fi | O roteador está ligado, mas o nome da rede não aparece. | Ative o Wi-Fi e tente reiniciar o roteador. |
| R3 - Problema no dispositivo | O roteador está ligado, a rede aparece e outro aparelho acessa a internet. | Confira a configuração de rede do dispositivo com problema. |
| R4 - Possível falha no provedor | O roteador está ligado, a rede aparece e outro aparelho também não acessa a internet. | Reinicie o roteador. Se continuar, fale com seu provedor. |
| R5 - Internet lenta | A internet está lenta e não cai com frequência. | Confira quantos aparelhos estão conectados e a velocidade contratada. |
| R6 - Problema no cabo de rede | Está usando cabo, mas ele não está conectado corretamente. | Confira a conexão e veja se o cabo está danificado. |
| R7 - Falha recente | A internet parou de repente e o roteador ainda não foi reiniciado. | Tente reiniciar o roteador e confira os cabos. |
| R8 - Possível problema de DNS | Nenhum site abre, mas a rede Wi-Fi aparece. | Confira as configurações de DNS do dispositivo. |
| R9 - Instabilidade | A conexão cai com frequência e o roteador ainda não foi reiniciado. | Verifique o roteador e os cabos; observe se as quedas continuam. |
| R10 - Instabilidade persistente | A conexão cai com frequência mesmo depois de reiniciar o roteador. | Fale com o provedor. |

As regras R1 a R4 são alternativas: o programa aplica a primeira que corresponder às respostas. As regras R5 a R10 são verificadas separadamente e podem aparecer junto com uma delas.

Depois do resultado, você pode iniciar outra análise respondendo sim à pergunta **“Quer analisar outra vez?”**.

## Limitações

- Os exemplos de treinamento são fictícios e em pequena quantidade.
- As regras são fixas e cobrem apenas alguns problemas comuns.
- O diagnóstico é uma sugestão; ele pode não identificar a causa real da falha.

## Estrutura do projeto

```text
Sistema_especialista_de_suporte_tecnico/
├── main.py
├── README.md
└── requirements.txt
```

## Objetivo

Demonstrar, de forma prática, como combinar um modelo simples de aprendizado de máquina com regras para investigar problemas de conexão e sugerir o que conferir.
