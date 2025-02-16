class CustomDialogue:
    def __init__(self, initial_text="", final_text="", error_text="option not found", input_text=">>>", is_loop=True, start_option_markers=" [", end_option_markers="]"):
        self.initial_text = initial_text
        self.final_text = final_text
        self.error_text = error_text
        self.input_text = input_text
        self.is_loop = is_loop
        self.start_option_markers = start_option_markers
        self.end_option_markers = end_option_markers
        self.options = {} 

    def add_option(self, name, function, custom_option_marker=False, start_custom_option_marker="", end_custom_option_marker=""):
        if custom_option_marker:
            self.options.setdefault(name, [function, start_custom_option_marker, end_custom_option_marker])
        else:
            self.options.setdefault(name, [function, self.start_option_markers, self.end_option_markers])
        #name: [0 - function, 1 - start_custom_option_marker, 2 - end_custom_option_marker]

    def ask_dialogue(self):
        print(self.initial_text)
        for key in self.options:
            print(f"{self.options[key][1]}{key}{self.options[key][2]}")
        print(self.final_text)

#--------------------------------------------------------------------------Input:
#Escolha uma das opções [opção1] [opção2] [opção3] [outros...]:
#>>>
        while True:
            user_input = input(self.input_text)
            if user_input in self.options:
                self.options[user_input][0]()
                return
            else:
                print(self.error_text)
            if not self.is_loop: break

class CustomListDialogue:
    def __init__(self, initial_text="", final_text="", error_text="option not found", input_text=">>>", is_loop=True, list_type=1):
        self.initial_text = initial_text
        self.final_text = final_text
        self.error_text = error_text
        self.input_text = input_text
        self.is_loop = is_loop
        self.list_type = list_type
        self.options = {}
        self.enumerated_options = []

    def add_option(self, name, function):
        self.options.setdefault(name, function)
        self.enumerated_options.append(name)
        #name: function

    def ask_dialogue(self):
        print(self.initial_text)

        for i, name in enumerate(self.enumerated_options):
            print(f"{i + 1} - {name}")

        if self.final_text != "":
            print(self.final_text)

#--------------------------------------------------------------------------Input:
#Escolha uma opção:
#1 - opção 1
#2 - opção 2
#3 - opção 3
#4 - outros...
#olá mundo
#>>>
        while True:
            user_input = input(self.input_text)
            try:
                user_input = int(user_input)
                is_int_input = True
            except ValueError:
                is_int_input = False

            if is_int_input and 0 <= user_input - 1 <= len(self.enumerated_options):
                self.options[self.enumerated_options[user_input - 1]]()
                return
            else:
                print(self.error_text)
            if not self.is_loop: break