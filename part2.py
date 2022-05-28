# Assembly Project Part Two

# Program Description: A program to assemble 'and', 'or', 'add' and 'sub' instructions just for registers and memory
# Author: Pardis Basiri
# Student Number: 9935714 
# Creation Date: 1400/10/06
# Revisions: 1.0.0

# Right format of entering input: ins reg1, reg2 (reg1 and reg2 can be memory or register but I didn't change the name after part one project)

# If the input is not right or not supported by this program it may end in on of the 3 exits:
# Exit1 : to stop if the len of input is not right.
# Exit2 : to stop if instruction or registers are not valid.
# Exit3 : to stop if registers are not in the same size or both operands are memory (sign: opcode = '-1').

instructions = ['add', 'sub', 'and', 'or']
reg8bit = ['al', 'cl', 'dl', 'bl', 'ah', 'ch', 'dh', 'bh']
reg16bit = ['ax', 'cx', 'dx', 'bx', 'sp', 'bp', 'si', 'di']
reg32bit = ['eax', 'ecx', 'edx', 'ebx', 'esp', 'ebp', 'esi', 'edi']
memory = ['[eax]', '[ecx]', '[edx]', '[ebx]', '[esp]', '[ebp]', '[esi]', '[edi]']
operands = reg8bit + reg16bit + reg32bit + memory

def find_opcode (ins):                           
                
    opcode = '-1'                            # setting a primarly amount for opcode to check if it was changed at the end
                                             # if opcode doesn't change => registers didn't have the same size
    
    if ins == 'add':
        if reg1 in reg8bit and reg2 in reg8bit or reg1 in memory and reg2 in reg8bit:
            opcode = '00'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '01'
        elif reg1 in memory and reg2 in reg16bit or reg1 in memory and reg2 in reg32bit:
            opcode = '01'
        if reg1 in reg8bit and reg2 in memory:
            opcode = '02'
        elif reg1 in reg16bit and reg2 in memory or reg1 in reg32bit and reg2 in memory:
            opcode = '03'
        
            
    elif ins == 'sub':
        if reg1 in reg8bit and reg2 in reg8bit or reg1 in memory and reg2 in reg8bit:
            opcode = '28'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '29'
        elif reg1 in memory and reg2 in reg16bit or reg1 in memory and reg2 in reg32bit:
            opcode = '29'
        if reg1 in reg8bit and reg2 in memory:
            opcode = '2A'
        elif reg1 in reg16bit and reg2 in memory or reg1 in reg32bit and reg2 in memory:
            opcode = '2B'
        

    elif ins == 'and':
        if reg1 in reg8bit and reg2 in reg8bit or reg1 in memory and reg2 in reg8bit:
            opcode = '20'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '21'
        elif reg1 in memory and reg2 in reg16bit or reg1 in memory and reg2 in reg32bit:
            opcode = '21'
        if reg1 in reg8bit and reg2 in memory:
            opcode = '22'
        elif reg1 in reg16bit and reg2 in memory or reg1 in reg32bit and reg2 in memory:
            opcode = '23'


    elif ins == 'or':
        if reg1 in reg8bit and reg2 in reg8bit or reg1 in memory and reg2 in reg8bit:
            opcode = '08'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '09'
        elif reg1 in memory and reg2 in reg16bit or reg1 in memory and reg2 in reg32bit:
            opcode = '09'
        if reg1 in reg8bit and reg2 in memory:
            opcode = '0A'
        elif reg1 in reg16bit and reg2 in memory or reg1 in reg32bit and reg2 in memory:
            opcode = '0B'
            
    return opcode

def find_REG (reg):
    if reg in memory:
        reg = reg[1:-1]
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
            
with open('assemblyCode.txt') as file:
    for line in file:
        print(line.rstrip())
        inp = line.rstrip()                 
        inp = (inp.lower()).split(' ')                 # inp = ['ins', 'reg1/mem',  'reg2/mem']
        
        while(True):        

            # Exit1:
            if len(inp) != 3:                          # if the program doesn't end when len input is wrong we will get error in line 20([:-1] part)
                print('Something wrong')
                break          
                
            ins = inp[0] 
            reg1 = inp[1][:-1]                         # using [:-1] to cut the ',' from the end of reg1
            reg2 = inp[2]

            # Exit2:
            if ins not in instructions or reg1 not in operands or reg2 not in operands:
                print('Something wrong')
                break
                  
            opcode = find_opcode(ins)

            # Exit3:
            if opcode == '-1':
                print('""')
                break
                
            # Second Part: MOD-REG-R/M
            MOD = '11'
            if reg1 in memory or reg2 in memory:
                MOD = '00'
            second_part = hex(int(MOD + find_REG(reg2) + find_REG(reg1), 2))          # To put MOD and REG and R/M togheter
                                                                                       #in a binary format and then convert it to hexadecimal

            # Final result if nothing went wrong
            print('"\\x' + opcode + '\\' + second_part + '"')
            break
    
    
    

    



