# Sistema Especialista de Suporte Tecnico

import unicodedata

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


dados = pd.DataFrame({
    "roteador": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "wifi":     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    "outro":    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    "problema": [
        "roteador", "roteador", "roteador", "roteador",
        "wifi", "wifi", "wifi", "wifi",
        "provedor", "provedor", "dispositivo", "dispositivo",
        "provedor", "provedor", "dispositivo", "dispositivo",
    ],
})

colunas = ["roteador", "wifi", "outro"]
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(dados[colunas], dados["problema"])


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(letra for letra in texto if unicodedata.category(letra) != "Mn")


def perguntar(texto):
    respostas_sim = {
        "s", "sim",
    }
    
    respostas_nao = {
        "n", "nao",
    }

    resposta = normalizar(input(f"\n{texto} (s/n): "))
    if resposta in {"exit", "sair"}:
        print("\nBeleza! Ate mais.")
        raise SystemExit

    while resposta not in respostas_sim and resposta not in respostas_nao:
        resposta = normalizar(input("Nao entendi. Pode responder sim ou nao? "))
        if resposta in {"exit", "sair"}:
            print("\nBeleza! Ate mais.")
            raise SystemExit

    return int(resposta in respostas_sim)


def diagnosticar():
    print("\nVamos ver o que esta acontecendo!\n")

    roteador = perguntar("As luzes do roteador estao acesas?")
    wifi = perguntar("O nome da rede Wi-Fi aparece?")
    outro = perguntar("Outro aparelho consegue acessar a internet?")
    internet_lenta = perguntar("A internet esta muito lenta?")
    usa_cabo = perguntar("Voce esta usando cabo de rede?")
    cabo = perguntar("O cabo esta conectado direitinho?") if usa_cabo else 1
    problema_recente = perguntar("A internet parou de funcionar de repente?")
    sites_abrem = perguntar("Voce consegue acessar algum site?")
    queda_frequente = perguntar("A internet cai e volta varias vezes?")
    reiniciou = perguntar("Voce ja tentou reiniciar o roteador?")

    caso = pd.DataFrame([[roteador, wifi, outro]], columns=colunas)
    previsao = modelo.predict(caso)[0]
    regras = []

    if roteador == 0:
        regras.append((
            "R1 - Roteador desligado",
            "Confira a tomada, a fonte e a energia do roteador.",
        ))
    elif wifi == 0:
        regras.append((
            "R2 - Problema na rede Wi-Fi",
            "Ative o Wi-Fi e tente reiniciar o roteador.",
        ))
    elif outro == 1:
        regras.append((
            "R3 - Problema no dispositivo",
            "Confira a configuracao de rede do dispositivo que esta falhando.",
        ))
    else:
        regras.append((
            "R4 - Possivel falha no provedor",
            "Reinicie o roteador. Se continuar, fale com seu provedor.",
        ))

    if internet_lenta and not queda_frequente:
        regras.append((
            "R5 - Internet lenta",
            "Veja quantos aparelhos estao conectados e compare com sua velocidade contratada.",
        ))

    if usa_cabo and not cabo:
        regras.append((
            "R6 - Problema no cabo de rede",
            "Confira a conexao do cabo e veja se ele esta danificado.",
        ))

    if problema_recente and not reiniciou:
        regras.append((
            "R7 - Falha recente",
            "Tente reiniciar o roteador e confira os cabos.",
        ))

    if not sites_abrem and wifi:
        regras.append((
            "R8 - Possivel problema de DNS",
            "Confira as configuracoes de DNS do dispositivo.",
        ))

    if queda_frequente and not reiniciou:
        regras.append((
            "R9 - Instabilidade",
            "Verifique o roteador e os cabos. Observe se a conexao continua caindo.",
        ))

    if queda_frequente and reiniciou:
        regras.append((
            "R10 - Instabilidade persistente",
            "Como reiniciar nao resolveu, talvez seja melhor falar com o provedor.",
        ))

    print("\n" + "=" * 45)
    print("RESULTADO")
    print("=" * 45)
    print("Minha ideia:", previsao)
    print("\nO que podemos conferir:")

    for titulo, sugestao in regras:
        print(f"\n{titulo}")
        print(f"Sugestao: {sugestao}")

def main():
    print("=" * 45)
    print("SUPORTE TECNICO")
    print("=" * 45)

    while True:
        diagnosticar()
        if not perguntar("\nQuer analisar outra vez?"):
            print("\nBeleza! Ate mais.")
            break


if __name__ == "__main__":
    main()
