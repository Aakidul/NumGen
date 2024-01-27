#Thanks for using this code

user_input = int(input("Enter a number: "))

with open('output.txt', 'w') as output_file:
    for i in range(1, user_input + 1):
        output_file.write(str(i) + '\n')

print(f"Output has been saved to 'output.txt'")

