def arithmetic_arranger(*args):
    if len(args[0]) > 5:
        arranged_problems = ("Error: Too many problems.")
        return arranged_problems
    secondRow = ""
    firstRow = ""
    spaces = "    "
    highlight = ""
    result = ""
    for element in args[0]:
        elem = element.split()
        if len(elem[0]) > 4 or len(elem[2]) > 4:
            arranged_problems = ("Error: Numbers cannot be more than four digits.")
            return arranged_problems
        try:
            int(elem[0]) and int(elem[2])
        except:
            arranged_problems = ("Error: Numbers must only contain digits.")
            return arranged_problems
        if len(elem[0]) <= len(elem[2]):
            secondElem = (f"{elem[1]} {elem[2]}")
            firstElem = (" " * (len(secondElem) - len(elem[0]))) + elem[0]
        elif len(elem[0]) > len(elem[2]):
            firstElem = "  " + elem[0]
            secondElem = elem[1] + (" " * ((len(elem[0]) - len(str(elem[2])))+1)) + elem[2]
        dashes = "-" * len(secondElem)
        strResult = str(eval(element))
        akapit = " " * (len(secondElem) - len(strResult))
        if len(result) < 1:
            result = result + akapit + (strResult)
        else:
            result = result + spaces + akapit + strResult
        if len(firstRow) < 1:
            firstRow = firstElem
            secondRow = secondRow + secondElem
            highlight += dashes
        elif len(firstRow) >= 1:
            firstRow = firstRow + spaces + firstElem
            secondRow = secondRow + spaces + secondElem
            highlight = highlight + spaces + dashes
        if elem[1] == "+" or elem[1] == "-":
            continue
        else:
            arranged_problems = ("Error: Operator must be '+' or '-'.")
            return arranged_problems
    if len(args) == 1:
       arranged_problems = (f'{firstRow}\n{secondRow}\n{highlight}')
    if len(args) == 2:
        if args[1] == True:
            arranged_problems = (f"""{firstRow}\n{secondRow}\n{highlight}\n{result}""")
    return arranged_problems

arithmetic_arranger(['3801 - 2', '123 + 49'])