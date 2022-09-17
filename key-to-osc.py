from ast import Str
import curses, time
from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 53000

osc_prefix = '/qlab/chain'

win = curses.initscr()
curses.noecho()
win.addstr(0, 0, 'press key to send OSC command, 0 - exit')

def input_char():
    try:
        while True: 
            ch = win.getch()
            if ch in range(32, 127): 
                break
            time.sleep(0.05)
    finally:
        curses.endwin()

    return chr(ch)


client = SimpleUDPClient(ip, port)  # Create client


def my_sender(): 
    char = input_char()

    if char.lower() in ['0']:
        print('finish')
    else: 
        win.addstr(2, 0, f'pressed key: {char}')
        win.addstr(3, 0, f'OSC message: {ip}:{port}{osc_prefix}-{char}')
        client.send_message(f'{osc_prefix}-{char}', 1)
        my_sender()


my_sender()