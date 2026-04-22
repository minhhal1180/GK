import matplotlib.pyplot as plt

def main():
    sl = {"Laptop": 10, "Mouse": 50, "Keyboard": 30}
    gia = {"Laptop": 800, "Mouse": 15, "Keyboard": 45}
    dt = {sp: n * gia.get(sp, 0) for sp, n in sl.items()}

    print("Bao cao")
    for sp, n in sl.items():
        g = gia.get(sp, 0)
        print(f"{sp}: {n} x ${g} = ${dt[sp]:,.2f}")
    print(f"Tong: ${sum(dt.values()):,.2f}")

    x, y = list(sl), list(sl.values())
    bars = plt.bar(x, y, color=["#5081D0", "#4BC367", "#8F4749"])
    plt.title("So luong da ban")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    for b in bars:
        h = b.get_height()
        plt.text(b.get_x() + b.get_width() / 2, h + 0.5, int(h), ha="center")

    plt.show()

if __name__ == "__main__":
    main()