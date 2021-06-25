def input_to_command_transform(input_message):
    user_input = input(input_message)

    user_input_divide = user_input.split()
    command = user_input_divide[0]
    arguments = ""

    for arg in user_input_divide[1:]:
        arguments = arguments + '"' + arg + '",'

    if arguments:
        executed_method = command + "(" + arguments[:-1] + ")"
    else:
        executed_method = command + "()"

    return (command, executed_method)
