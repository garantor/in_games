import re



class StringCalculator:
    def __init__(self) -> None:
        pass

    def Add(self, numbers):
        if numbers == "":  # checking for empty input numbers
            return 0
        else:
            # if number is valid and not empty
            delimiter = ","  # setting the delimiter for separating the input values
            if numbers[:2] == "//":  # checking for delimiter setter
                _delimiter = re.search(
                    "(?<=\[).*(?=\])", numbers )  # using regular expression to search through the input values and group it, creating the custom delimiter
                
                delimiter = _delimiter.group()
                numbers = numbers[numbers.index("\n") + 1 :]
                print(numbers)
                # starting at the index one after the first instance of the new line (string "\n")
                # the index() helps us find the first instance of \n and we add 1, 
                # this should include all character after the new line

            mod_numbers = re.sub(delimiter, ",", numbers) 
            # the above line of code is using the sub() function from the 
            # re module to replace all occurrences of the delimiter variable with a "," 
            # in the numbers variable and returns the modified string.
            #using re sub method we are able to check for
            
            replaced_numbers = mod_numbers.replace("\n", ",")
            #the above code replace all occupance of the newline

            empty_numbers = [int(x) for x in replaced_numbers.split(",") if x != ""]

            negatives = [x for x in empty_numbers if x < 0] #using list compherention to check for negative values

            if negatives:

                raise Exception(
                    f"negatives {str(negatives[0])} not allowed") #raise the default exception if it found a negative value
                

            sum_numbers = [x if x <= 1000 else 0 for x in empty_numbers] #using list comprehension to get list of numbers

            return sum(sum_numbers) #use python built in sum method to sum total 

if __name__ == '__main__':
    stringInput = input("enter your numbers separated by comma ")
    adc = StringCalculator()
    output = adc.Add(stringInput)
    print(output)
