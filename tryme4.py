# define the new_line function to print a dot
def new_line():
    print('.')

# define the three_lines function to call the new_line function three times
def three_lines():
    new_line()
    new_line()
    new_line()

# define the nine_lines function to call the three_lines function three times
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# define the clear_screen function to call the nine_lines function three times,
# then call the three_lines and new_line functions oncec
def clear_screen():
    for _ in range(3):
        nine_lines()
    three_lines()
    new_line()

# print a placeholder message
print("Printing nine lines")

# call the nine_lines function
nine_lines()

# print another placeholder message
print("Calling clearScreen()")

# call the clear_screen function
clear_screen()