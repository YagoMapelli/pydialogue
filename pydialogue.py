class Dialogue:
    def __init__(self, initial_text="", final_text="", error_text="option not found", input_text=">>>", is_loop=True, start_option_markers=" [", end_option_markers="]"):
        self.initial_text = initial_text
        self.final_text = final_text
        self.error_text = error_text
        self.input_text = input_text
        self.is_loop = is_loop
        self.start_option_markers = start_option_markers
        self.end_option_markers = end_option_markers
        self.options = {}

    def add_option(self, name, function, start_option_marker=None, end_option_marker=None):
            self.options[name] = [
                function,
                self.start_option_markers if start_option_marker is None else start_option_marker,
                self.end_option_markers if end_option_marker is None else end_option_marker
                ]
        #name: [0 - function, 1 - start_option_marker, 2 - end_option_marker]

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

class ListDialogue:
    def __init__(self, initial_text="", final_text="", error_text="option not found", input_text=">>>", is_loop=True):
        self.initial_text = initial_text
        self.final_text = final_text
        self.error_text = error_text
        self.input_text = input_text
        self.is_loop = is_loop
        self.options = {}

    def add_option(self, name, function):
        self.options[len(self.options) + 1] = [name, function]
        #number: [name, function]

    def ask_dialogue(self):
        print(self.initial_text)

        for i in range(1, self.options):
            print(f"{i + 1} - {self.options[i + 1][0]}")

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

            try: user_input = int(user_input)
            except ValueError: pass

            if isinstance(user_input, int) and user_input in self.options:
                self.options[user_input][1]()
                return
            else:
                print(self.error_text)
            if not self.is_loop: break