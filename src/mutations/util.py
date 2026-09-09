def mutate_string(string, position, character):
    input_string=list(string)
    input_string[position]=character
    
    return ''.join(input_string)