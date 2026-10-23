def basic_arithmetic():
    #code to take in equation then append to a formatted list
    expression = input()
    formatted = []
    term = ""
    start = 0
    last_symbol = 0

    brackets = 0
    orders = 0
    addition = 0
    subtraction = 0
    multiplication = 0
    division = 0

    for i in range(len(expression)):
        term = term + expression[i]
        if (expression[i] == "+" or expression[i] == "-" or expression[i] == "*" or expression[i] == "/" or expression[i] == "%" or expression[i] == "**" or expression[i] == "^"):
            formatted.append(float(expression[start:i])) # numbers enter list as floats
            formatted.append(expression[i]) #symbols are strings in the list
            start = i + 1
            last_symbol = i
            if(expression[i] == "+"):
                addition+= 1
            if(expression[i] == "-"):
                subtraction+= 1
            if(expression[i] == "*"):         
                multiplication+= 1         
            if(expression[i] == "/"):
                division+= 1
            if(expression[i] == "^" or "**"):         
                orders+= 1         


    formatted.append(float(expression[last_symbol+1:])) #add last term to list
    print(formatted)

    #BOMDAS and arithmetic calculation
    if(brackets != 0):
        print("Not supported yet") #ADD SUPPORT FOR DETECTING BRACKETS - SEPERATING THEM AS THEIR OWN LIST ELEMENTS, THEN PERFORMING THEIR CALCULATIONS FIRST
    if(orders != 0):
         print("Not supported yet") #ADD SUPPORT FOR DETECTING ORDERS - SEPERATING THEM AS THEIR OWN LIST ELEMENTS, THEN PERFORMING THEIR CALCULATIONS SECOND
    if(addition != 0):
        for h in range(len(formatted)):
            if(type(formatted[h]) != float):#if symbol
                calculation = formatted[h-1] + formatted[h+1]
                del formatted[h-1 : h+1]
                formatted.insert(h-1,calculation)

    print(formatted)

basic_arithmetic()