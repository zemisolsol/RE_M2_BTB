#!/usr/bin/env python3

import random
import numpy
import itertools
from pym2e.asm import *
from pym2e.experiment import *
from pym2e.setup import *
from pym2e.event import *
from pym2e.util import *

from m1n1.asm import ARMAsm

def BTB_SIZE_INDIRECT(num_branches, align): 
    test_code = r"""
.macro OneJump index
    .p2align {align}
    adr x0, next_\index
    br x0
next_\index:
.endm

BtbLoop:
.irp label, {sequence}
    OneJump index=\label
.endr
end:
    nop
""".format(sequence=",".join([str(x) for x in range(0, num_branches)]), align=align)
    return test_code

def BTB_CAPACITY():
    ####### BTB Capacity Test #######
    N = [3]
    B = [20480, 1024, 20480, 2048, 20480, 3072, 20480, 4096, 20480, 5120, 20480, 6144, 20480, 7168, 20480, 8192]
    
    res_n = [] 
    for n in N:
        res_b = []
        for b in B:
            BTB_TEST = MyExperiment(AssemblerTemplate(BTB_SIZE_INDIRECT(b, n)))
            code = BTB_TEST.compile(0xc6, addr=0x09_0000_0000)
            tgt.write_payload(code.start, code.data)
            for i in range(1):
                tgt.smp_call_sync(code.start, 0)
            res = tgt.smp_call_sync(code.start, 0)
            res_b.append(round((res/b)*100, 2))
        res_n.append(res_b)
        print('N = '+str(n))
   
    transposed = list(zip(*res_n))
    for i, row in enumerate(transposed):
        branches = B[i] 
        values = ' '.join(f'{val:.2f}' for val in row)
        print(f'{branches} {values}')
    
    with open('result.txt', 'w') as f:
        for i, row in enumerate(transposed):
            branches = B[i] 
            values = ' '.join(f'{val:.2f}' for val in row)
            print(f'{branches} {values}', file=f)

tgt = TargetMachine()

BTB_CAPACITY()
