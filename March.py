# March.py
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
		print()
		print(' 		+================================================================+')
		print(' 		|                                                                |')
		print(' 		|                       /help BROWSER                            |')
		print(' 		|                                                                |')
		print(' 		| Type "/gs + something" to search something with Google.        |')
		print(' 		| Type "/ys + something" to search something with YouTube.       |')
		print(' 		|                                                                |')
		print(' 		| Type "/bm" to back the main menu.                              |')
		print(' 		| Type "/help" for more information about BROWSER.               |')
		print(' 		|                                                                |')
		print(' 		+================================================================+')
		print()

	def webbrowser_process():
		while True:
			cmd = read_command('root@Browser:~#')
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
					print('\n')
					menu()
				else:
					print('\'{}\': command not found'.format(cmd[1:]))
					print('Type "/help" for more information')
			else:
				print('\'{}\': command not found'.format(cmd))
				print('Type "/help" for more information')	

class my_deencode:

	def deencode_help():
		print()
		print(' 		+========================================================================+')
		print(' 		|                                                                        |')
		print(' 		|                       /help Decode/Encode                              |')
		print(' 		|                                                                        |')
		print(' 		| Type "/de + [option] + data" to decode data with your option.          |')
		print(' 		| Type "/en + [option] + data" to encode data with your option.          |')
		print(' 		|                                                                        |')
		print(' 		| [option]                                                               |')
		print(' 		| -b64: base64                                                           |')
		print(' 		| -ce[k]: Ceasar #decode does not require [k]                            |')
		print(' 		|                                                                        |')
		print(' 		|                                                                        |')
		print(' 		| Type "/hash + [option] + data" to hash your data with your option.     |')
		print(' 		|                                                                        |')
		print(' 		| [option] #hash                                                         |')
		print(' 		| -md5   : MD5                                                           |')
		print(' 		| -sha1  : SHA-1                                                         |')
		print(' 		| -sha224: SHA-224                                                       |')
		print(' 		| -sha256: SHA-256                                                       |')
		print(' 		| -sha384: SHA-384                                                       |')
		print(' 		| -sha512: SHA-512                                                       |')
		print(' 		| -shake128[length]: SHAKE-128                                           |')
		print(' 		| -shake256[length]: SHAKE-256                                           |')
		print(' 		|                                                                        |')
		print(' 		| Type "/bm" to back the main menu.                                      |')
		print(' 		| Type "/help" for more information about Decode/Encode                  |')
		print(' 		|                                                                        |')
		print(' 		+========================================================================+')
		print()	

	def decode(data, option):
		if data == '':
			return 'Require data argument. None is given'
		elif option.lower() == '-b64':
			try:
				decoded = base64.b64decode(data.encode('ascii'))
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + decoded.decode('ascii')
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
						return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data[j])
			for i in range(len(decoded)):
				k = i + 1
				if k < 10: k = '0' + str(k)
				print(' With k = {} your decode data is {}'.format(k, ''.join(x for x in decoded[i])))										
			return '\n'
		else:
			return 'Invalid option.\n Type /help for more information'

	def encode(data, option):
		if data == '':
			return 'Require data argument. None is given'
		elif option.lower() == '-b64':
			try:
				encoded = base64.b64encode(data.encode('ascii'))
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + str(encoded.decode('ascii'))
		elif option.lower().startswith('-ce'):
			if not option.lower().startswith('-ce['):
				return 'Invalid option.\nType /help for more information' 
			elif option.count('[') > 1 or option.count(']') > 1:
				return "Invalid 'k'"
			elif '[' in option.lower() and ']' in option.lower():
				k = option[option.index('[')+1:option.index(']')]
				check_k = is_number(k)
				check_float = is_float(k)
				if check_float:
					check_k = 'float'
				if k.count('-') == 1 and (check_k == 'float' or check_k):
					check_k = 'sub'
				if check_k == 'float':
					return 'k must be int, not float'
				elif check_k == 'sub':
					return 'k must be greater or equal 0'
				elif check_k:
					k = int(k)
					data = data.upper().split()
					data = ''.join(x for x in data)
					encoded = []
					for i in range(len(data)):
						try:
							index_append = full_ascii_char.index(data[i])+k
							if index_append > 25: index_append %= 26
							encoded.append(full_ascii_char[index_append])
						except ValueError:
							return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data[i])
					return ' '.join(x for x in encoded)
				else:
					return 'k must be int, not string'
			else:
				return "Required argument 'k'"
		else:
			return 'Invalid option.\nType /help for more information'

	def hash(data, option):
		if data == '':
			return 'Require data argument. None is given'
		elif option.lower() == '-md5':
			try:
				hashed = hashlib.md5(data.encode('ascii')).hexdigest()
				return hashed
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
		elif option.lower() == '-sha1':
			try:
				hashed = hashlib.sha1(data.encode('ascii')).hexdigest()
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + hashed
		elif option.lower() == '-sha224':
			try:
				hashed = hashlib.sha224(data.encode('ascii')).hexdigest()
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + hashed
		elif option.lower() == '-sha256':
			try:
				hashed = hashlib.sha256(data.encode('ascii')).hexdigest()
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + hashed
		elif option.lower() == '-sha384':
			try:
				hashed = hashlib.sha384(data.encode('ascii')).hexdigest()
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + hashed
		elif option.lower() == '-sha512':
			try:
				hashed = hashlib.sha512(data.encode('ascii')).hexdigest()
			except ValueError:
				return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
			return ' ' + hashed
		elif option.lower().startswith('-shake128'):
			if not option.lower().startswith('-shake128['):
				return 'Invalid option.\nType /help for more information'
			elif option.count('[') > 1 or option.count(']') > 1:
				return 'Invalid length'
			elif '[' in option.lower() and ']' in option.lower():
				length = option[option.index('[')+1:option.index(']')]
				check_length = is_number(length)
				check_float = is_float(length)
				if check_float:
					check_length = 'float'
				if length.count('-') == 1 and (check_length == 'float' or check_length):
					check_length = 'sub'
				if check_length == 'float':
					return 'length must be int, not float'
				elif check_length == 'sub':
					return 'length must be greater or equal 0'
				elif check_length:
					try:
						hashed = hashlib.shake_128(data.encode('ascii')).hexdigest(int(length))
					except ValueError:
						return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
					return ' ' + hashed
				else:
					return 'length must be int, not string'
			else:
				return "Required argument 'length'"
		elif option.lower().startswith('-shake256['):
			if not option.lower().startswith('-shake256['):
				return 'Invalid option.\nType /help for more information'
			elif option.count('[') > 1 or option.count(']') > 1:
				return 'Invalid length'
			elif '[' in option.lower() and ']' in option.lower():
				length = option[option.index('[')+1:option.index(']')]
				check_length = is_number(length)
				check_float = is_float(length)
				if check_float:
					check_length = 'float'
				if length.count('-') == 1 and (check_length == 'float' or check_length):
					check_length = 'sub'
				if check_length == 'float':
					return 'length must be int, not float'
				elif check_length == 'sub':
					return 'length must be greater or equal 0'
				elif check_length:
					try:
						hashed = hashlib.shake_256(data.encode('ascii')).hexdigest(int(length))
					except ValueError:
						return 'ValueError. Your data contains invalid alphabet. \'{}\' given'.format(data)
					return ' ' + hashed
				else:
					return 'length must be int, not string'
			else:
				return "Required argument 'length'"
		else:
			return 'Invalid option.\nType /help for more information'

	def deencode_process():
		while True:
			cmd = read_command('root@De/Encode:~#')
			if cmd[0] == '/':
				cmd_lst = cmd.split()
				if cmd_lst[0].lower() == '/help':
					my_deencode.deencode_help()
				elif cmd_lst[0].lower() == '/en':
					if cmd_lst[1][0] == '-':
						decoded = my_deencode.encode(' '.join(cmd_lst[2:]), cmd_lst[1])
						print(decoded)
					else:
						print('Invalid option. None given')
						print('Type /help for more information')
				elif cmd_lst[0].lower() == '/de':
					if cmd_lst[1][0] == '-':
						decoded = my_deencode.decode(' '.join(cmd_lst[2:]), cmd_lst[1])
						print(decoded)
					else:
						print('Invalid option. None given')
						print('Type /help for more information')
				elif cmd_lst[0].lower() == '/hash':
					if cmd_lst[1][0] == '-':
						decoded = my_deencode.hash(' '.join(cmd_lst[2:]), cmd_lst[1])
						print(decoded)
					else:
						print('Invalid option. None given')
						print('Type /help for more information')
				elif cmd_lst[0].lower() == '/bm':
					print('\n')
					menu()
				else:
					print('\'{}\': command not found'.format(cmd[1:]))
					print('Type "/help" for more information')
			else:
				print('\'{}\': command not found'.format(cmd))
				print('Type "/help" for more information')

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

#extra functions
def __main__help__():
	print("""
Infomation help

Choose the item by type its number.
""")

def introduction():
	subprocess.call('title = March', shell=True)
	print("""
				

bbbbbbbb                                                                                                                                                       
b::::::b            lllllll                                       kkkkkkkk                                                                                     
b::::::b            l:::::l                                       k::::::k                                                                                     
b::::::b            l:::::l                                       k::::::k                                                                                     
b:::::b            l:::::l                                       k::::::k                                                                                     
b:::::bbbbbbbbb     l::::l   aaaaaaaaaaaaa       cccccccccccccccc k:::::k    kkkkkkkrrrrr   rrrrrrrrr      ooooooooooo       ssssssssss       eeeeeeeeeeee    
b::::::::::::::bb   l::::l   a::::::::::::a    cc:::::::::::::::c k:::::k   k:::::k r::::rrr:::::::::r   oo:::::::::::oo   ss::::::::::s    ee::::::::::::ee  
b::::::::::::::::b  l::::l   aaaaaaaaa:::::a  c:::::::::::::::::c k:::::k  k:::::k  r:::::::::::::::::r o:::::::::::::::oss:::::::::::::s  e::::::eeeee:::::ee
b:::::bbbbb:::::::b l::::l            a::::a c:::::::cccccc:::::c k:::::k k:::::k   rr::::::rrrrr::::::ro:::::ooooo:::::os::::::ssss:::::se::::::e     e:::::e
b:::::b    b::::::b l::::l     aaaaaaa:::::a c::::::c     ccccccc k::::::k:::::k     r:::::r     r:::::ro::::o     o::::o s:::::s  ssssss e:::::::eeeee::::::e
b:::::b     b:::::b l::::l   aa::::::::::::a c:::::c              k:::::::::::k      r:::::r     rrrrrrro::::o     o::::o   s::::::s      e:::::::::::::::::e 
b:::::b     b:::::b l::::l  a::::aaaa::::::a c:::::c              k:::::::::::k      r:::::r            o::::o     o::::o      s::::::s   e::::::eeeeeeeeeee  
b:::::b     b:::::b l::::l a::::a    a:::::a c::::::c     ccccccc k::::::k:::::k     r:::::r            o::::o     o::::ossssss   s:::::s e:::::::e           
b:::::bbbbbb::::::bl::::::la::::a    a:::::a c:::::::cccccc:::::ck::::::k k:::::k    r:::::r            o:::::ooooo:::::os:::::ssss::::::se::::::::e          
b::::::::::::::::b l::::::la:::::aaaa::::::a  c:::::::::::::::::ck::::::k  k:::::k   r:::::r            o:::::::::::::::os::::::::::::::s  e::::::::eeeeeeee  
b:::::::::::::::b  l::::::l a::::::::::aa:::a  cc:::::::::::::::ck::::::k   k:::::k  r:::::r             oo:::::::::::oo  s:::::::::::ss    ee:::::::::::::e  
bbbbbbbbbbbbbbbb   llllllll  aaaaaaaaaa  aaaa    cccccccccccccccckkkkkkkk    kkkkkkk rrrrrrr               ooooooooooo     sssssssssss        eeeeeeeeeeeeee
""")
	input()
	print('\n'*10)

def main_menu():
	print("""
                                    +=============================+
                                    |                             |
                                    |          MAIN MENU          |
                                    |                             |
                                    | 1. Use Browser              |
                                    |                             |
                                    | 2. Decode/Encode - Hash     |
                                    |                             |
                                    |                             |
                                    |      © Copyright Gr^k-T     |
                                    |                             |
                                    +=============================+
""")

def read_command(com_input):
	cmd = ''
	while len(cmd) == 0:
		cmd = input(com_input+' ')
		cmd = cmd.strip()
	return cmd

def menu():
	main_menu()
	print('Type /help for more information.\n')
	while True:
		cmd = read_command('root@Gr^k-T:~#')
		if cmd == '1':
			my_webbrowser.webbrowser_help()
			my_webbrowser.webbrowser_process()
		elif cmd == '2':
			my_deencode.deencode_help()
			my_deencode.deencode_process()
		elif cmd.lower() == 'exit':
			exit()
		elif (cmd.lower()).startswith('cd'):
			print(' Cannot change directory')
		elif cmd.lower() == '/help' or cmd.lower() == 'help':
			__main__help__()
		else:
			subprocess.call(cmd, shell=True)

def main():
	introduction()
	menu()

if __name__ == '__main__':
	main()