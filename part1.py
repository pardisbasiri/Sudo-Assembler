# Assembly Project Part One

# Program Description: A program to assemble 'and', 'or', 'add' and 'sub' instructions just for registers
# Author: Pardis Basiri 
# Student Number: 9935714 
# Creation Date: 1400/09/09
# Revisions: 0.0.0

# Right format of entering input: ins reg1, reg2

# If the input is not right or not supported by this program it may end in on of the 3 exits:
# Exit1 : to stop if the len of input is not right.
# Exit2 : to stop if instruction or registers are not valid.
# Exit3 : to stop if registers are not in the same size (the sign is when opcode = -1)

import sys

inp = (input().lower()).split(' ')         # inp = ['ins', 'reg1,',  'reg2']

# Exit1:
if len(inp) != 3:                          # if the program doesn't end when len input is wrong we will get error in line 20([:-1] part)
    print('Something wrong')                                          
    sys.exit()
    
ins = inp[0] 
reg1 = inp[1][:-1]                         # using [:-1] to cut the ',' from the end of reg1
reg2 = inp[2]

instructions = ['add', 'sub', 'and', 'or']
reg8bit = ['al', 'cl', 'dl', 'bl', 'ah', 'ch', 'dh', 'bh']
reg16bit = ['ax', 'cx', 'dx', 'bx', 'sp', 'bp', 'si', 'di']
reg32bit = ['eax', 'ecx', 'edx', 'ebx', 'esp', 'ebp', 'esi', 'edi']
all_reg = reg8bit + reg16bit + reg32bit

# Exit2:
if ins not in instructions or reg1 not in all_reg or reg2 not in all_reg:
    print('Something wrong')                                          
    sys.exit()


def find_opcode (ins):                           
    
    opcode = '-1'                            # setting a primarly amount for opcode to check if it was changed at the end
                                             # if opcode doesn't change => registers didn't have the same size
    
    if ins == 'add':
        if reg1 in reg8bit and reg2 in reg8bit:
            opcode = '00'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '01'
        
            
    elif ins == 'sub':
        if reg1 in reg8bit and reg2 in reg8bit:
            opcode = '28'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '29'
        

    elif ins == 'and':
        if reg1 in reg8bit and reg2 in reg8bit:
            opcode = '20'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '21'


    elif ins == 'or':
        if reg1 in reg8bit and reg2 in reg8bit:
            opcode = '08'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '09'
            
    return opcode
          

def find_REG (reg):
                                                                            # exp to get how it works:
    if reg == reg8bit[0] or reg == reg16bit[0] or reg == reg32bit[0]:       # for al, ax, eax => REG = '000' 
        REG = '000'                                                         
                                                                                    
    elif reg == reg8bit[1] or reg == reg16bit[1] or reg == reg32bit[1]:     
        REG = '001'
        
    elif reg == reg8bit[2] or reg == reg16bit[2] or reg == reg32bit[2]:
        REG = '010'
        
    elif reg == reg8bit[3] or reg == reg16bit[3] or reg == reg32bit[3]:
        REG = '011'
        
    elif reg == reg8bit[4] or reg == reg16bit[4] or reg == reg32bit[4]:
        REG = '100'
    
    elif reg == reg8bit[5] or reg == reg16bit[5] or reg == reg32bit[5]:
        REG = '101'
        
    elif reg == reg8bit[6] or reg == reg16bit[6] or reg == reg32bit[6]:
        REG = '110'
    
    elif reg == reg8bit[7] or reg == reg16bit[7] or reg == reg32bit[7]:
        REG = '111'
    
    return REG
      
opcode = find_opcode(ins)

# Exit3:
if opcode == '-1':
    print('""')
    sys.exit()
    
# Second Part: MOD-REG-R/M  
second_part = hex(int('11' + find_REG(reg2) + find_REG(reg1), 2))          # To put MOD and REG and R/M togheter
                                                                           #in a binary format and then convert it to hexadecimal

# Final result if nothing went wrong
print('"\\x' + opcode + '\\' + second_part + '"')
    
    
    

    



