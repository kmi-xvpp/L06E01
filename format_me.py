output_prefix = 'Result'

input_number=42

tmp = input_number % 2

if ( tmp > 0 ) == True:
    result = "odd"
else:
    result = "even"

print(f"{output_prefix}: number {input_number} is {result}, since division remainder is {tmp}.")