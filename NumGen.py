#Thanks for using this code

user_input = int(input("Enter A Number: "))
#Main loop
with open('output.txt', 'w') as output_file:
    for i in range(1, user_input + 1):
        output_file.write(str(i) + '\n')
#output saved path
print(f"Output Saved To: 'output.txt'")

