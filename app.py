def assistente():
    print("📘 Assistente Financeiro - Fundação Bradesco")
    print("Digite 'sair' para encerrar.\n")

    ultimo_calculo = 0

    while True:
        user = input("Você: ").lower()

        if user == "sair":
            print("Assistente: Encerrando atendimento. Bons estudos! 📚")
            break

        # Conceito financeiro
        elif "cdb" in user:
            print("Assistente: CDB é um investimento de renda fixa onde você empresta dinheiro ao banco e recebe juros.")

        elif "poupança" in user:
            print("Assistente: Poupança é um tipo de investimento com baixo risco e rendimento mensal.")

        # Cálculo simples
        elif "rende" in user:
            try:
                palavras = user.split()
                numeros = [float(p) for p in palavras if p.replace('.', '').isdigit()]

                valor = numeros[0]
                meses = int(numeros[1])

                taxa = 0.01  # 1% ao mês (educacional)
                montante = valor * (1 + taxa) ** meses

                ultimo_calculo = montante

                print(f"Assistente: Após {meses} meses, você terá R$ {montante:.2f}")

            except:
                print("Assistente: Use o formato: 'rende 1000 em 12 meses'")

        # Memória simples
        elif "ultimo" in user:
            if ultimo_calculo:
                print(f"Assistente: Seu último cálculo foi R$ {ultimo_calculo:.2f}")
            else:
                print("Assistente: Nenhum cálculo realizado ainda.")

        # Ajuda
        else:
            print("Assistente: Posso te ajudar com:")
            print("- Cálculos de investimento")
            print("- Explicação de CDB e poupança")
            print("Exemplo: 'rende 1000 em 12 meses'")

# executar
assistente()
