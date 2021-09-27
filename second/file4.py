class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


def main():
    mars = Cat(name="Mars")
    print(mars.name)


if __name__ == "__main__":
    main()