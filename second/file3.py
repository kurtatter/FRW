class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


def main():
    sharik = Dog(name="Шарик")
    print(sharik.name)

if __name__ == "__main__":
    main()