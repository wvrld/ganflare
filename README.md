`⚡ genflare`

`genflare` is a command-line tool written in python which helps remove the tedium of common capture-the-flag 'shell searching'.

We've all been there; a bit of time has passed since our enumeration and we're finally ready to run a reverse shell on our target. However, soon, you're 30 tabs deep in some random blog posts trying to find out the syntax for *that one command* you know you should've memorized by now but couldn't be bothered to. You give up, head over to pentestmonkey, or read through your old notes in an attempt to find that elusive command, and finally, after the motherboard on your target has corroded because of how long it's been, you finally find it; swearing thereafter to remember that command so you never forget it again.

> Okay, yes. That's *quite* the exaggeration, but it's really annoying! Anyways, genflare will make it so that you can just type in the language you need a shell for, and it will spit out the most common ones used in CTFs!

## ⚡ Disclaimer! 
This tool generates reverse shell commands. However, keep in mind that obfuscation does not exist yet. **OPSEC wise, this tool is the equivalent of running head first into a wall made completely out of megaphones announcing your every move. Speaking of reverse shells**...

- DO NOT use these shells, or *any* commands such as these on hosts which you do not have EXPLICIT WRITTEN permission to do so.
- The author of `genflar` will not be held responsible if you decide to use this against someone or something you don't have permission to attack. Be smart, guys.
- This tool is going to be an evergrowing project, please report any bugs, issues, etc. and I'll try my absolute best to get the issues resolved.

## ⭐ Installation
```
git clone https://github.com/wvrld/genflare && cd genflare/
python3 -m pip install -r requirements.txt
chmod +x genflare.py
```

## 🩸 Usage 
```
wvrld@snowflake:~$ python3 genflare.py -h

usage: genflare.py [-h] [-i ip] [-p port] [-s shell] [-l] [-v]

generate common shells used during CTFs!

optional arguments:
  -h, --help            show this help message and exit
  -i ip, --ip ip        LHOST
  -p port, --port port  LPORT
  -s shell, --shell shell
                        SHELL
  -l, --list-shells     outputs the currently compatible shells (more shells
                        are planned to be included in the future :D
  -v, --version         prints version
```

The script also works with `user-supplied arguments (from v1.1 onwards)`. If you'd like to skip the whole one-by-one entries for the various parameters the script uses, you can pass them into the command line as follows:
```
python3 genflare.py -i 10.0.0.1 -p 9999 -s <shell>
python3 genflare.py -i $ip -p $port -s <shell>
```

As stated before, this script is ever growing, so, more shells are surely on their way once I get the time to incorporate them in. To list the *currently compatible* shells, run the script with `-l or --list-shells`:
```
python3 genflare.py --list-shells

[+] the accepted shells are  'POWERSHELL', 'PYTHON3', 'PYTHON', 'BASH', 'PERL', 'RUBY', 'LUA', 'PHP', 'SH', 'NC'
```

## 📑 To-Do 
- <del>`create support for user-supplied arguments`</del> ✅ 
- `add more shells/languages`
- `add in some download cradles/QoL stuff?`
- `add an auto listener initializer for shells like nc, python, etc.`

```
[for the future]
```

- `obfuscated shells?` <br>
- `support for windows?`
- `what else? hmm...`
