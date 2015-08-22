#setting up build system to kill process run by sublime

I found an interesting way to solve this.

My build system on sublime-text2 call my Makefile which has 2 options and uses the ONESHELL directive:

.ONESHELL:
run: myprogram
    ./myprogram &
    echo $$! > "pid.tmp"
Note that after it starts my program its pid is saved on a file. And i have a second option:

stop:
    kill -9 `cat pid.tmp`
    rm pid.tmp
This option kills the process started by the run command.

Then i configured my build system (Tools -> Build System -> New Build System...) so i could access both options:

{
    "cmd": ["make"],
    "variants":
    [
            {
                    "name": "Run",
                    "cmd": ["make", "run"]
            },
            {
                    "name": "Stop",
                    "cmd": ["make", "stop"]
            }
    ]
}

But i want to call both options from key bindings on sublime so i edited the file "Preferences -> Key Bindings - User" to look like this:

[
{ "keys": ["ctrl+r"], "command": "build", "args": {"variant": "Run"} },
{ "keys": ["alt+r"], "command": "build", "args": {"variant": "Stop"} }
]
Now if i press ctrl+r my program starts (and enters an infinity loop) and when i press alt+r my program stops which is almost what i wanted.

The only problem left is that when i run alt+r i loose the output produced by ctrl+r.