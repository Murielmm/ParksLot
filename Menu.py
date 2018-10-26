from datetime import datetime
import Park

Park = Park.park()


class menu:

    def displayMainMenu(self):
        print("---------Menu---------")
        option = input("Digite a opção desejada:\n1 - Registrar Entrada\n"
                      "2 - Registrar Saída\n3 - Listar Veículos\n0 - Sair da Aplicação\n")

        if option != '1' and option != '2' and option != '3' and option != '0':
            print("\nERRO! Opção inválida!")
            return

        return int(option)

    def displayEntryMenu(self):
        print("\n-----Registrar Entrada-----")
        vehicle_type = input("Tipo do veículo(M/A): ").upper()

        if vehicle_type != 'M' and vehicle_type != 'A':
            print("\nERRO! Tipo de veículo inválido!")
            return

        if Park.validParkCapacity(vehicle_type) is True:
            return {'Type': vehicle_type,
                    'Plate': input("Placa do veículo: ").upper(),
                    'Cpf': input("CPF do condutor: "),
                    'Name': input("Nome do condutor: "),
                    'Phone': input("Telefone do condutor: "),
                    'Time': str(datetime.now())}

    def displayExitMenu(self):
        print("\n-----Registrar Saída-----")
        return input("Digite a placa do veículo: ").upper()
