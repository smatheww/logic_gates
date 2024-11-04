import unittest
from logic_gates import (
    LogicGate, BinaryGate, UnaryGate,
    ANDGate, ORGate, XORGate, NOTGate,
    NANDGate, NORGate, Connector
)

class TestLogicGates(unittest.TestCase):
    def setUp(self):
        """Initialize gates for each test"""
        self.and_gate = ANDGate("AND1")
        self.or_gate = ORGate("OR1")
        self.xor_gate = XORGate("XOR1")
        self.not_gate = NOTGate("NOT1")
        self.nand_gate = NANDGate("NAND1")
        self.nor_gate = NORGate("NOR1")

    def test_and_gate(self):
        """Test AND gate truth table"""
        test_cases = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1)
        ]
        for a, b, expected in test_cases:
            self.and_gate.set_pins(a, b)
            self.assertEqual(self.and_gate.get_output(), expected)

    def test_or_gate(self):
        """Test OR gate truth table"""
        test_cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        ]
        for a, b, expected in test_cases:
            self.or_gate.set_pins(a, b)
            self.assertEqual(self.or_gate.get_output(), expected)

    def test_xor_gate(self):
        """Test XOR gate truth table"""
        test_cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)
        ]
        for a, b, expected in test_cases:
            self.xor_gate.set_pins(a, b)
            self.assertEqual(self.xor_gate.get_output(), expected)

    def test_not_gate(self):
        """Test NOT gate truth table"""
        test_cases = [
            (0, 1),
            (1, 0)
        ]
        for a, expected in test_cases:
            self.not_gate.set_pin(a)
            self.assertEqual(self.not_gate.get_output(), expected)

    def test_nand_gate(self):
        """Test NAND gate truth table"""
        test_cases = [
            (0, 0, 1),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)
        ]
        for a, b, expected in test_cases:
            self.nand_gate.set_pins(a, b)
            self.assertEqual(self.nand_gate.get_output(), expected)

    def test_nor_gate(self):
        """Test NOR gate truth table"""
        test_cases = [
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 0)
        ]
        for a, b, expected in test_cases:
            self.nor_gate.set_pins(a, b)
            self.assertEqual(self.nor_gate.get_output(), expected)

    def test_connector(self):
        """Test connector between gates"""
        self.and_gate.set_pins(1, 1)  # Should output 1
        self.or_gate.set_pins(0, 0)   # Should output 0
        connector = Connector(self.and_gate, self.not_gate)
        self.assertEqual(self.not_gate.get_output(), 0)

    def test_pin_validation(self):
        """Test pin validation"""
        with self.assertRaises(AssertionError):
            self.and_gate.get_output()  # Should raise error when pins not set

if __name__ == '__main__':
    unittest.main()