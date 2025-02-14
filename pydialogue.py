class basic_dialogue:
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

class custom_dialogue(self, initial_text="", final_text="", error_text="option not found", input_text=">>>", is_loop=True, start_option_markers=" [", end_option_markers="]"):
    def __init__(self):
        self.initial_text = initial_text
        self.final_text = final_text
        self.error_text = error_text
        self.input_text = input_text
        self.is_loop = is_loop
        self.start_option_markers = start_option_markers
        self.end_option_markers = end_option_markers
        self.options = {} 

    def addOption(self, name, function, start_custom_option_marker=self.start_option_markers, end_custom_option_marker=self.end_option_markers):
        self.options.setdefault(name, [function, start_custom_option_marker, end_custom_option_marker])
        #Key: [0 - function, 1 - start_custom_option_marker, 2 - end_custom_option_marker]

    def askDialogue(self):
        print(self.initial_text)
        for key in self.options:
            print(f"{self.options[key][1]}{key}{self.options[key][2]}")
        print(self.final_text)

        while self.is_loop == True:
            user_input = input(self.input_text)
            if user_input in self.options:
                self.options[user_input][0]()
                return
            else:
                print(self.error_text)

class custom_list_dialogue(self, initial_text="", final_text="", error_text="option not found", input_text=">>>", is_loop=True, list_type=1):
    def __init__(self):
        self.initial_text = initial_text
        self.final_text = final_text
        self.error_text = error_text
        self.input_text = input_text
        self.is_loop = is_loop
        self.list_type = list_type
        self.options = {} 

    def addOption(self, name, function):
        self.options.setdefault(name, function)

    def askDialogue(self):
        print(self.initial_text)
        print(*(f"{i + 1} - {key}" for i, key in enumerate(self.options)), sep="\n")
        print(self.final_text)

        while self.is_loop == True:
            user_input = input(self.input_text)
            if user_input in self.options:
                self.options[user_input]()
                return
            else:
                print(self.error_text)