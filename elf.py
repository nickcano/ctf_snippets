from pwn import *

## protections ##
nx = binary.nx
relro = binary.relro

## sections ##
sections = binary.num_sections()
segments = binary.num_segments()
fucked_segments = binary.rwx_segments
write_segments = binary.writable_segments
nowrite_segments = binary.non_writable_segments

## symbols and addresses ##
fread_offset = libc.symbols['fread']

entry = binary.entry
fread_got = binary.got['fread']
fread_plt = binary.plt['write']
function_dict = binary.functions