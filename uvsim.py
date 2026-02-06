class UVSimMemory:
    def __init__(self, size=100):
        # Initialize 100-word memory with +0000
        self.memory = ["+0000"] * size
        self.accumulator = "+0000"  # Accumulator register
        self.program_counter = 0    # Program counter

    def read_memory(self, address):
        """Return the word at the given memory address."""
        if 0 <= address < len(self.memory):
            return self.memory[address]
        else:
            raise IndexError("Memory address out of range")

    def write_memory(self, address, value):
        """Write a signed 4-digit word to memory."""
        if not self._is_valid_word(value):
            raise ValueError("Value must be a signed 4-digit number")
        if 0 <= address < len(self.memory):
            self.memory[address] = value
        else:
            raise IndexError("Memory address out of range")

    def load_accumulator(self, address):
        """Load value from memory into the accumulator."""
        self.accumulator = self.read_memory(address)

    def store_accumulator(self, address):
        """Store accumulator value into memory."""
        self.write_memory(address, self.accumulator)

    def fetch_instruction(self):
        """Fetch the instruction at the current program counter."""
        instruction = self.read_memory(self.program_counter)
        self.program_counter += 1
        return instruction

    def reset(self):
        """Reset memory, accumulator, and program counter."""
        self.memory = ["+0000"] * len(self.memory)
        self.accumulator = "+0000"
        self.program_counter = 0

    @staticmethod
    def _is_valid_word(value):
        """Check if value is a signed 4-digit decimal."""
        if isinstance(value, str) and len(value) == 5 and (value[0] in "+-" and value[1:].isdigit()):
            return True
        return False

    def display_state(self):
        """Print memory, accumulator, and program counter."""
        print(f"Accumulator: {self.accumulator}")
        print(f"Program Counter: {self.program_counter}")
        print("Memory Snapshot:")
        for i in range(0, len(self.memory), 10):
            print(" ".join(f"{addr}:{self.memory[addr]}" for addr in range(i, i+10)))

