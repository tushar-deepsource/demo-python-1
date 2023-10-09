"""Complexity test file"""


def function():
    """method one docstring."""

    def inner(f, a):
        """Functions don't increase complexity"""

    class A:
        "neither do classes"

        if x > y:
            for i in range(10):
                print([i * j for j in range(1, i)])

    print(x if x > 10 else y)
    print(x or y or z or w or v or u or t and foo and bar)

    while True:
        print(list(x for x in "123" if True))


def num_to_word(x):
    """Converts numbers to words"""
    if x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    elif x == 4:
        return "four"
    elif x == 5:
        return "five"
    elif x == 6:
        return "six"
    elif x == 7:
        return "seven"
    elif x == 8:
        return "eight"
    elif x == 9:
        return "nine"
    elif x == 10:
        return "ten"
    elif x == 11:
        return "eleven"
    elif x == 12:
        return "twelve"
    elif x == 13:
        return "thirteen"
    elif x == 14:
        return "fourteen"
    elif x == 15:
        return "fifteen"
    else:
        return "this doesn't count"


class C:
    """Test class"""

    def __init__(self, a, b):
        """Complexity is 3, don't raise."""
        for i in a:
            for j in b:
                print(i or j)

    def method_one(self, a, b):
        """Complexity here is 18, raise."""
        print(
            [
                x
                for i in a
                for j in i
                for k in j.items()
                if k["foo"] == "stuff" or k["a"] or k["b"] or k["c"] or k["x"] or k["y"]
                for stuff in k["foo"].bar
                if stuff.value > 10
                for items in stuff.items
                for x in items.values
                if (
                    any(something.foo == 42 for something in x)
                    and x.last in (1, 2, 3)
                    or x.first == 0
                )
            ]
        )

    def method_two(self, a):
        """Complexity is 17, raise."""
        return (
            "one"
            if a == 1
            else "two"
            if a == 2
            else "three"
            if a == 3
            else "four"
            if a == 4
            else "five"
            if a == 5
            else "six"
            if a == 6
            else "seven"
            if a == 7
            else "eight"
            if a == 8
            else "nine"
            if a == 9
            else "ten"
            if a == 10
            else "eleven"
            if a == 11
            else "twelve"
            if a == 12
            else "thirteen"
            if a == 13
            else "fourteen"
            if a == 14
            else "fifteen"
            if a == 15
            else "sixteen"
            if a == 16
            else "too big"  # else doesn't count in complexity
        )

    def method_three(self):
        """Complexity here is 16. raise."""
        try:
            foo()
        except OneError:
            print("One")
        except TwoError:
            print("Two")
        except ThreeError:
            print("Three")
        except FourError:
            print("Four")
        except FiveError:
            print("Five")
        except SixError:
            print("Six")
        except SevenError:
            print("Seven")
        except EightError:
            print("Eight")
        except NineError:
            print("Nine")
        except TenError:
            print("Ten")
        except ElevenError:
            print("Eleven")
        except TwelveError:
            print("Twelve")
        except ThirteenError:
            print("Thirteen")
        except FourteenError:
            print("Fourteen")
        except FifteenError:
            print("Fifteen")
        else:
            print("this doesn't count")

    def method_four(self):
        """Complexity here is 16. Raise."""
        match foo:
            case OneError():
                print("One")
            case TwoError():
                print("Two")
            case ThreeError():
                print("Three")
            case FourError():
                print("Four")
            case FiveError():
                print("Five")
            case SixError():
                print("Six")
            case SevenError():
                print("Seven")
            case EightError():
                print("Eight")
            case NineError():
                print("Nine")
            case TenError():
                print("Ten")
            case ElevenError():
                print("Eleven")
            case TwelveError():
                print("Twelve")
            case ThirteenError():
                print("Thirteen")
            case FourteenError():
                print("Fourteen")
            case _:
                print("this DOES count")

    def method_five(self):
        """Complexity here is 12, don't raise here."""
        match foo:
            case OneError():
                print("One")
            case TwoError():
                print("Two")
            case ThreeError():
                print("Three")
            case FourError():
                print("Four")
            case FiveError():
                print("Five")
            case SixError():
                print("Six")
            case SevenError():
                print("Seven")
            case EightError():
                print("Eight")
            case NineError():
                print("Nine")
            case TenError():
                print("Ten")
            case _:
                print("this DOES count")
