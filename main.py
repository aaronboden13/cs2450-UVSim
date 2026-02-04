# TODO: Create the main loop which takes the input file name and runs the contained
# BasicML code then outputs to the console any write statements
'''
Main execution driver for the UVSim
Handles program loading and fetch-decode-execute loop. 
1. Prompt user for BasicML input file.
2. Load BasicML program into UVSim memory starting at address 00.
3. Execute the program in loop from execute_program():
- Fetch the instruction at the current instruction counter.
- Decode the instruction into opcode and operand.
- Dispatch execution to the operation.
- Increment program counter
- Continue until HALT (opcode 43)
'''

from uvsim import UVSim #memory, accumulator, program counter?
from io import load_program #reads program file imput
from operations import OPERATIONS #holds the operations mapping

def execute_program(uvsim: UVSim) -> None:

    memory_size = 100

    while True:
        ic = uvsim.instruction_counter
        if not (0 <= ic < memory_size):
            raise RuntimeError(f"Program counter out of bounds: {ic}")

        instruction = uvsim.memory[uvsim.instruction_counter] #access current memory through program counter
        uvsim.instruction_counter += 1 #move to next instruction by incrementing PC
        
        if not isinstance(instruction, int):
            raise ValueError(f"Non-integer instruction: {instruction}")
        
        opcode = instruction // 100 
        operand = instruction % 100 
        
        if opcode not in OPERATIONS:
            raise RuntimeError(f"Invalid opcode {opcode}")

        if opcode == 43: #HALT I SAID HALT
            break
        
        try:
            OPERATIONS[opcode](uvsim, operand) 
        #assuming this is how operations is setup. Call coresponding opcode from operations table and pass the operand address to uvsim.
        except Exception as e:
            raise RuntimeError(
                f"Error executing instruction at address {ic}: "
                f"instruction={instruction}, opcode={opcode}, operand={operand}"
            )
        
    return

def main() -> None:
    filename = input("Enter BasicML program file: ") #ask user for file

    uvsim = UVSim() #create uvsim instance

    try:
        load_program(filename, uvsim) #read BasicML file and place instructions into UVSim memory.

        execute_program(uvsim) #start running program that's loaded in UVSim machine.

    except Exception as e:
        raise RuntimeError(f"Runtime error: {e}")
    
    return

if __name__ == "__main__":
    main()