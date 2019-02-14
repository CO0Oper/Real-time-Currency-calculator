import json
from urllib.request import urlopen
from Currency import Currency

with urlopen("http://www.floatrates.com/daily/usd.json") as response:
    source = response.read()

data = json.loads(source)
currencyArray = []
codeList = []


def fetchData():
    for item in data:
        indiv = data[item]
        code = indiv['code']
        alphaCode = indiv['alphaCode']
        numericCode = indiv['numericCode']
        name = indiv['name']
        rate = indiv['rate']
        date = indiv['date']
        inverseRate = indiv['inverseRate']

        currency = Currency(code, alphaCode, numericCode, name, rate, date, inverseRate)
        currencyArray.append(currency)
        codeList.append(currency.code)


def __existinList__(input):
    try:
        index = codeList.index(input)
    except ValueError:
        print(input + " not found in the array.")
        index = 1.1

    if index >= 0:
        return index


def __useIn__():
    fetchData()

    money = 0.0
    con = False

    while not con:
        main = __existinList__(input("Enter the code of main currency: ").upper())
        if main != 1.1:
            con = True

    con = False
    while not con:
        try:
            money = float(input("Enter how much you want to convert: "))
            if money < 0:
                print("Input must be greater than 0.")
                con = False
            else:
                con = True
        except ValueError:
            print("Invalid input")
            con = False

    con = False

    while not con:
        tempIn = input("Enter the code of target currency: \nor 'a' to list all supported currency code: ")
        if str(tempIn.upper()) == "A":
            print(codeList)
            target = __existinList__(input("Enter the code of target currency: ").upper())
        elif tempIn != "a" or "A":
            target = __existinList__(tempIn.upper())

        if target >= 0:
            print("")
            con = True
        else:
            print("not found")

    fmoney = (money / currencyArray[main].rate) * currencyArray[target].rate
    if round(fmoney, 2) * 1 == 0:
        if round(fmoney, 3) * 1 != 0:
            print("Equals: ", "{0:.3f}".format(round(fmoney, 3)))
    else:
        print("Equals: ", "{0:.2f}".format(round(fmoney, 2)))


def __deck__():
    con = False
    while not con:
        __useIn__()
        if input("Another one? (y)").upper() == "Y":
            con = False
        else:
            con = True


__deck__()

