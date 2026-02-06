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

from uvsim import UVSimMemory #memory, accumulator, program counter?
from operations import OPERATIONS #holds the operations mapping

def execute_program(uvsim: UVSimMemory) -> None:

    memory_size = len(uvsim.memory)

    while True:
        if not (0 <= uvsim.program_counter < memory_size):
            raise RuntimeError(f"Program counter out of bounds: {uvsim.program_counter}")

        instruction = uvsim.fetch_instruction()
        ic = uvsim.program_counter - 1 # grabs current program counter subtracts one as it has already been incremented in uvsim
        
        if not isinstance(instruction, str):
            raise ValueError(f"Non-string instruction at address {ic}: {instruction!r}")
        
        try:
            instruction_int = int(instruction)
        except ValueError:
            raise RuntimeError(f"Invalid instruction format at address {ic}: {instruction!r}")
        
        opcode = abs(instruction_int) // 100 
        operand = abs(instruction_int) % 100 
        
        if opcode not in OPERATIONS:
            raise RuntimeError(f"Invalid opcode {opcode}")
        
        try:
            OPERATIONS[opcode](uvsim, operand) 
        #assuming this is how operations is setup. Call coresponding opcode from operations table and pass the operand address to uvsim.
        except Exception as e:
            raise RuntimeError(
                f"Error executing instruction at address {ic}: "
                f"instruction={instruction}, opcode={opcode}, operand={operand}"
            ) from e
        
        if opcode == 43: #HALT I SAID HALT
            break
        
    return

def main() -> None:
    filename = input("Enter BasicML program file: ") #ask user for file

    uvsim = UVSimMemory() #create uvsim instance

    check = uvsim.load_program(filename)
    if not check:
        return
    
    execute_program(uvsim)

    return

if __name__ == "__main__":
    main()