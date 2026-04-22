import random

FILE_KL = "ky_luc_doan_so.txt"

def doc_kl():
    try:
        with open(FILE_KL, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return None

def luu_kl(n):
    k = doc_kl()
    if k is None or n < k:
        with open(FILE_KL, "w") as f:
            f.write(str(n))

def choi():
    sbm, max_l = random.randint(1, 100), 7
    print(f"\nDoan 1-100 / {max_l} luot")
    if (k := doc_kl()) is not None:
        print(f"Ky luc: {k}")

    for l in range(1, max_l + 1):
        s = input(f"\n{l}/{max_l} So (x thoat): ").strip().lower()
        if s == "x":
            return False
        try:
            d = int(s)
        except ValueError:
            print("Nhap so")
            continue

        if d == sbm:
            print(f"Dung: {sbm} ({l} luot)")
            luu_kl(l)
            return True
        print("Lon hon" if d < sbm else "Nho hon")

    print(f"\nHet luot, So: {sbm}")
    return True

if __name__ == "__main__":
    while choi():
        if input("\nChoi tiep y/x: ").strip().lower() != "y":
            break
    print("Tam biet")