# Payton Womack

# Write a program to convert roman numerals to decimal numbers and decimal
# numbers back to roman numerals to check their accuracy.
# There are seven basic roman numerals:
# I= 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# IV = 4, XL = 40, XC = 90, CD = 400, CM = 900.

# Roman to integer class created
class Roman():
    # Conversion method that receives the inputted Roman numeral (s)
    def conversion(self, s):
        # Dictionary with letter conversions
        romanNum = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        # Total for the conversion of the Roman numeral
        integer = 0
        # for loop to go through each character in length of Roman numeral
        for iCount in range(len(s)):
            if iCount > 0 and romanNum[s[iCount]] > romanNum[s[iCount - 1]]:
                integer += romanNum[s[iCount]] - 2 * romanNum[s[iCount - 1]]
            else:
                integer += romanNum[s[iCount]]
        return integer
    
# Integer to Roman class created
class Integer():
    # Reversion method that receives the inputted integer (n)
    def reversion(self, n):
        # Another dictionary
        romanNum = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        roman = ""
        for value, symbol in romanNum.items():
            while n >= value:
                roman += symbol
                n -= value
        return roman

# Choose conversion option
decision = input("Enter the following options to choose a conversion\n(I) Integer to Roman numeral\n(R) Roman numeral to Integer\n\n").upper()
if decision == 'R':
    # INPUT: Gets Roman numeral from user
    RomanNum = input("\nEnter a Roman numeral (i.e. XIV): ").upper()

    # Avoid crashing if input isn't valid
    try:
        oRomanNum = Roman().conversion(RomanNum)
        print(oRomanNum)
    except KeyError:
        print("Invalid input: not a valid Roman numeral")

elif decision == 'I':
    # INPUT: Gets integer from user
    n = int(input("\nEnter an integer: "))
    oRomanNum = Integer().reversion(n)
    print(oRomanNum)