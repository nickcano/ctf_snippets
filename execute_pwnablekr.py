from pwn import *

challenge_ssh_port = 2222
challenge_user = "user"
# if you want to automatically download the binary and load it as `binary` with `ELF()`, put the file name here.
# otherwise, put `None`
challenge_binary = "binary"
# if the challenge requires a local nc to an elevated instance, put the port here and `io` will be a tube to that instance.
# otherwise, put `None` and `io` will be a tube to the ssh terminal
challenge_net_port = 9032

ssh = ssh(challenge_user, "pwnable.kr", password="guest", port=challenge_ssh_port)
if (challenge_net_port is None):
	io = ssh.shell()
else:
	io = ssh.remote("localhost", challenge_net_port)

if (challenge_binary is not None):
	try:
		binary = ELF("./%s" % challenge_binary)
	except:
		ssh.download("~/%s" % challenge_binary)
		binary = ELF("./%s" % challenge_binary)

# start exploit here
io.interactive()