# Python --version: 3.6.0
# Author: Gr^k-T - Nguyen Thanh Trung

import time
import os
import webbrowser
import sys
import subprocess
import base64
import hashlib

full_ascii_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
		print('| | -ce[k]: Ceasar #decode does not require [k]                            |')
		print('| | Type "/hash + [option] + something" to hash something with your option.|')
		print('| | [option] #hash                                                         |')
		print('| | -sha1  : SHA-1                                                         |')
		print('| | -sha224: SHA-224                                                       |')
		print('| | -sha256: SHA-256                                                       |')
		print('| | -sha384: SHA-384                                                       |')
		print('| | -sha512: SHA-512                                                       |')
		print('| | -shake128[length]: SHAKE-128                                           |')
		print('| | -shake256[length]: SHAKE-256                                           |')
		print('| | Type "/bm" to back the main menu.                                      |')
		print('| | Type "/help" for more information about Decode/Encode                  |')
		print('| +========================================================================+')
		print('|')	

	def decode(data, option):
		if data == '':
			return '| Require data argument. None is given'
		elif option.lower() == '-b64':
			decoded = base64.b64decode(data.encode('ascii'))
			return '| ' + decoded.decode('ascii')
		elif option.lower() == '-ce':
			data = data.upper().split()
			data = ''.join(x for x in data)
			decoded = []
			for i in range(1, len(full_ascii_char) + 1):
				decoded.append([])
				for j in range(len(data)):
					try:
						decoded[i-1].append(full_ascii_char[full_ascii_char.index(data[j]) - i])
					except ValueError:
						return 'ValueError. Char must be in alphabet. %c given' %data[j]
			for i in range(len(decoded)):
				k = i + 1
				if k < 10: k = int('0' + str(k))
				print('| With k = %d your decode data is %s' %(i + 1, ''.join(str(x) for x in decoded[i])))										
			return '|'
		else:
			return '| Invalid option.\n| Type /help for more information'

	def encode(data, option):
		if data == '':
			return '| Require data argument. None is given'
		elif option.lower() == '-b64':
			encoded = base64.b64encode(data.encode('ascii'))
			return '| ' + str(encoded.decode('ascii'))
		else:
			return '| Invalid option.\n| Type /help for more information'

	def hash(data, option):
		if data == '':
			return '| Require data argument. None is given'
		elif option.lower() == '-sha1':
			hashed = hashlib.sha1(data.encode('ascii')).hexdigest()
			return '| ' + hashed
		elif option.lower() == '-sha224':
			hashed = hashlib.sha224(data.encode('ascii')).hexdigest()
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
		elif option.lower().startswith('-shake128'):
			if option.count('[') > 1 or option.count(']') > 1:
				return '| Invalid length'
			elif '[' in option.lower() and ']' in option.lower():
				length = option[option.index('[')+1:option.index(']')]
				check_length = is_number(length)
				check_float = is_float(length)
				if check_float:
					check_length = 'float'
				if length.count('-') == 1 and (check_length == 'float' or check_length):
					check_length = 'sub'
				if check_length == 'float':
					return '| length must be int, not float'
				elif check_length == 'sub':
					return '| length must be greater or equal 0'
				elif check_length:
					hashed = hashlib.shake_128(data.encode('ascii')).hexdigest(int(length))
					return '| ' + hashed
				else:
					return '| length must be int, not string'
			else:
				return "| Required argument 'length'"
		elif option.lower().startswith('-shake256'):
			if option.count('[') > 1 or option.count(']') > 1:
				return '| Invalid length'
			elif '[' in option.lower() and ']' in option.lower():
				length = option[option.index('[')+1:option.index(']')]
				check_length = is_number(length)
				check_float = is_float(length)
				if check_float:
					check_length = 'float'
				if length.count('-') == 1 and (check_length == 'float' or check_length):
					check_length = 'sub'
				if check_length == 'float':
					return '| length must be int, not float'
				elif check_length == 'sub':
					return '| length must be greater or equal 0'
				elif check_length:
					hashed = hashlib.shake_256(data.encode('ascii')).hexdigest(int(length))
					return '| ' + hashed
				else:
					return '| length must be int, not string'
			else:
				return "| Required argument 'length'"
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
						decoded = my_deencode.encode(' '.join(cmd_lst[2:]), cmd_lst[1])
						print(decoded)
					else:
						print('| Invalid option. None given')
						print('| Type /help for more information')
				elif cmd_lst[0].lower() == '/de':
					if cmd_lst[1][0] == '-':
						decoded = my_deencode.decode(' '.join(cmd_lst[2:]), cmd_lst[1])
						print(decoded)
					else:
						print('| Invalid option. None given')
						print('| Type /help for more information')
				elif cmd_lst[0].lower() == '/hash':
					if cmd_lst[1][0] == '-':
						decoded = my_deencode.hash(' '.join(cmd_lst[2:]), cmd_lst[1])
						print(decoded)
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

#helping functions

def is_number(n):
	try:
		int(n)
		return True
	except:
		return False

def is_float(n):
	if n.count('.') != 1:
		return False
	else:
		try:
			int(n[:n.index('.')])
			int(n[n.index('.')+1:])
			return True
		except:
			return False

def introduction():
	print("""
				
				            Nguyen Thanh Trung — Gr^k-T

				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTT+:::::::::::::::::::::::::::::::+TTTTTTTT
				TTTTTTTTT:                               :TTTTTTTT
				TTTTTTTTT:                               :TTTTTTTT
				TTTTTTTTT:      ........................./TTTTTTTT
				TTTTTTTTT:      :25/06/2016-ateotsmerthdTTTTTTTTTT
				TTTTTTTTT:      :NguyenThanhTrung?$=???+TTTTTTTTTT
				TTTTTTTTT:      :Trung/.               :TTTTTTTTTT
				TTTTTTTTT:      :ThanhTrung/.          :TTTTTTTTTT
				TTTTTTTTT:      :ThanhTrung\^^^/       :TTTTTTTTTT
				TTTTTTTTT:      :ThanhTrung^^.         :TTTTTTTTTT
				TTTTTTTTT:      :Trung^^.              :TTTTTTTTTT
				TTTTTTTTT:      :.-               -/^^TTTTTTTTTTTT
				TTTTTTTTT:                   -/^^TTTTTTTTTTTTTTTTT
				TTTTTTTTT:              -+^^TTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTT:         :+^^TTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTT:    :+^^TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTT+25/06TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
				TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
""")
	input()
	print('\n'*10)

def main_menu():
	print("""
                                    +============================+
                                    |                            |
                                    |        MAIN MENU           |
                                    |                            |
                                    | 1. Use Browser             |
                                    |                            |
                                    | 2. Decode/Encode - Hash    |
                                    |                            |
                                    |                            |
                                    |      © Copyright Gr^k-T    |
                                    |                            |
                                    +============================+
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
	print('| Type /help for more information.\n|')
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
		elif (cmd.lower()).startswith('cd'):
			print('| Cannot change directory')
		elif cmd.lower() == '/help' or cmd.lower() == 'help':
			print("""|
| Infomation help
|
| Choose the item by type its number.
|""")
		else:
			subprocess.call(cmd, shell=True)

def main():
	introduction()
	menu()

if __name__ == '__main__':
	main()