# Python --version: 3.6.0
# Author: Gr^k-T - Nguyen Thanh Trung

import time
import os
import webbrowser
import sys
import subprocess
import base64
import hashlib

class my_webbrowser:

	def webbrowser_help():
		print('|')
		print('| +================================================================+')
		print('| |                       /help BROWSER                            |')
		print('| | Type "/gs + something" to search something with Google.        |')
		print('| | Type "/ys + something" to search something with YouTube.       |')
		print('| | Type "/bm" to back the main menu.                              |')
		print('| | Type "/help" for more information about BROWSER.               |')
		print('| +================================================================+')
		print('|')

	def webbrowser_process():
		while True:
			cmd = read_command('root@Browser:~#')
			cmd = cmd.strip()
			if cmd[0] == '/':
				cmd_lst = cmd.split()
				if cmd_lst[0] == '/help':
					my_webbrowser.webbrowser_help()
				elif cmd_lst[0].lower() == '/gs':
					gg_search = ' '.join(cmd_lst[1:])
					gg_search = gg_search.split()
					gg_search = '+'.join(gg_search)
					url = 'https://www.google.com.vn/#q='+gg_search
					webbrowser.open_new(url)
				elif cmd_lst[0].lower() == '/ys':
					yt_search = ' '.join(cmd_lst[1:])
					yt_search = yt_search.split()
					yt_search = '+'.join(yt_search)
					url = 'https://www.youtube.com/results?search_query='+yt_search
					webbrowser.open_new(url)	
				elif cmd_lst[0].lower() == '/bm':
					print('|                                                                                                 |')
					print("+-------------------------------------------------------------------------------------------------+")
					menu()
				else:
					print('| \'{}\': command not found'.format(cmd[1:]))
					print('| Type "/help" for more information')
			else:
				print('| \'{}\': command not found'.format(cmd))
				print('| Type "/help" for more information')	

class my_deencode:

	def deencode_help():
		print('|')
		print('| +========================================================================+')
		print('| |                       /help Decode/Encode                              |')
		print('| | Type "/de + [option] + something" to decode with your option.          |')
		print('| | Type "/en + [option] + something" to encode with your option.          |')
		print('| | [option]                                                               |')
		print('| | -b64: base64                                                           |')
		print('| | Type "/hash + [option] + something" to hash something with your option.|')
		print('| | [option] #hash                                                         |')
		print('| | -sha1  : SHA-1                                                         |')
		print('| | -sha256: SHA-256                                                       |')
		print('| | -sha384: SHA-384                                                       |')
		print('| | -sha512: SHA-512                                                       |')
		print('| | Type "/bm" to back the main menu.                                      |')
		print('| | Type "/help" for more information about Decode/Encode                  |')
		print('| +========================================================================+')
		print('|')	

	def decode(data, option):
		if option.lower() == '-b64':
			decoded = base64.b64decode(data.encode('ascii'))
			return '| ' + decoded.decode('ascii')
		else:
			return '| Invalid option.\n| Type /help for more information'

	def encode(data, option):
		if option.lower() == '-b64':
			encoded = base64.b64encode(data.encode('ascii'))
			return '| ' + str(encoded.decode('ascii'))
		else:
			return '| Invalid option.\n| Type /help for more information'

	def hash(data, option):
		if option.lower() == '-sha1':
			hashed = hashlib.sha1(data.encode('ascii')).hexdigest()
			return '| ' + hashed
		elif option.lower() == '-sha256':
			hashed = hashlib.sha256(data.encode('ascii')).hexdigest()
			return '| ' + hashed
		elif option.lower() == '-sha384':
			hashed = hashlib.sha384(data.encode('ascii')).hexdigest()
			return '| ' + hashed
		elif option.lower() == '-sha512':
			hashed = hashlib.sha512(data.encode('ascii')).hexdigest()
			return '| ' + hashed
		else:
			return '| Invalid option.\n| Type /help for more information'

	def deencode_process():
		while True:
			cmd = read_command('root@De/Encode:~#')
			cmd = cmd.strip()
			if cmd[0] == '/':
				cmd_lst = cmd.split()
				if cmd_lst[0].lower() == '/help':
					my_deencode.deencode_help()
				elif cmd_lst[0].lower() == '/en':
					if cmd_lst[1][0] == '-':
						print(my_deencode.encode(' '.join(cmd_lst[2:]), cmd_lst[1]))
					else:
						print('| Invalid option. None given')
						print('| Type /help for more information')
				elif cmd_lst[0].lower() == '/de':
					if cmd_lst[1][0] == '-':
						print(my_deencode.decode(' '.join(cmd_lst[2:]), cmd_lst[1]))
					else:
						print('| Invalid option. None given')
						print('| Type /help for more information')
				elif cmd_lst[0].lower() == '/hash':
					if cmd_lst[1][0] == '-':
						print(my_deencode.hash(' '.join(cmd_lst[2:]), cmd_lst[1]))
					else:
						print('| Invalid option. None given')
						print('| Type /help for more information')
				elif cmd_lst[0].lower() == '/bm':
					print('|                                                                                                 |')
					print("+-------------------------------------------------------------------------------------------------+")
					menu()
				else:
					print('| \'{}\': command not found'.format(cmd[1:]))
					print('| Type "/help" for more information')
			else:
				print('| \'{}\': command not found'.format(cmd))
				print('| Type "/help" for more information')

def introduction():
	print("""
				
				            Nguyen Thanh Trung — Gr^k-T

				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNN+:::::::::::::::::::::::::::::::+NNNNNNNN
				NNNNNNNNN:                               :NNNNNNNN
				NNNNNNNNN:                               :NNNNNNNN
				NNNNNNNNN:      ........................./NNNNNNNN
				NNNNNNNNN:      yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNN:      yNmhhhhhhhhhhhhhhhhhhhhmNNNNNNNNNN
				NNNNNNNNN:      yNNNhs/.               sNNNNNNNNNN
				NNNNNNNNN:      yNNNNNNNmho/.          sNNNNNNNNNN
				NNNNNNNNN:      yNNNNNNNNNNNNmy/       sNNNNNNNNNN
				NNNNNNNNN:      yNNNNNNNNmho/.         sNNNNNNNNNN
				NNNNNNNNN:      yNNNdyo:.              sNNNNNNNNNN
				NNNNNNNNN:      ++-`              -/shmNNNNNNNNNNN
				NNNNNNNNN:                  `-/shNNNNNNNNNNNNNNNNN
				NNNNNNNNN:             `-+sdNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNN:        `:+ydNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNN:   `:+ydNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNooymNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
				NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
""")
	time.sleep(3)
	print('\n'*10)

def main_menu():
	print("""
                                    +=========================+
                                    |                         |
                                    |        MAIN MENU        |
                                    |                         |
                                    | 1. Use Browser          |
                                    |                         |
                                    | 2. Decode/Encode        |
                                    |                         |
                                    |                         |
                                    |      © Copyright Gr^k-T |
                                    |                         |
                                    +=========================+
""")
	print("+-------------------------------------------------------------------------------------------------+")
	print("| >_                                       root@Gr^k-T: ~                                         |")
	print("+-------------------------------------------------------------------------------------------------+")

def read_command(com_input):
	cmd = ''
	while len(cmd) == 0:
		cmd = input('| '+com_input+' ')
	return cmd

def menu():
	main_menu()
	while True:
		cmd = read_command('root@Gr^k-T:~#')
		cmd = cmd.strip()
		if cmd == '1':
			my_webbrowser.webbrowser_help()
			my_webbrowser.webbrowser_process()
		elif cmd == '2':
			my_deencode.deencode_help()
			my_deencode.deencode_process()
		elif cmd.lower() == 'exit':
			exit()
		elif cmd.lower() == '/help':
			print("""|
| Infomation help
|""")
		else:
			subprocess.call(cmd, shell=True)

def main():
	introduction()
	menu()

if __name__ == '__main__':
	main()