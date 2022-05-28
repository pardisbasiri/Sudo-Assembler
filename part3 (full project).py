# Assembly Project Part Three

# Program Description: A program to assemble 'and', 'or', 'add' and 'sub' instructions for registers and memory and 'jmp' instruction.
# Author: Pardis Basiri
# Student Number: 9935714 
# Creation Date: 1400/10/14
# Revisions: 2.0.0

import sys
                                                                                                                                                           
instructions = ['add', 'sub', 'and', 'or']
reg8bit = ['al', 'cl', 'dl', 'bl', 'ah', 'ch', 'dh', 'bh']
reg16bit = ['ax', 'cx', 'dx', 'bx', 'sp', 'bp', 'si', 'di']
reg32bit = ['eax', 'ecx', 'edx', 'ebx', 'esp', 'ebp', 'esi', 'edi']
memory = ['[eax]', '[ecx]', '[edx]', '[ebx]', '[esp]', '[ebp]', '[esi]', '[edi]']
operands = reg8bit + reg16bit + reg32bit + memory

def find_opcode (ins, reg1, reg2):                           
                
    opcode = '-1'                            # setting a primarly amount for opcode to check if it was changed at the end
                                             # if opcode doesn't change => registers didn't have the same size
    
    if ins == 'add':
        if reg1 in reg8bit and reg2 in reg8bit or reg1 in memory and reg2 in reg8bit:
            opcode = '00'
        elif reg1 in reg16bit and reg2 in reg16bit or reg1 in reg32bit and reg2 in reg32bit:
            opcode = '01'
        elif reg1 in memory and reg2 in reg16bit or reg1 in memory and reg2 in reg32bit:
            opcode = '01'
        elif reg1 in reg8bit and reg2 in memory:
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
        elif reg1 in reg8bit and reg2 in memory:
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
        elif reg1 in reg8bit and reg2 in memory:
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
        elif reg1 in reg8bit and reg2 in memory:
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

def ins_result (inp, result):
    inp = inp.split(' ')                                  # inp = ['ins', 'reg1/mem',  'reg2/mem']
    
    if len(inp) != 3:                                     # To stop if the len of input is not right. 20([:-1] part)
        is_wrong = True          
        
    ins = inp[0] 
    reg1 = inp[1][:-1]                                    # using [:-1] to cut the ',' from the end of reg1
    reg2 = inp[2]

    if ins not in instructions or reg1 not in operands or reg2 not in operands:
        is_wrong = True                                   # To stop if instruction or registers are not valid.
        
    if reg1  in memory and reg2 in memory:                # To stop when two operands are memory
        is_wrong = True
        
    opcode = find_opcode(ins, reg1, reg2)

    if opcode == '-1' and is_wrong == False:              # To stop if registers are not in the same size.
        if result == '':
            print('""')
        else:
            print('"'+ result + '"')
        sys.exit()
        
    # Second Part: MOD-REG-R/M
    MOD = '11'
    if reg1 in memory or reg2 in memory:
        MOD = '00'
    second_part = hex(int(MOD + find_REG(reg2) + find_REG(reg1), 2))           # To put MOD and REG and R/M togheter
                                                                               #in a binary format and then convert it to hexadecimal
    
    result += '\\x' + opcode + '\\' + second_part + ''
    
    return result
    

def jmp_result (inp, file_list, counter, result):
    
    index_jmp = file_list.index(inp)
       
    label = inp[4:] + ':'
    
    if label in file_list:
        index_label = file_list.index(label)
        opcode = 'EB'
    else:                                                # When label jmp doesn't exist in file
        is_wrong = True
    
        del file_list[index_jmp]
        return file_list, counter
        
    count_label = 0                                      # To count the number of labels between jmp and it's label 
    if index_label < index_jmp:                          # When label is before jmp
        
        for i in file_list[index_label+1:index_jmp]:
            if i[-1] == ':':
                count_label +=1
                
        second_part = ((index_label - index_jmp + count_label)*2)
        
        
        #Getting 2's complement of the sencond_part:
        
        binary_number = int("{0:08b}".format(second_part))
        flipped_binary_number = ~ binary_number
        flipped_binary_number = flipped_binary_number + 1
        str_twos_complement = str(flipped_binary_number)
        second_part = hex(int(str_twos_complement, 2))
        
    if index_label > index_jmp:                          # When label is after jmp
        
        for i in file_list[index_jmp+1:index_label]:
            if i[-1] == ':':
                count_label +=1
            
        second_part = hex((index_label - index_jmp - count_label)*2)
    
    result += '\\x' + opcode + '\\' + second_part + ''

    del file_list[index_jmp]                            # To delet jmp from list
    counter = file_list.index(label) + 1                # To set right index for jumping into label instructions
    return file_list, counter, result
    
            
with open('assemblyCode.txt') as file:
    
    # Initial values:
    is_wrong = False
    file_list = []
    result = ''
    counter = 0                                         # Counter for the loop (an index number in file_list)
    
    for line in file:
        inp = (line.rstrip()).lower()
        file_list += [inp]
    
    max_index = len(file_list) - 2
    
    while(counter <= max_index and is_wrong == False):
        
        inp = file_list[counter]
        
        if inp[-1] == ':':             # To pass the label
            counter += 1
        
        elif inp[0:3] == 'jmp':
            max_index = max_index - 1
            file_list, counter, result = jmp_result(inp, file_list, counter, result)
        
        else:
            result = ins_result(inp, result)
            counter+=1
    
    if is_wrong == False:
        print('"'+ result + '"')
    else:
        print('Something wrong')
        
            
    
            
        
    
    
    

    



