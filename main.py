from pystyle import *
import random
from time import sleep
import os

banner1 = """                                                                                
                        .                               (.                      
                                                                                
                         %%%%%%%%%%%%%%%%%%%%%%              *.                 
                   .   %%%%%%%%%%%%%%%%%%%%%%%%%%            (.                 
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%         (,                 
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%       (.                 
                       %%%%%%%%%                   &&%%%%    (,                 
                       %%%%%%%  &&&&  &&&&&  (&&&&&&&&&%%%   (.                 
                       %%%%%%%%%&&&@  &&&&(  &&&&&&&&&&&&&   (,                 
                       %%%%%%%%%%%&   &&&&   &&&&&&&&&&&&&,, #.                 
                       %%%%%%%%%%%   .&&&&   &&&&&&&&&&&&&,,,(.                 
                       %%%%%%%%%%    &&&&&   &&&  *&&&&&&&,,,%.                 
                       %%%%%%%%%    &&&&&&&      &&&&&&&&&,,,%.                 
                   ,   (%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&.,,*%.                 
                    .    %%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&,,,,*(.                 
                    ...                ,,,,,,,,,,,,,,,,,,,*(/,                  
                       *#,,,,,,,,,,,,,,,,,///////*//*//*((/.                    """
Anime.Fade(Center.Center(banner1), Colors.yellow_to_red,
           Colorate.Diagonal, enter=True)
active = True
while active:
    title1 = """                               
  ####  #    #  ####  # #    # 
 #    # #    # #    # #  #  #  
 #      ###### #    # #   ##   
 #      #    # #    # #   ##   
 #    # #    # #    # #  #  #  
  ####  #    #  ####  # #    # 
                               
                               """
    print(Colorate.Horizontal(Colors.red_to_yellow, title1))
    choix = input("1 - choix du nombre\n2 - automatique Random\n")
    choix = int(choix)
    os.system('cls' if os.name == 'nt' else 'clear')
    if choix == 1:
        print("""                                                                      
        //   ) )                                                          
   /    /___/ /  ___      ___     ( )  _   __      ___    __  ___ / __    
  /     ____ / //   ) ) ((   ) ) / / // ) )  ) ) //   ) )  / /   //   ) ) 
 //           //   / /   \ \    / / // / /  / / //   / /  / /   //   / /  
//           ((___/ / //   ) ) / / // / /  / / ((___( (  / /   //   / /   """)
            
        running = True
        n = input("\n\n\n\nnumber plz ==>\n")
        t = float(n)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(n)
        sleep(1)
        while running:

            r = t % 2
            if r == 1:
                sleep(0.0001)
                x = t * 3 + 1
                a = int(x)
                print(x)
                if x == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print("----------------------------------------------------------------------------------------------")
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif r == 0:
                sleep(0.0001)
                x = t / 2
                a = int(x)
                print(x)
                if x == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print("----------------------------------------------------------------------------------------------")
                    os.system('cls' if os.name == 'nt' else 'clear')
            r = x % 2
            if r == 1:
                sleep(0.0001)
                a = x * 3 + 1
                b = int(a)
                print(a)
                if a == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print("----------------------------------------------------------------------------------------------")
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif r == 0:
                sleep(0.0001)
                a = x / 2
                b = int(a)
                print(a)
                if a == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print("----------------------------------------------------------------------------------------------")
                    os.system('cls' if os.name == 'nt' else 'clear')
            r = b % 2
            if r == 1:
                sleep(0.0001)
                t = b * 3 + 1
                x = int(t)
                print(t)
                if t == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print("----------------------------------------------------------------------------------------------")
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif r == 0:
                sleep(0.0001)
                t = b / 2
                x = int(t)
                print(t)
                if t == 1:
                    print("ce nombre n'est pas le bon")
                    running = False
                    sleep(2.5)
                    print("----------------------------------------------------------------------------------------------")
                    os.system('cls' if os.name == 'nt' else 'clear')
    elif choix == 2:
        print("""                    __________            .__                __  .__     
____________    ____\______   \____  _____|__| _____ _____ _/  |_|  |__  
\_  __ \__  \  /    \|     ___/  _ \/  ___/  |/     \\__  \\   __\  |  \ 
 |  | \// __ \|   |  \    |  (  <_> )___ \|  |  Y Y  \/ __ \|  | |   Y  \
 |__|  (____  /___|  /____|   \____/____  >__|__|_|  (____  /__| |___|  /
            \/     \/                   \/         \/     \/          \/ """)
        running = True
        n = random.randint(1, 1000000000000000000)
        t = float(n)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(n)
        sleep(1)
        while running:

            r = t % 2
            if r == 1:
                sleep(0.0001)
                x = t * 3 + 1
                a = int(x)
                print(x)
                if x == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print(Colorate.Vertical(Colors.yellow_to_red,"----------------------------------------------------------------------------------------------"))
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif r == 0:
                sleep(0.0001)
                x = t / 2
                a = int(x)
                print(x)
                if x == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print(Colorate.Vertical(Colors.yellow_to_red,"----------------------------------------------------------------------------------------------"))
                    os.system('cls' if os.name == 'nt' else 'clear')
            r = x % 2
            if r == 1:
                sleep(0.0001)
                a = x * 3 + 1
                b = int(a)
                print(a)
                if a == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print(Colorate.Vertical(Colors.yellow_to_red,"----------------------------------------------------------------------------------------------"))
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif r == 0:
                sleep(0.0001)
                a = x / 2
                b = int(a)
                print(a)
                if a == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print(Colorate.Vertical(Colors.yellow_to_red,"----------------------------------------------------------------------------------------------"))
                    os.system('cls' if os.name == 'nt' else 'clear')
            r = b % 2
            if r == 1:
                sleep(0.0001)
                t = b * 3 + 1
                x = int(t)
                print(t)
                if t == 1:
                    print("ce nombre n'est pas le bon ")
                    running = False
                    sleep(1)
                    print(Colorate.Vertical(Colors.yellow_to_red,"----------------------------------------------------------------------------------------------"))
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif r == 0:
                sleep(0.0001)
                t = b / 2
                x = int(t)
                print(t)
                if t == 1:
                    print(Colorate.Vertical(Colors.yellow_to_red,"ce nombre n'est pas le bon"))
                    running = False
                    sleep(2.5)
                    print(Colorate.Vertical(Colors.yellow_to_red,"----------------------------------------------------------------------------------------------"))
                    os.system('cls' if os.name == 'nt' else 'clear')