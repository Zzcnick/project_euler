def NumInWords(n): # Range from 0 to 1000? Why not more?
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    weird  = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    places = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion']
    size   = len(str(n)) # Number of digits.
    times  = (size - 1) / 3
    count  = 0
    final  = ''
    while count < times + 1:
        words = ''
        if (n % 1000) / 100 != 0:
            words += digits[(n % 1000) / 100] + " hundred"
            if n % 100 != 0:
                words += " and "
        if n % 100 > 19:
            words += weird[(n % 100) / 10]
            if n % 10 != 0:
                words += "-" + digits[n % 10]
        elif 0 < n % 100 < 20:
            words += digits[n % 100]
        final = words + " " + places[count] + " " + final
        count += 1
        n = n / 1000
    if final == '':
        final += digits[0]
    return len(final) - final.count(" ") - final.count("-")

zab = 0
for i in range(1, 1001):
    zab += NumInWords(i)
print zab
