from pip._vendor.distlib.compat import raw_input
import time
import os

symbollist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T" , "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numberofcharacters = 0
mincharacters = 0
maxcharacters = 0
filenum = 0

for i in range(1, 1000):
    if os.path.exists("BRUTEFORCE" + str(i) + ".txt"):
        print("BRUTEFORCE" + str(i) + ".txt" + " already exists.")
    elif i == 1000:
        print("ERROR: You already got 1000 Bruteforce lists...")
        break
    else:
        print("Creating new file...")
        time.sleep(1)
        file = open("BRUTEFORCE" + str(i) + ".txt", "w")
        filenum = i
        break

def createList(numberc, minc, maxc, filenumber):
    different = 0
    if int(minc) <= 1 and int(maxc) >= 1 or numberc == "1":
        for symbol in symbollist:
            file.write(symbol + "\n")
            print(symbol)
            different = different + 1

    if int(minc) <= 2 and int(maxc) >= 2 or numberc == "2":
        for symbol in symbollist:
            for symbol2 in symbollist:
                file.write(symbol + symbol2 + "\n")
                print(symbol + symbol2)
                different = different + 1

    if int(minc) <= 3 and int(maxc) >= 3 or numberc == "3":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    file.write(symbol + symbol2 + symbol3 + "\n")
                    print(symbol + symbol2 + symbol3)
                    different = different + 1

    if int(minc) <= 4 and int(maxc) >= 4 or numberc == "4":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        file.write(symbol + symbol2 + symbol3 + symbol4 + "\n")
                        print( symbol + symbol2 + symbol3 + symbol4)
                        different = different + 1

    if int(minc) <= 5 and int(maxc) >= 5 or numberc == "5":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            file.write(symbol + symbol2 + symbol3 + symbol4 +symbol5 + "\n")
                            print(symbol + symbol2 + symbol3 + symbol4 + symbol5)
                            different = different + 1

    if int(minc) <= 6 and int(maxc) >= 6 or numberc == "6":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                file.write(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + "\n")
                                print(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6)
                                different = different + 1

    if int(minc) <= 7 and int(maxc) >= 7 or numberc == "7":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                for symbol7 in symbollist:
                                    file.write(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + "\n")
                                    print(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7)
                                    different = different + 1

    if int(minc) <= 8 and int(maxc) >= 8 or numberc == "8":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                for symbol7 in symbollist:
                                    for symbol8 in symbollist:
                                        file.write(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + "\n")
                                        print(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8)
                                        different = different + 1

    if int(minc) <= 9 and int(maxc) >= 9 or numberc == "9":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                for symbol7 in symbollist:
                                    for symbol8 in symbollist:
                                        for symbol9 in symbollist:
                                            file.write(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + "\n")
                                            print(symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9)
                                            different = different + 1

    if int(minc) <= 10 and int(maxc) >= 10 or numberc == "10":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                for symbol7 in symbollist:
                                    for symbol8 in symbollist:
                                        for symbol9 in symbollist:
                                            for symbol10 in symbollist:
                                                file.write(
                                                    symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + symbol10 + "\n")
                                                print(
                                                    symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + symbol10)
                                                different = different + 1

    if int(minc) <= 11 and int(maxc) >= 11 or numberc == "11":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                for symbol7 in symbollist:
                                    for symbol8 in symbollist:
                                        for symbol9 in symbollist:
                                            for symbol10 in symbollist:
                                                for symbol11 in symbollist:
                                                    file.write(
                                                        symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + symbol10 + symbol11 + "\n")
                                                    print(
                                                        symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + symbol10 + symbol11)
                                                    different = different + 1

    if int(minc) <= 12 and int(maxc) >= 12 or numberc == "12":
        for symbol in symbollist:
            for symbol2 in symbollist:
                for symbol3 in symbollist:
                    for symbol4 in symbollist:
                        for symbol5 in symbollist:
                            for symbol6 in symbollist:
                                for symbol7 in symbollist:
                                    for symbol8 in symbollist:
                                        for symbol9 in symbollist:
                                            for symbol10 in symbollist:
                                                for symbol11 in symbollist:
                                                    for symbol12 in symbollist:
                                                        file.write(
                                                            symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + symbol10 + symbol11 + symbol12 + "\n")
                                                        print(
                                                            symbol + symbol2 + symbol3 + symbol4 + symbol5 + symbol6 + symbol7 + symbol8 + symbol9 + symbol10 + symbol11 + symbol12)
                                                        different = different + 1

    file.close()
    print("Finished! Your list is saved as \"BRUTEFORCE" + str(filenumber) + ".txt\"")
    print(str(different) + " different passwords generated.")
    time.sleep(3)


certaincharacter = raw_input("Do you know the exact number of characters for the password? [y/n]\n")
if certaincharacter == "y":

    numberofcharacters = raw_input("What's the exact number of characters for the password? (1-12)\n")
    createList(numberofcharacters, mincharacters, maxcharacters)

elif certaincharacter == "n":

    mincharacters = raw_input("What are the minimum of characters you want to have? (1-12)\n")
    maxcharacters = raw_input("What is the maximum of characters you want to have? (1-12)\n")
    createList(numberofcharacters, mincharacters, maxcharacters, filenum)

else:
    print("ERROR...")
    time.sleep(3)

