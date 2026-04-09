vc1 = input("Qual é o valor da primeira carta?")
nc1 = input("Qual o naipe da primeira carta? Use C para copas, O para ouros, E para espadas e P para paus ")
vc2 = input("Qual o valor da segunda carta?")
nc2 = input("Qual o naipe da segunda carta? Use C para copas, O para ouros, E para espadas e P para paus ")
vc3 = input("Qual o valor da terceira carta? ")
nc3 = input("Qual o naipe da terceira carta? Use C para copas, O para ouros, E para espadas e P para paus ")
trinca = False
if (nc1.upper() != nc2.upper() and nc1.upper() != nc3.upper() and nc2.upper() != nc3.upper()) and (vc1 == vc2 and vc1 == vc3):
    trinca = True
    print("Você fez uma trinca!")
else: print("Não fez uma trinca!")
