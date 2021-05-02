# String Exercises

# INSTRUCTIONS

# Add a comment above each line of code describing what it does.
# Be specific. Use multiple comment lines if you need to
# OR write code below the comments requesting code.
# Make sure your file runs and generates the correct results.

def main():
    # define variable str1 with string "Hello"
    str1 = "Hello"
    # print out the 2nd letter of str1
    print(str1[1])

    # ASSIGNMENT QUESTIONS START HERE
    print(str1[-2])
    print(str1[:3])
    print(str1[2:len(str1)-1])
    str2 = "World"
    print(str1+str2)

    # write code below to iterate over str1 and print each character
    # separated by a space in a single line
    # Your code goes here

    # write code below. Create 2 lists. Print each. Print concatenation of them.
    # Your code goes here

    # write code that demonstrates you can append to list1 created above
    # Your code goes here

    # write code that demonstrates parsing of an input phrase into words in a list'
    # Your code goes here

    # write code that gets pi from the math library and outputs as "3.14"
    # using string formatting.
    # Your code goes here

    # in the code below, what does line[:-1] evaluate to?
    # assume infile has been opened for reading a text file
    # assume infile is a text file with multiple lines each line ending with
    # a carriage return/linefeed character
    # NOTE: you are just being asked to answer the questions above. DO NOT
    # uncomment the code below.
    '''
    for line in infile:
        print(line[:-1])
    '''


main()
