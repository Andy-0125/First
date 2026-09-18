# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]
credit_number = "1234-5678-9109"
last_digits = credit_number[-4:]
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[4:])
print(credit_number[-1])
print(f"XXXX-XXXX-XXXX-{last_digits}")
print(credit_number[3::2])
print(credit_number[9::-1])