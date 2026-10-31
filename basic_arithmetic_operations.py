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
    #Top teir = Brackets, subdivide into their own list, then perform the 2 teir test on their contents
    #There may be more than 1 set of brackets in an expression
    #Teir 1 = / and *
    #Teir 2 = + and 0

    if(division or multiplication != 0): #Teir 1 Simplification
        h = 0
        while division or multiplication != 0: #can't use for loops as the length changes throughout execution and for loop condition does not change to reflect this,
            if(formatted[h] == '*'):            #Setting the while loops execution to be determined by the amount of types of operations left is efficient, as once all the current teirs operations are executed the required number of times, then the program can terminate      
                calculation = formatted[h-1] * formatted[h+1]
                del formatted[h-1 : h+2] #need to increase final index by 1 as the last index is not included for deleting                     
                formatted.insert(h-1,calculation)
                multiplication = multiplication - 1
                h = h - 1
            if(formatted[h] == "/"):                          
                calculation = formatted[h-1] / formatted[h+1]
                del formatted[h-1 : h+1]                     
                formatted.insert(h-1,calculation)
                division = division - 1
            h = h + 1           
    if(addition or subtraction != 0): #Teir 2 Simplification
        l = 0   
        while l < len(formatted):                           
            if(formatted[l] == "+"):                    
                calculation = formatted[l-1] + formatted[l+1]     
                del formatted[l-1 : l+1]                          
                formatted.insert(l-1,calculation)  
                l = l -1               
            if(formatted[l] == "-"):                    
                calculation = formatted[l-1] - formatted[l+1]     
                del formatted[l-1 : l+1]                          
                formatted.insert(l-1,calculation)
                l = l - 1  
              
    print("Answer :", *formatted)

    #must be condiiton where is len = 3 for formatted, then the final condition is carried out, 
    #How do i know when to stop checking + reducing expression and actually compute it
    #Current, initial format will simply run through list, reducing expression, then carry out final computations

basic_arithmetic()