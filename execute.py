from pwn import *

local_info = ['binary_name', 'lib/x86_64-linux-gnu/libc-2.23.so']
remote_info = ['network_addr', 0000, 'libc.so.6']

libc_path = ''
if (args.REMOTE):
	libc_path = remote_info[2]
	io = remote(remote_info[0], remote_info[1])
else:
	libc_path = local_info[1]
	io = process(local_info[0], raw=False)

if (len(libc_path) > 0):
	libc = ELF(libc_path)
binary = ELF(local_info[0])

## examples ##
io.recv()
io.send("hello")
io.sendline("hello")
io.interactive()