class dialogue:
    def __init__(self, initial_text, final_text, error_text, dialogue_type, is_loop=True, **options): # Options retorna um dicionário
#------------------------------------------------------------------------------------------------------------------------------------------Filters:

        if not options:
            raise ValueError("dialogue doesn't have any option")

#------------------------------------------------------------------------------------------------------------------------------------------

        self.initial_text = str(initial_text)
        self.final_text = str(final_text)
        self.error_text = str(error_text)
        self.dialogue_type = dialogue_type
        self.is_loop = is_loop if isinstance(is_loop, bool) else True
        self.options = {}
        
        for key, value in options.items():
            self.options[str(key)] = value
    
    def askDialogue(self):
#------------------------------------------------------------------------------------------------------------------------------------------Type 1
        if self.dialogue_type == 1:
            print(self.initial_text, end="")
            for i in self.options:
                print(f" [{i}]", end="")
            print(self.final_text)

            while True:
                user_input = input(">>>")
                if user_input in self.options:
                    self.options[user_input]()
                    return
                else:
                    print(self.error_text)
                if not self.is_loop: break
#------------------------------------------------------------------------------------------------------------------------------------------Type 2
        elif self.dialogue_type == 2:
            print(self.initial_text)
            enumerated_itens = ["_"]
            for i, key in enumerate(self.options):
                print(f"{i + 1} - {key}")
                enumerated_itens.append(self.options[key]) # lista com os itens postos na ordem em que são apresentados começando pelo 1
            print(self.final_text)

            while True:
                user_input = input(">>>")
                input_can_int = True
                try: int(user_input)
                except: input_can_int = False

                if input_can_int and int(user_input) > 0 and int(user_input) <= len(enumerated_itens) - 1: #Verifica se pode ser um int, se é maior que 0 e se tem nas opções
                    enumerated_itens[int(user_input)]()
                    return
                else:
                    print(self.error_text)
                if not self.is_loop: break
        else:
            raise ValueError(f"dialogue can't find type{self.dialogue_type}")