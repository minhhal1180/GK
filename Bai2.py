def chuan_hoa(s):
    return " ".join(s.split()).title()

def sap_xep_ten(ds):
    return sorted(ds, key=lambda t: t.split()[-1])

if __name__ == "__main__":
    ds = [" nguYen   vaN a ", "tRAn tHi b", "   le hoang    c", "pHam   thi Diem"]

    print("Goc:")
    for t in ds:
        print(f"- {t}")

    ds_ch = [chuan_hoa(t) for t in ds]
    print("\nChuan hoa:")
    for t in ds_ch:
        print(f"- {t}")

    ds_sx = sap_xep_ten(ds_ch)
    print("\nSap xep:")
    for t in ds_sx:
        print(f"- {t}")