a = 1
print("")
end =  ["ene","ane","anoic acid","anol"]
start =  ["meth","eth","prop","but","pent","hex","hept","oct","non","dec","undec","dodec"]
valid = []
for i in end:
    for j in start:
        valid.append(j+i)
valid.remove("methene")
while a == 1:
    
    alkane = 0
    alkene = 0
    carbox = 0
    alcohol = 0
    print("\n")
    compound = str(input("Enter the name of your organic compound\n"))
    compound = compound.lower()

    while compound == "methene":
        compound = str(input("Methene does not exist .. enter a valid  compound\n"))
    while compound not in valid:
        compound = str(input("Enter a valid  compound\n"))
    carbon = 0
    dash = ""
    print("","\n")
    if compound[len(compound) - 3:] ==  "ane":
        alkane_carbon_row = ""
        alkane_hydrogen_row = ""
        if compound[0:2] == "me":
            carbon = 1
        elif compound[0:2] == "et":
            carbon = 2
        elif compound[0:2] == "pr":
            carbon = 3
        elif compound[0:2] == "bu":
            carbon = 4
        elif compound[0:2] == "pe":
            carbon = 5
        elif compound[0:3] == "hex":
            carbon = 6
        elif compound[0:3] == "hep":
            carbon = 7
        elif compound[0:2] == "oc":
            carbon = 8
        elif compound[0:2] == "no":
            carbon = 9
        elif compound[0:2] == "de":
            carbon = 10
        elif compound[0:5] == "undec":
            carbon = 11
        elif compound[0:5] == "dodec":
            carbon = 12
        dash = "      |" * (carbon)
        alkane_carbon_row = "C  -   "* (carbon-1)
        alkane_hydrogen_row = "      H"* (carbon)
        print(alkane_hydrogen_row,"\n")
        print(dash,"\n")
        print("H  - ",alkane_carbon_row+"C  - "+"  H\n")
        print(dash,"\n")
        print(alkane_hydrogen_row)
        print("","\n")
        alkane += 1
    elif compound[len(compound) - 3:] == "ene":
        if compound[0:2] == "et":
            carbon = 2
        elif compound[0:2] == "pr":
            carbon = 3
        elif compound[0:2] == "bu":
            carbon = 4
        elif compound[0:2] == "pe":
            carbon = 5
        elif compound[0:3] == "hex":
            carbon = 6
        elif compound[0:3] == "hep":
            carbon = 7
        elif compound[0:2] == "oc":
            carbon = 8
        elif compound[0:2] == "no":
            carbon = 9
        elif compound[0:2] == "de":
            carbon = 10
        elif compound[0:5] == "undec":
            carbon = 11
        elif compound[0:5] == "dodec":
            carbon = 12
        updash = "|      " * (carbon - 2)
        downdash = "|      " * (carbon -2 )
        alkene_carbon_row = "   -  C" * (carbon - 2)
        alkene_hydrogen_down_row = "H      " * (carbon -2)
        alkene_hydrogen_up_row= "H      " * (carbon - 2)
        if carbon >= 2:
            print("    H     H       "+alkene_hydrogen_up_row,"\n")
            print("    |     |"+"       "+updash,"\n")
            print("    C  == C",alkene_carbon_row,"  -  H\n")
            print("    |            ",downdash,"\n")
            print("    H             "+alkene_hydrogen_down_row)
            print("","\n")
            alkene += 1
    elif compound[len(compound) - 3:] == "nol":
        if compound[0:2] == "me":
            carbon = 1
        elif compound[0:2] == "et":
            carbon = 2
        elif compound[0:2] == "pr":
            carbon = 3
        elif compound[0:2] == "bu":
            carbon = 4
        elif compound[0:2] == "pe":
            carbon = 5
        elif compound[0:3] == "hex":
            carbon = 6
        elif compound[0:3] == "hep":
            carbon = 7
        elif compound[0:2] == "oc":
            carbon = 8
        elif compound[0:2] == "no":
            carbon = 9
        elif compound[0:2] == "de":
            carbon = 10
        elif compound[0:5] == "undec":
            carbon = 11
        elif compound[0:5] == "dodec":
            carbon = 12
        alcohol_hydrogen_row = carbon * "      H"
        dash = "      |" * carbon
        alcohol_carbon_row = "C  -   " * carbon
        print(alcohol_hydrogen_row,"\n")
        print(dash,"\n")
        print("H  - ",alcohol_carbon_row+"O  -  H\n")
        print(dash,"\n")
        print(alcohol_hydrogen_row)
        print("\n")
        alcohol += 1
    elif compound[len(compound) - 4:] == "acid":
        if compound[0:2] == "me":
            carbon = 1
        elif compound[0:2] == "et":
            carbon = 2
        elif compound[0:2] == "pr":
            carbon = 3
        elif compound[0:2] == "bu":
            carbon = 4
        elif compound[0:2] == "pe":
            carbon = 5
        elif compound[0:3] == "hex":
            carbon = 6
        elif compound[0:3] == "hep":
            carbon = 7
        elif compound[0:2] == "oc":
            carbon = 8
        elif compound[0:2] == "no":
            carbon = 9
        elif compound[0:2] == "de":
            carbon = 10
        elif compound[0:5] == "undec":
            carbon = 11
        elif compound[0:5] == "dodec":
            carbon = 12
        carbox_hydrogen_row = "      H" * (carbon - 1)
        carbox_carbon_row =   "H" +" -   C " * (carbon)
        dash = "      |" * (carbon - 1)
        print(carbox_hydrogen_row,"          O\n")
        print(dash,"       // \n")
        print(carbox_carbon_row,"\n")
        print(dash,"       \\ \n")
        print(carbox_hydrogen_row,"          O   -   H")
        print("\n")
        carbox += 1

def information(compound):
    global carbox,alkane,alkene,alcohol,carbon
    if carbox == 1:
        print("functional group : COOH\ngeneral formula: C(n)H(2n-1)COOH")
    if alkane == 1:
        print("General formula : C(n)H(2n + 2)")
