# Nome: João Victor dos Santos Silva Pinto
# Curso: Superior de Tecnologia em Análise e Desenvolvimento de Sistemas

# Importação de bibliotecas utilizadas
from time import sleep
from typing import Literal

# Classe principal do sistema puc
class SchoolSystem:
    # Definição de tipos de dados do menu principal
    MenuOptionsType = Literal["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"]

    # Definição de opções do menu principal
    _MAIN_MENU_OPTIONS: dict[str, str] = {
        "Estudantes": "1",
        "Professores": "2",
        "Disciplinas": "3",
        "Turmas": "4",
        "Matrículas": "5",
        "Sair": "0"
    }

    # Definição de opções do menu de entidades
    _ENTITY_MENU_OPTIONS: dict[str, str] = {
        "Incluir": "1",
        "Listar": "2",
        "Atualizar": "3",
        "Excluir": "4",
        "Voltar ao menu principal": "0"
    }

    # Nome do submenu atual que segue o padrão do tipo de dado MenuOptionsType
    _sub_menu_name: MenuOptionsType  = "ESTUDANTES"

    # Dicionário de listas de entidades para as operações
    _entities_lists: dict[MenuOptionsType, list[str]] = {
        "ESTUDANTES": []
    }

    # Metodo construtor da classe que inicia já no menu principal
    def __init__(self):
        self._main_menu()

    # Metodo do menu principal
    def _main_menu(self) -> None:
        while True:
            print("***** SISTEMA PUC ******")

            # Exibição das opções do menu principal baseada no dicionário _MAIN_MENU_OPTIONS e leitura da opção
            for option, value in self._MAIN_MENU_OPTIONS.items():
                print(f"({value}) {option}")

            menu_option: str = input("DIGITE UMA OPÇÃO: ")

            # Redirecionamento para o submenu da entidade estudantes
            if menu_option == "1":
                self._sub_menu_name = "ESTUDANTES"
                self._entity_menu()
                break

            # Opção de sair do sistema
            if menu_option == "0":
                print("***** SISTEMA ENCERRADO *****")
                break

            # Retorna ao menu principal caso a opção escolhida não esteja disponível
            if menu_option in ["2", "3", "4", "5"]:
                print("EM DESENVOLVIMENTO")
                print("RETORNANDO AO MENU PRINCIPAL...")
                sleep(1)
                continue

            # Retorna ao menu principal caso a opção escolhida não seja válida
            print("OPÇÃO INVÁLIDA")
            print("RETORNANDO AO MENU PRINCIPAL...")
            sleep(1)

    # Metodo do submenu de entidades
    def _entity_menu(self) -> None:
        while True:
            print(f"***** [{self._sub_menu_name}] MENU DE OPERAÇÕES *****".upper())

            # Exibição das opções do submenu baseada no dicionário _ENTITY_MENU_OPTIONS e leitura da opção
            for option, value in self._ENTITY_MENU_OPTIONS.items():
                print(f"({value}) {option}")

            menu_option: str = input("DIGITE UMA OPÇÃO: ")

            # Redirecionamento para o menu principal
            if menu_option == "0":
                self._main_menu()
                break

            # Retorna ao menu de entidades caso a opção escolhida não esteja disponível
            if menu_option in ["3", "4"]:
                print("EM DESENVOLVIMENTO")
                print(f"RETORNANDO AO MENU {self._sub_menu_name}...")
                sleep(1)
                continue

            # Redirecionamento para a inclusão de entidades
            if menu_option == "1":
                self._add_entity()
                continue

            # Redirecionamento para a listagem de entidades
            if menu_option == "2":
                self._list_entities()
                continue

            # Retorna ao menu de entidades caso a opção escolhida não seja válida
            print("OPÇÃO INVÁLIDA")
            print(f"RETORNANDO AO MENU {self._sub_menu_name}...")
            sleep(1)

    # Metodo de inclusão de entidades
    def _add_entity(self) -> None:
        print("===== INCLUSÃO =====")

        # Leitura do nome da entidade e inclusão na lista de entidades
        entity_name: str = input("NOME: ")
        self._entities_lists[self._sub_menu_name].append(entity_name)

        # Mensagem de sucesso e retorno ao menu de entidades
        print(f"{entity_name} FOI INCLUÍDO COM SUCESSO".upper())
        input("Pressione ENTER para continuar.")
        print(f"RETORNANDO AO MENU {self._sub_menu_name}...")
        sleep(1)

    # Metodo de listagem de entidades
    def _list_entities(self) -> None:
        # Verificação se há entidades cadastradas caso contrário exibe mensagem e retorna ao menu de entidades
        if not self._entities_lists[self._sub_menu_name]:
            print(f"NÃO HÁ {self._sub_menu_name} CADASTRADOS".capitalize())
            input("Pressione ENTER para continuar.")
            print(f"RETORNANDO AO MENU {self._sub_menu_name}...")
            sleep(1)
            return

        # Exibição das entidades cadastradas
        print("===== LISTAGEM =====")
        for entity in self._entities_lists[self._sub_menu_name]:
            print(f"- {entity}")

        # Mensagem de retorno ao menu de entidades
        input("Pressione ENTER para continuar.")
        print(f"RETORNANDO AO MENU {self._sub_menu_name}...")
        sleep(1)

# Instanciação da classe principal do sistema
SchoolSystem()
