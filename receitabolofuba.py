def receita_bolo_de_fuba():
    # Variáveis iniciais
    forno = 'desligado'
    doçura = 'Bastante'  # Opções: 'Pouca', 'Normal', 'Bastante'
    
    # Pré-aquecer o forno se estiver desligado
    if forno == 'desligado':
        print("Forno está desligado. Pré-aquecendo a 180°C...")
        forno = 'preaquecido'
    else:
        print("Forno já está aquecido.")
    
    # Ajustar a quantidade de açúcar conforme a doçura desejada
    if doçura == 'Pouca':
        xicaras_de_acucar = 2
    elif doçura == 'Normal':
        xicaras_de_acucar = 3
    elif doçura == 'Bastante':
        xicaras_de_acucar = 5
    else:
        xicaras_de_acucar = 3  # Valor padrão
    
    print("\n=== Receita de Bolo de Fubá ===\n")
    print("Ingredientes:")
    print(f" - 2 xícaras de fubá")
    print(f" - 1 xícara de farinha de trigo")
    print(f" - {xicaras_de_acucar} xícaras de açúcar")
    print(" - 3 ovos")
    print(" - 1 xícara de leite")
    print(" - 1/2 xícara de óleo")
    print(" - 1 colher (sopa) de fermento em pó")
    print(" - Erva-doce a gosto (opcional)\n")
    print("Modo de Preparo:")
    print("1. Unte uma forma com manteiga e fubá.")
    print("2. Em uma tigela, misture o fubá, a farinha de trigo e o açúcar.")
    print("3. Adicione os ovos, o leite e o óleo, misturando bem até obter uma massa homogênea.")
    print("4. Incorpore o fermento e a erva-doce, misturando delicadamente.")
    print("5. Despeje a massa na forma e leve ao forno por aproximadamente 40 minutos ou até dourar.")
    print("6. Retire do forno, espere esfriar, desenforme e sirva.")

# Chamar a função para exibir a receita
receita_bolo_de_fuba()
