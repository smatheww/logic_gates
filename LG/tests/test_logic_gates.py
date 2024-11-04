# tests/test_logic_gates.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from logic_gates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, HalfAdder, FullAdder, EightBitAdder

class TestLogicGates(unittest.TestCase):

    def test_and_gate(self):
        gate = ANDGate("AND")
        gate.set_pins(1, 1)
        self.assertEqual(gate.get_output(), 1)
        gate.set_pins(1, 0)
        self.assertEqual(gate.get_output(), 0)

    def test_or_gate(self):
        gate = ORGate("OR")
        gate.set_pins(1, 0)
        self.assertEqual(gate.get_output(), 1)
        gate.set_pins(0, 0)
        self.assertEqual(gate.get_output(), 0)

    def test_not_gate(self):
        gate = NOTGate("NOT")
        gate.set_pin(1)
        self.assertEqual(gate.get_output(), 0)
        gate.set_pin(0)
        self.assertEqual(gate.get_output(), 1)

    def test_nand_gate(self):
        gate = NANDGate("NAND")
        gate.set_pins(1, 1)
        self.assertEqual(gate.get_output(), 0)
        gate.set_pins(1, 0)
        self.assertEqual(gate.get_output(), 1)

    def test_nor_gate(self):
        gate = NORGate("NOR")
        gate.set_pins(0, 0)
        self.assertEqual(gate.get_output(), 1)
        gate.set_pins(1, 0)
        self.assertEqual(gate.get_output(), 0)

    def test_xor_gate(self):
        gate = XORGate("XOR")
        gate.set_pins(1, 0)
        self.assertEqual(gate.get_output(), 1)
        gate.set_pins(1, 1)
        self.assertEqual(gate.get_output(), 0)

class TestAdders(unittest.TestCase):

    def test_half_adder(self):
        half_adder = HalfAdder()
        sum_bit, carry_bit = half_adder.calculate(1, 0)
        self.assertEqual((sum_bit, carry_bit), (1, 0))
        sum_bit, carry_bit = half_adder.calculate(1, 1)
        self.assertEqual((sum_bit, carry_bit), (0, 1))

    def test_full_adder(self):
        full_adder = FullAdder()
        sum_bit, carry_out = full_adder.calculate(1, 1, 0)
        self.assertEqual((sum_bit, carry_out), (0, 1))
        sum_bit, carry_out = full_adder.calculate(1, 1, 1)
        self.assertEqual((sum_bit, carry_out), (1, 1))

    def test_eight_bit_adder(self):
        adder = EightBitAdder()
        a = [0, 1, 1, 0, 0, 1, 0, 1]
        b = [1, 0, 1, 1, 0, 1, 1, 0]
        result, carry_out = adder.calculate(a, b)
        self.assertEqual(result, [1, 0, 0, 0, 1, 1, 0, 1])
        self.assertEqual(carry_out, 0)

if __name__ == "__main__":
    unittest.main()
