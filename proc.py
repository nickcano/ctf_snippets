from pwn import *

## basic examples ##
python_pid = proc.pid_by_name('python')

parent_pid = proc.parent(python_pid)
siblings = proc.children(parent_pid)

ancestors = proc.ancestors(python_pid)

cmdline = proc.cmdline(python_pid)
binary_path = proc.exe(python_pid)

## sleep until pid has a debugger attached ##
proc.wait_for_debugger(pid)

## get a list of a process memory maps ##
def proc_mem_maps(pid):
	command = "/proc/%d/maps" % pid
	mapio = process(["cat", command], raw=False)
	mapio.wait_for_close()
	res = mapio.recv()
	ret = []
	for line in res.splitlines():
		addresses = line.split()[0]
		if ("-" in line):
			sbase, send = addresses.split("-")
			ret.append([int(sbase, 16), int(send, 16)])
	return ret