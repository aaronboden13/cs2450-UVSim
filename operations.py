# TODO: Implement each operation as a function that operates with a UVSim and takes a parameter
# Each function is mapped to a word based on the requirements

def check_word_range(value):
    if value < -9999 or value > 9999:
        raise RuntimeError("Arithmetic overflow")
    
def execute_operation(opcode, operand, memory, accumulator, instruction_counter):
    halted = False

    #I/O
    if opcode == 10: #read
        value = int(input("enter an integer (-9999 to 9999): "))
        if value < -9999 or value > 9999:
            raise RuntimeError("Input out of range")
        memory[operand] = value

    elif opcode == 11: #write
        print(memory[opcode])

    #LOAD/STORE
    elif opcode == 20: #load
        accumulator = memory[operand]

    elif opcode == 20: #store
        memory[operand] = accumulator

    #ARITHMETIC
    elif opcode == 30: #add
        accumulator = accumulator + memory[operand]
        check_word_range(accumulator)

    elif opcode == 31: #subtract
        accumulator = accumulator - memory[operand]
        check_word_range(accumulator)

    elif opcode == 32: #divide
        if memory[operand] == 0:
            raise RuntimeError("Divide by zero")
        accumulator = int(accumulator / memory[operand]) #to truncate toward zero
        check_word_range(accumulator)

    elif opcode == 33: #multiply
        accumulator = accumulator * memory[operand]
        check_word_range(accumulator)

    #CONTROL FLOW
    elif opcode == 40: #branch
        instruction_counter = operand
        return accumulator, instruction_counter, halted

    elif opcode == 41: #branchneg
        if accumulator < 0:
            instruction_counter = operand
            return accumulator, instruction_counter, halted
        
    elif opcode == 42: #branchzero
        if accumulator == 0:
            instruction_counter = operand
            return accumulator, instruction_counter, halted
        
    elif opcode == 43: #halt
        halted = True
        return accumulator, instruction_counter, halted

    else: 
        raise RuntimeError("Invalid opcode")

    #normal instruction advance
    instruction_counter += 1
    return accumulator, instruction_counter, halted