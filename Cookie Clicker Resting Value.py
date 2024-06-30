def resting_value(n: int, bankLevel: int) -> None:
    rest = 10 * (n + 1) + bankLevel - 1

    stocks = {
        0: "CRL",
        1: "CHC",
        2: "BTR",
        3: "SUG",
        4: "NUT",
        5: "SLT",
        6: "VNl",
        7: "EGG",
        8: "CNM",
        9: "CRM",
        10: "JAM",
        11: "WCH",
        12: "HNY",
        13: "CKI",
        14: "RCP",
        15: "SBD",
        16: "PBL",
        17: "YOU"
            }
    print(f"the resting value of stock: {stocks.get(n)} is {rest}")


bankLevel = int(input("Input your Cookie Bank level"))
for x in range(0, 18):
    resting_value(x, bankLevel)

