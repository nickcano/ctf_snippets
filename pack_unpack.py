## standard ##
import struct

struct.pack("<Q", some_uqword_value)
struct.unpack("<Q", some_string)[0]

struct.pack("<q", some_qword_value)
struct.unpack("<q", some_string)[0]

struct.pack("<L", some_ulong_value)
struct.unpack("<L", some_string)[0]

struct.pack("<l", some_long_value)
struct.unpack("<l", some_string)[0]

## pwntools ##
from pwn import *

p64(some_qword_value)
u64(some_string)

p32(some_long_value)
u32(some_string)