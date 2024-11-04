"""# LOGIC GATE PROBLEM
Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?

The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit.

Now extend that circuit and implement an 8-bit full adder."""

# logic_gates.py

class LogicGate:
    def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    def set_pins(self, value_a, value_b):
        self.pin_a = value_a
        self.pin_b = value_b

    def get_pin_a(self):
        return self.pin_a
    
    def get_pin_b(self):
        return self.pin_b


class ANDGate(BinaryGate):
    def perform_gate_logic(self):
        return int(self.pin_a and self.pin_b)


class ORGate(BinaryGate):
    def perform_gate_logic(self):
        return int(self.pin_a or self.pin_b)


class XORGate(BinaryGate):
    def perform_gate_logic(self):
        return int((self.pin_a or self.pin_b) and not (self.pin_a and self.pin_b))


class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None

    def set_pin(self, value):
        self.pin = value

    def get_pin(self):
        return self.pin


class NOTGate(UnaryGate):
    def perform_gate_logic(self):
        return int(not self.pin)


class NANDGate(ANDGate):
    def perform_gate_logic(self):
        return int(not super().perform_gate_logic())


class NORGate(ORGate):
    def perform_gate_logic(self):
        return int(not super().perform_gate_logic())


class HalfAdder:
    def __init__(self):
        self.xor_gate = XORGate("XOR")
        self.and_gate = ANDGate("AND")

    def calculate(self, a, b):
        self.xor_gate.set_pins(a, b)
        self.and_gate.set_pins(a, b)
        sum_bit = self.xor_gate.get_output()
        carry_bit = self.and_gate.get_output()
        return sum_bit, carry_bit


class FullAdder:
    def __init__(self):
        self.half_adder1 = HalfAdder()
        self.half_adder2 = HalfAdder()
        self.or_gate = ORGate("OR")

    def calculate(self, a, b, carry_in):
        sum1, carry1 = self.half_adder1.calculate(a, b)
        sum2, carry2 = self.half_adder2.calculate(sum1, carry_in)
        self.or_gate.set_pins(carry1, carry2)
        carry_out = self.or_gate.get_output()
        return sum2, carry_out


class EightBitAdder:
    def __init__(self):
        self.adders = [FullAdder() for _ in range(8)]

    def calculate(self, a, b):
        carry = 0
        result = []
        # Perform addition bit by bit from least significant to most significant
        for i in range(7, -1, -1):  # Start from the least significant bit
            sum_bit, carry = self.adders[7 - i].calculate(a[i], b[i], carry)
            result.insert(0, sum_bit)  # Insert at the beginning to maintain order
        return result, carry  # Return result in the correct order along with final carry

