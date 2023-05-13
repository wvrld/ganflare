#!/usr/bin/env python3

import os
import re
import sys
import time
import argparse
import platform
import netifaces
from termcolor import cprint
from colorama import Fore, Style
from netifaces import interfaces, ifaddresses, AF_INET

ok = Fore.LIGHTGREEN_EX + '[+]' + Style.RESET_ALL
err = Fore.LIGHTRED_EX + '[!]' + Style.RESET_ALL
info = Fore.LIGHTYELLOW_EX + '[*]' + Style.RESET_ALL

if sys.version_info.major != 3:
    print('\n' + err + ''' please run this script with python3.
    usage: python3 genflare.py <args> \n''')
    sys.exit(1)

acceptedshells = ['POWERSHELL',
                  'PYTHON3',
                  'PYTHON',
                  'BASH',
                  'PERL',
                  'RUBY',
                  'LUA',
                  'PHP',
                  'SH',
                  'NC']


def clear():
    time.sleep(0.5)
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def banner():
    print(Fore.LIGHTMAGENTA_EX + '''\
    
    ┌─┐┌─┐┌┐┌┌─┐┬  ┌─┐┬─┐┌─┐  (cli shell generator) v1.1
    │ ┬├┤ │││├┤ │  ├─┤├┬┘├┤      
    └─┘└─┘┘└┘└  ┴─┘┴ ┴┴└─└─┘  by wvrld.                
''' + Style.RESET_ALL)


def init():
    clear()
    banner()


def inetfaces():
    print(info, 'getting interfaces for lhost population...')
    time.sleep(0.3)
    print(ok, netifaces.interfaces())
    ips = []
    for interface in interfaces():
        if AF_INET in ifaddresses(interface):
            for link in ifaddresses(interface)[AF_INET]:
                ips.append(link['addr'])
            print('ok', Fore.LIGHTYELLOW_EX + link['addr'], Style.RESET_ALL)


def submitlhost():
    global lhost
    print(info, 'getting lhost submission')
    print(info, 'which address would you like to create a reverse shell for?')
    while True:
        try:
            lhost = input('\n\rflare > ')
            if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', lhost):
                print('\n' + ok, 'lhost set to: {}'.format(Fore.LIGHTYELLOW_EX + lhost))
                return lhost
            else:
                print('\n' + err, 'please enter one of the addresses above.')
                print(err, 'example:' + Fore.LIGHTYELLOW_EX, 'flare >', Fore.LIGHTRED_EX + '192.168.0.1',
                      Style.RESET_ALL)
        except:
            print('\n\n' + err, 'exception caught! exiting...\n')
            sys.exit(1)


def submitlport():
    global lport
    init()
    print('\n' + ok, 'lhost set to: {}'.format(Fore.LIGHTYELLOW_EX + lhost))
    print('\n' + info, 'getting port submission')
    print(info, 'please specify a port for the connect back')
    while True:
        try:
            lport = input('\n\rflare > ')
            integer = lport.isdigit()
            if integer:
                print('\n' + ok, 'lport set to: {}'.format(Fore.LIGHTYELLOW_EX + lport))
                return lport
            else:
                print('\n' + err, 'please enter a port')
                print(err, 'example:' + Fore.LIGHTYELLOW_EX, 'flare >', Fore.LIGHTRED_EX + '9999',
                      Style.RESET_ALL)
        except:
            print('\n\n' + err, 'exception caught! exiting...\n')
            sys.exit(1)


def showcurrentconfig():
    init()
    print('\n' + ok, Fore.LIGHTYELLOW_EX + 'lhost, lport', Style.RESET_ALL + 'is set to {}'.format(Fore.LIGHTMAGENTA_EX + lhost) +
          Fore.LIGHTYELLOW_EX + ':' + '{}'.format(Fore.LIGHTMAGENTA_EX + lport) + '\n' + Style.RESET_ALL)


def gettypeofshell():
    global shelltype
    print(info, 'getting shell submission')
    print(info, 'which type of shell would you like to use?')
    print(info, 'the following shells are currently compatible', Fore.LIGHTRED_EX + '''\r
    
    POWERSHELL
    PYTHON3
    PYTHON
    BASH
    PERL
    RUBY
    LUA
    PHP
    SH
    NC''', Style.RESET_ALL)

    while True:
        try:
            shelltype = input('\n\rflare > ')
            if shelltype.upper() in acceptedshells:
                print('\n' + ok, 'shell is set to {}'.format(Fore.LIGHTYELLOW_EX + shelltype.upper()))
                return shelltype
            else:
                print('\n' + err, 'please the type of shell you\'d like to use')
                print(err, 'example:' + Fore.LIGHTYELLOW_EX, 'flare >', Fore.LIGHTRED_EX + 'powershell/bash/zsh/nc...',
                      Style.RESET_ALL)
        except:
            print('\n\n' + err, 'exception caught! exiting...\n')
            sys.exit(1)


def showshelloutput():
    init()
    location = 'src/' + shelltype.lower()
    shell = open(location, 'r')
    shells = shell.readlines()
    print(ok, 'cooking some {}'.format(Fore.LIGHTRED_EX + shelltype.upper()), Style.RESET_ALL + 'shells!')
    cprint('\n*here you go, enjoy*\n', 'green', attrs=['bold', 'blink'])
    time.sleep(1)
    for sh in shells:
        print(ok, Fore.LIGHTYELLOW_EX + re.sub('TEMPHOST', lhost, sh).replace('TEMPPORT', lport))
    print(ok, 'thank you for using' + Fore.LIGHTMAGENTA_EX, 'genflare!', Style.RESET_ALL + 'remember that in the '
                                                                                          'absence of a '
                                                                                          'fully-tty shell, '
                                                                                          'you should '
                                                                                          'stabilize or spawn a '
                                                                                          'tty :)\n')


parser = argparse.ArgumentParser(description='generate common shells used during CTFs!')
parser.add_argument('-i', '--ip', metavar='ip', dest='lhost', type=str, help='LHOST', required=False)
parser.add_argument('-p', '--port', metavar='port', dest='lport', type=int, help='LPORT', required=False)
parser.add_argument('-s', '--shell', metavar='shell', dest='shelltype', type=str, help='SHELL', required=False)
parser.add_argument('-l', '--list-shells',
                    dest='listed',
                    help='outputs the currently compatible shells (more shells '
                         'are planned to be included in the future :D',
                    action='store_true')
parser.add_argument('-v', '--version', help='prints version', action='version', version='%(prog)s v1.1')

args = parser.parse_args()

if args.listed:
    print('\n' + ok, 'the accepted shells are', Fore.LIGHTYELLOW_EX,
          '{}'.format(acceptedshells).replace('[', '').replace(']', ''), '\n')

elif args.lhost and args.lport and args.shelltype:
    shelltype = args.shelltype
    lhost = args.lhost
    lport = args.lport
    lport = str(lport)
    if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', lhost) and shelltype.upper() in acceptedshells:
        showshelloutput()
    elif not re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', lhost):
        print('\n')
        print(err, 'looks like you mistyped an ip, please check your input!\n')
        sys.exit(1)
    elif shelltype.upper() not in acceptedshells:
        print('\n')
        print(err, 'the shell you have specified either doesn\'t exist or isn\'t currently compatible. exiting...')
        print(info,
              'for a list of compatible shells, run the script with `--list-shells` -> ./genflare --list-shells\n')
        sys.exit(1)

elif args.lhost and args.lport:
    lhost = args.lhost
    lport = args.lport
    lport = str(lport)
    init()
    print('\n' + ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}:{}'.format(lhost.upper(), lport), Style.RESET_ALL)
    showcurrentconfig()
    gettypeofshell()
    showshelloutput()
    sys.exit(0)

elif args.shelltype and args.lport:
    shelltype = args.shelltype
    lport = args.lport
    lport = str(lport)
    if shelltype.upper() in acceptedshells:
        init()
        print('')
        print(ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(shelltype.upper()), Style.RESET_ALL)
        print(ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(lport), Style.RESET_ALL)
        inetfaces()
        submitlhost()
        showcurrentconfig()
        showshelloutput()
    else:
        print('')
        print(err, 'the shell you have specified either doesn\'t exist or isn\'t currently compatible. exiting...')
        print(info,
              'for a list of compatible shells, run the script with `--list-shells` -> ./genflare --list-shells\n')
        sys.exit(1)

elif args.shelltype and args.lhost:
    shelltype = args.shelltype
    lhost = args.lhost
    if shelltype.upper() in acceptedshells:
        init()
        print('')
        print(ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(shelltype.upper()), Style.RESET_ALL)
        print(ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(lhost), Style.RESET_ALL)
        submitlport()
        showcurrentconfig()
        showshelloutput()
    else:
        print('')
        print(err, 'the shell you have specified either doesn\'t exist or isn\'t currently compatible. exiting...')
        print(info,
              'for a list of compatible shells, run the script with `--list-shells` -> ./genflare --list-shells\n')
        sys.exit(1)

elif args.lhost:
    lhost = args.lhost
    init()
    print('\n', ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(lhost.upper()), Style.RESET_ALL)
    submitlport()
    showcurrentconfig()
    gettypeofshell()
    showshelloutput()

elif args.lport:
    lport = args.lport
    lport = str(lport)
    init()
    print('\n' + ok, 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(lport), Style.RESET_ALL)
    inetfaces()
    submitlhost()
    showcurrentconfig()
    gettypeofshell()
    showshelloutput()

elif args.shelltype:
    shelltype = args.shelltype
    if shelltype.upper() in acceptedshells:
        init()
        print('\n')
        print('\n' + ok + 'user supplied' + Fore.LIGHTMAGENTA_EX, '{}'.format(shelltype.upper()), Style.RESET_ALL)
        inetfaces()
        submitlhost()
        submitlport()
        showcurrentconfig()
        showshelloutput()
    else:
        print('\n')
        print(err, 'the shell you have specified either doesn\'t exist or isn\'t currently compatible. exiting...')
        print(info,
              'for a list of compatible shells, run the script with `--list-shells` -> ./genflare --list-shells\n')
        sys.exit(1)

elif __name__ == '__main__':
    clear()
    banner()
    inetfaces()
    submitlhost()
    submitlport()
    showcurrentconfig()
    gettypeofshell()
    showshelloutput()
