def make_thread(t):
    print(f"Starting to make {t} thread")
    print(f"Made thread with lots of wool")
    return f"{t} thread"


def make_cloth(c):
    print(f"Starting to make {c} clothes")
    supplies = make_thread(c * 100)
    print(f"Made cloth with {supplies}")
    return f"{c} cloth"


def make_shirts(s):
    print(f"Starting to make {s} shirts")
    supplies = make_cloth(s * 3)
    print(f"Made shirt with {supplies}")
    return f"{s} shirt"


if __name__ == "__main__":
    result = make_shirts(1)
