"""Make a superclass and subclasses that inherit the feature of the parent
class that simulates the AND, OR & NOT gates."""


class LogicGate:
    """Parent class describes the label and output of the logic gate."""

    def __init__(self, gate):
        """Initiate the attributes of the class"""
        self.label = gate
        self.output = None

    def get_label(self):
        """Gets and returns the label for the logic gate"""
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """This class simulates a logic gate with two inputs lines"""

    def __init__(self, n):
        """Initialize the attributes of the parent class. Then intialize
        attributes specify to the BinaryGate class"""
        super().__init__(n)

        self.switchA = None
        self.switchB = None

    def get_switch_a(self):
        if self.switchA is None:
            return int(input(f"Enter switch A input {self.get_label()} -->"))
        else:
            return self.switchA.get_from().get_output()

    def get_switch_b(self):
        if self.switchB is None:
            return int(input(f"Enter switch B input {self.get_label()} -->"))
        else:
            return self.switchB.get_from().get_output()

    def set_next_switch(self, source):
        if self.switchA is None:
            self.switchA = source
        elif self.switchB is None:
            self.switchB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    """This class simulates a logic gate with a single input line NOT gate."""

    def __init__(self, n):
        super().__init__(n)

        self.switch = None  # Attribute that describes the single input
        # switch for the NOT gate

    def get_switch(self):
        return int(input(f"Enter Switch input for gate {self.get_label()} -->"))

    def set_next_switch(self, source):
        if self.switch is None:
            self.switch = source
        else:
            raise RuntimeError("ERROR: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):

        a = self.get_switch_a()
        b = self.get_switch_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):

        a = self.get_switch_a()
        b = self.get_switch_b()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        pin = self.get_switch()

        if pin == 1:
            return 0
        else:
            return 1


class Connector:
    """Model of a connector that allows for the connecting of Logic gates"""

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_switch(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

print(g3.get_output())
