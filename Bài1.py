def nhap_ds():
    ds = []
    while True:
        ten = input("Ten mon (x thoat): ").strip()
        if ten.lower() == "x":
            break

        if not ten:
            print("Nhap ten")
            continue

        try:
            gia = float(input(f"Gia '{ten}': "))
            if gia < 0:
                print("Gia am")
                continue
        except ValueError:
            print("Nhap so")
            continue

        ds.append({"ten": ten, "gia": gia})

    return ds

def xuat_file(ds, tep="ket_qua_chi_tieu.txt"):
    if not ds:
        print("Khong co du lieu")
        return
    tong = sum(m["gia"] for m in ds)
    m_max = max(ds, key=lambda m: m["gia"])

    with open(tep, "w", encoding="utf-8") as f:
        for i, m in enumerate(ds, 1):
            f.write(f"{i}. {m['ten']}: {m['gia']:,.2f} VND\n")
        f.write(f"Tong: {tong:,.2f} VND\n")
        f.write(f"Cao nhat: {m_max['ten']} ({m_max['gia']:,.2f} VND)\n")

if __name__ == "__main__":
    ds = nhap_ds()
    xuat_file(ds)