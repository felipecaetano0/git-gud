class Singleton:
    __instance = None

    def __new__(cls, x):
        print("Inside new")
        if cls.__instance is None:
            print("Creating a new object")
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, x):
        print("Inside init")
        self.x = x

    def hi(self):
        print("hElLo MoThErFuCkErs")


if __name__ == "__main__":
    s1 = Singleton(1)
    s2 = Singleton(2)
    print(f"s1 == s2 ? {s1 == s2}")

    print(f"s1.x = {s1.x}")
    print(f"s2.x = {s2.x}")

    s1.x = 42
    print(f"s1.x = {s1.x}")
    print(f"s2.x = {s2.x}")
