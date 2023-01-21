import re



class StringCalculator:
    def __init__(self) -> None:
        pass


    def custom_delimiter(self, numbers:str):
        '''
        create a custom delimiter to handle all custom delimeters
        '''
        if numbers[:2] == "//":  # checking for delimiter setter
            num = numbers.replace("//", '').replace('\n', '') #replaced both the // and new line with an empty string
            patterns = re.compile(r'[^***%;\[\]]')  #using regex pattern to check for special character used as delimiter for the numbers
            p_nums = patterns.finditer(num) #using finditer helps to comb through the string and return what matches the pattern
            list_number = [] 
            for i in p_nums: #loop through our result and append it to the empty list created above
                list_number.append(int(i.group(0)))
            return list_number

    def Add(self, numbers):
        if numbers == "":  # checking for empty input numbers
            return 0
        else:
            # if number is valid and not empty
            delimiter = ","  # setting the delimiter for separating the input values
            if numbers[:2] == "//":  # checking for delimiter setter
                empty_numbers = self.custom_delimiter(numbers)

            else:
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
