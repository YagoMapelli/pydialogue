# pydialogue
 
Serve para facilitar o diálogo entre o código e o usuário em programas que não tem interface gráfica

para testar, na versão 1.0 é posivel adicionar este trecho código no final do codigo principal:

def opção1_function():
    print("opção 1 foi selecionada")

def opção2():
    print("opção 2 foi selecionada")

main = dialogue("o que você escolhe?", "", "esta opção n é valida", 1, True, opção1 = opção1_function , opção2 = opção2)
main.askDialogue()

second_dialogue("o que você escolhe?", "agr é com a formatação tipo 2", "esta opção n é valida", 2, True, opção1 = opção1_function , opção2 = opção2)



def opção1_function():
    print("opção 1 foi selecionada")

def opção2():
    print("opção 2 foi selecionada")

dialogue = custom_list_dialogue(initial_text="Escolha uma opção:", error_text="essa opção n eziste", input_text="-->", is_loop=True, list_type=1)
dialogue.addOption("opção1", opção1_function)
dialogue.addOption("opção2", opção2)
dialogue.askDialogue()