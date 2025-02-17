# pydialogue
 
Serve para facilitar o diálogo entre o código e o usuário em programas que não tem interface gráfica

para testar, na versão 2.3.4 é posivel adicionar este trecho código no final do codigo principal:

def opção1_function():
    print("opção 1 foi selecionada")

def opção2():
    print("opção 2 foi selecionada")

main = Dialogue(initial_text="escolha uma opção", final_text=":", input_text=">>>", is_loop=False, start_option_markers="(", end_option_markers=")")
main.add_option("opção 1", opção1_function, "[", end_option_marker="]")
main.add_option("opção 2", opção2)
main.ask_dialogue()

lista = ListDialogue("escolha uma das opções:", error_text="essa opção n existe", input_text=">>>>", is_loop=True)
lista.add_option("opção 1", opção1_function)
lista.add_option("opção 2", opção2)
lista.ask_dialogue()

from time import sleep
sleep(4)