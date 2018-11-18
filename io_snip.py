from pwn import *
import sys

show_interop = args.INTEROP

def send_line(line):
	if (show_interop):
		print(line)
	io.sendline(line)

def read():
	data = io.recv()
	if (show_interop):
		sys.stdout.write(data)
	return data

def read_lines_until(prompt):
	res = ""
	while (prompt not in res):
		res += read()
	return res