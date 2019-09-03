def search(bc):
    err_occur = []
    out = open('CIFout.txt', 'w')
    count = 0
    try:
        with open('C:\\CIF.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if line.lower().find(bc) != -1:
                    err_occur.append((linenum, line.rstrip('\n')))
                    for linenum, line in err_occur:
                        print("Line ", linenum, ": ", line, sep='')
                        count += 1
                    print(count)
                    out.write(line + '\n')
    except FileNotFoundError:
        print("Log file not found.")
        out.write('None' + '\n')
    out.close()

def effective(Eff):
    err_occur1 = []
    out = open('CIFout_Effective.txt', 'w')
    count = 0
    try:
        with open('CIFout.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if line.find(Eff) != -1:
                    err_occur1.append((linenum, line.rstrip('\n')))
                    for linenum, line in err_occur1:
                        print("Line", linenum, ": ", line, sep='')
                    count += 1
                    print(count)
                    out.write(line + '\n')
    except FileExistsError:
        print("Log file not found.")
        out.write('None' + '\n')
    out.close()
Eff = 'Effective'
bc = str(input("Enter BC Number: "))
bc1 = '¦' + bc + '¦'
print(bc1)
search(bc1)
print(Eff)
effective(Eff)

