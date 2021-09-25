#page( text_display )    Version 1.09    9-25-21
from os import system, name        

class IntroScreen():
    def __init__(self): self.name = "IntroScreen"        
    def __str__(self): return self.name

    @staticmethod
    def title_text(): print("T h e    L a s t    T e x t    A d v e n t u r e\n")
    @staticmethod 
    def intro_text():       
        #Intro test
        with open( "player.txt", "r" ) as file: file = file.read()
        if file == "":
            name_ = input("Adventurer, tell us your name?")
            print( "\nHello,", name_+"!\n" )
            with open("player.txt", 'a') as file_:
                file_.write("Hi "+name_+",\n" "Welcome back.\n")
                file_.close()
        elif file != "":
            with open("player.txt", 'r') as file_:
                print( file_.read() )
                file_.close()
                
    @staticmethod 
    def clear():
        if name == 'Android':_ = system('cls')
        else: _ = system('clear')
