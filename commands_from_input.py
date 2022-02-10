if __name__ == '__main__':
    N = int(input())
    count = 0
    final_list = []
    command_list = []
    temp_input = []
    remove_command_input = []
    while count < N:
        command_list.append(input())
        count += 1
    #print (command_list)
    for command in command_list:
        # Insert Command
        if "insert" in command:
            temp_input = command.split()
            final_list.insert(int(temp_input[1]), int(temp_input[2]))

        # Print Command
        elif "print" in command:
            print(final_list)

        # Remove Command
        elif "remove" in command:
            temp_input = command.split()
            final_list.remove(int(temp_input[1]))

        # Append Command
        elif "append" in command:
            temp_input = command.split()
            final_list.append(int(temp_input[1]))

        # Sort Command
        elif "sort" in command:
            final_list.sort()

        # Pop Command
        elif "pop" in command:
            final_list.pop(-1)

        # Reverse Command
        elif "reverse" in command:
            final_list.reverse()

    #print ("Final List:{}".format(final_list))
