#utf-8 -*-

import os
w = '\x1b[1;37m'
b = '\x1b[1;36m'
g = '\x1b[1;32m'
y = '\x1b[1;33m'
r = '\x1b[1;31m'

def banner():
	os.system('clear')
	print(f'''{g}╋╋┏┳━━━┳━┓┏━┳━━━┳━━━┓
{g}╋╋┃┃┏━┓┃┃┗┛┃┃┏━━┫┏━┓┃
{y}╋╋┃┃┃╋┃┃┏┓┏┓┃┗━━┫┗━━┓
{y}┏┓┃┃┗━┛┃┃┃┃┃┃┏━━┻━━┓┃
{g}┃┗┛┃┏━┓┃┃┃┃┃┃┗━━┫┗━┛┃
{g}┗━━┻┛╋┗┻┛┗┛┗┻━━━┻━━━┛{r} v0.2
{b}╔═════════════════════════════════════════╗
{b}║{y}*{g} Author{w}  :{g} JAMES404            {b}                    
{b}║{y}*{r} WhatsApp{w}:{r} +96598064347            {b}        
{b}║{y}*{b} Github{w}  :{b} \x1b[4mgithub.com/James404-cyber\x1b[0m{b}    
{b}╚═════════════════════════════════════════╝ ''')
