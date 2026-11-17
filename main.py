
# Sistema especialista de suporte técnico

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Dados simulados
dados = pd.DataFrame({
    "roteador": [0,0,0,0, 1,1,1,1, 1,1,1,1, 1,1,1,1],
    "wifi":     [0,0,0,0, 0,0,0,0, 1,1,1,1, 1,1,1,1],
    "outro":    [0,0,0,0, 0,0,1,1, 0,0,1,1, 0,0,1,1],
    "problema": [
        "roteador", "roteador", "roteador", "roteador",
        "wifi", "wifi", "wifi", "wifi",
        "provedor", "provedor", "dispositivo", "dispositivo",
        "provedor", "provedor", "dispositivo", "dispositivo"
    ]
})

# 2. Treinamento do modelo
X = dados[["roteador", "wifi", "outro"]]
y = dados["problema"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_treino, y_treino)


# 3. Perguntas ao usuário
def perguntar(pergunta):

    sim = [
        "s", "sim", "ss"
    ]

    nao = [
        "n", "não", "nao"
    ]

    resposta = input(pergunta + " (s/n): ").strip().lower()

    while resposta not in sim and resposta not in nao:
        resposta = input("Não entendi. Responda sim ou não: ").strip().lower()

    if resposta in sim:
        return 1
    else:
        return 0


# 4. Análise do problema
def analisar():

    print("\nVamos verificar sua internet!\n")

    roteador = perguntar("As luzes do roteador estão acesas?\n")
    wifi = perguntar("A rede Wi-Fi aparece?\n")
    outro = perguntar("Outro aparelho consegue acessar a internet?\n")

    caso = pd.DataFrame(
        [[roteador, wifi, outro]],
        columns=["roteador", "wifi", "outro"]
    )

    # Previsão do aprendizado de máquina
    previsao = modelo.predict(caso)[0]

    # 5. Regras do sistema especialista
    if roteador == 0:
        regra = "R1"
        resposta = "Confira a tomada e a fonte do roteador."

    elif wifi == 0:
        regra = "R2"
        resposta = "Verifique se o Wi-Fi está ativado e reinicie o roteador."

    elif outro == 1:
        regra = "R3"
        resposta = "O problema pode estar no dispositivo que você está usando."

    else:
        regra = "R4"
        resposta = "Reinicie o roteador. Se continuar, fale com seu provedor."

    # 6. Resultado
    print("\n--- Resultado ---")
    print("Modelo identificou:", previsao)
    print("Regra aplicada:", regra)
    print("Sugestão:", resposta)

    print("\nEssa é uma orientação inicial.")



# 7. Programa principal
def main():

    print("=" * 40)
    print("SISTEMA ESPECIALISTA DE SUPORTE TÉCNICO")
    print("=" * 40)

    while True:
        analisar()

        continuar = perguntar("\nDeseja analisar outro problema?")

        if continuar == 0:
            print("\nBeleza! Até mais.")
            break


if __name__ == "__main__":
    main()
