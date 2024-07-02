def resting_value(n: int, bankLevel: int) -> str:
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
    return f"the resting value of stock: {stocks.get(n)} is {rest} \n"


bankLevel = int(input("Input your Cookie Bank level"))
check = input("Would you like to write the output to a TXT file? y/n")
if check == "y":
    with open("results.txt" , "w") as txtfile:
        for x in range (0,18):
            txtfile.writelines(resting_value(x, bankLevel))

if check == "n":
    for x in range(0, 18):
        print(resting_value(x, bankLevel))


