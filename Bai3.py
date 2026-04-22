def c2f(c):
    return (c * 9 / 5) + 32

def f2c(f):
    return (f - 32) * 5 / 9

def u2v(u, tg):
    return u * tg

def main():
    m = 0
    while True:
        try:
            if m == 0:
                c = float(input("\nC->F / C: "))
                print(f"KQ: {c}C = {c2f(c):.2f}F")
            elif m == 1:
                f = float(input("\nF->C / F: "))
                print(f"KQ: {f}F = {f2c(f):.2f}C")
            else:
                u = float(input("\nUSD->VND / USD: "))
                tg = float(input("Tg: "))
                print(f"KQ: {u} USD = {u2v(u, tg):,.2f} VND")
        except ValueError:
            print("Nhap so")

        cmd = input("Enter tiep (x): ").strip().lower()
        if cmd == "x":
            break
        m = (m + 1) % 3

if __name__ == "__main__":
    main()