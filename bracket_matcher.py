

# Given a string made up of brackets []{}() make sure they match in the right order without
# stack.
# [{}] ---------> Valid
# (()()) ---------> Valid
# {] ---------> Invalid
# [()]))() ---------> Invalid
# []{}({}) ---------> Valid
# [{]} ---------> Invalid

strings = ["[{}]","(()())","{]","[()]))()","[]{}({})","[{]}","[[]]"]
opening_brackets = ["[","{","("]
bracket_mapping = {
    "[":"]",
    "{":"}",
    "(":")",
}
def validate_brackets(string:str):
    valid = True
    original_string = string
    while len(string) != 0:

        # checking if first element is an opening bracket
        if string[0] in opening_brackets:
            found = False
            # Finding closing bracket for opening bracket.
            for j in range(1,len(string),2):
                # Checking if the closing bracket is the right one for the opening bracket
                if(string[j]==bracket_mapping[string[0]]):
                    found = True

                    # Removing the opening and closing brackets so that the first element of string
                    # changes.
                    string = string[1:j] + string[j+1:]
                    break
            # When couldnt find closing closing bracket
            if not found:

                valid = False
                break

        # What to do if there is a closing bracket without an opening bracket
        # eg :- }][]()
        else:
            valid = False
            break


    print(original_string,'--------->',"Valid" if valid else "Invalid")

for i in strings:
    validate_brackets(i)

