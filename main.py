import abc

from State import StartState, State


class MyGrammarCheck:
    def __init__(self):
        self.state = StartState(self)

    def changeState(self, state: State):
        self.state = state

    def check(self, str):
        self.changeState(StartState(self))
        for char in str:
            self.state.process(char)

        return self.state.accepted


def main():
    grammar = MyGrammarCheck()
    print(grammar.state)
    print(grammar.check("aaaaaaaaa"))
    print(grammar.state)
    print(grammar.check("aa"))
    print(grammar.state)
    print(grammar.check("abca"))
    print(grammar.state)
    print(grammar.check("bcaa"))
    print(grammar.state)


if __name__ == '__main__':
    main()
