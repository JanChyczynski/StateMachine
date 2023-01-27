import abc


class State(abc.ABC):
    def __init__(self, grammar):
        self.grammar = grammar
        self.accepted = False

    @abc.abstractmethod
    def process(self, input: str):
        pass


class AcceptingState(State):
    def __init__(self, grammar):
        super().__init__(grammar)
        self.accepted = True


class StartState(AcceptingState):
    def process(self, char: str):
        if char == 'a':
            self.grammar.changeState(AState(self.grammar))
        elif char == 'b':
            self.grammar.changeState(CState(self.grammar))
        else:
            self.grammar.changeState(RejectState(self.grammar))


class AState(AcceptingState):
    def process(self, char: str):
        if char == 'a':
            self.grammar.changeState(AState(self.grammar))
        elif char == 'b':
            self.grammar.changeState(BState(self.grammar))
        else:
            self.grammar.changeState(RejectState(self.grammar))


class BState(AcceptingState):
    def process(self, char: str):
        if char == 'a':
            self.grammar.changeState(EndState(self.grammar))
        elif char == 'b':
            self.grammar.changeState(BState(self.grammar))
        else:
            self.grammar.changeState(RejectState(self.grammar))


class CState(AcceptingState):
    def process(self, char: str):
        if char == 'a':
            self.grammar.changeState(CState(self.grammar))
        elif char == 'c':
            self.grammar.changeState(BState(self.grammar))
        else:
            self.grammar.changeState(RejectState(self.grammar))


class EndState(AcceptingState):
    def process(self, input: str):
        if input != "":
            self.grammar.changeState(RejectState(self.grammar))


class RejectState(State):
    def __init__(self, grammar):
        super().__init__(grammar)
        self.accepted = False

    def process(self, char: str):
        pass
