# ttr source file
import keyboard
import os
import colorama

colorama.init()

def main(filename):
    try:
        with open(filename, "r") as f:
            os.system("cls" if os.name == "nt" else "clear")
            for line in f:
                args = line.split()
                term_width = os.get_terminal_size().columns
                usingMid = False
                usingEnd = False
                color = "WHITE"
                whitespace_prefix = ""
                strT = 0
                
                i = 0
                while i < len(args):
                    if i < len(args):
                        current_arg = args[i]
                        
                        if current_arg == "[Color": # color
                            if i + 1 < len(args):
                                color_arg = args[i+1]
                                color = color_arg.replace("]", "")
                                strT += len("[Color " + color + "] ")
                                i += 1
                        
                        elif current_arg == "[Mid]": # mid text
                            usingMid = True
                            usingEnd = False
                            strT += len("[Mid] ")
                        
                        elif current_arg == "[w/": # w/ eval
                            if i + 1 < len(args):
                                evalArg = args[i+1].replace("]", "")
                                CevalArg = evalArg.replace("End", str(term_width)).replace("Start", "0")
                                whitespace_amount = eval(CevalArg)
                                whitespace_prefix = " " * whitespace_amount
                                strT += len("[w/ " + evalArg + "] ")
                                i += 1
                                
                        elif current_arg.startswith("[Whitespace"): # add whitespace line
                            if i + 1 < len(args):
                                amount_str = args[i+1]
                                amount = int(amount_str.replace("l]", ""))
                                whitespace_prefix = " " * amount
                                strT += len("[Whitespace " + amount_str + "] ")
                                i += 1

                        elif current_arg == "[End]": # start from end of line
                            usingMid = False
                            usingEnd = True
                            strT += len("[End] ")
                    
                    i += 1
                
                color = getattr(colorama.Fore, color)
                content_text = line.strip()[strT:]
                
                if usingMid:
                    text = color + content_text.center(term_width - len(content_text))
                    print(text)
                elif usingEnd:
                    text = color + " " * (term_width - len(content_text)) + content_text
                    print(text)
                else:
                    print(color + whitespace_prefix + content_text)
                
    except FileNotFoundError:
        print("File not found to render.") # error when file is not found

def GUI():
    os.system("cls" if os.name == "nt" else "clear")
    print("TTR | Text To Render Shell")
    print("Press [O] to open file. Press [C] to exit.")
    while True:
        key = keyboard.read_event().name
        if key == "o": # open file
            file = input(f"{colorama.Fore.BLACK}{colorama.Back.LIGHTBLACK_EX} File name> {colorama.Style.RESET_ALL}{colorama.Fore.GREEN}")
            main(file)
        elif key == "c": # exit
            return
        # TO DO // more options such as edit and etc

GUI()