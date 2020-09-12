# Collaborators: none
#
for x in range(2,51):
    print(x)
    remainder = (x%3)
    if remainder == 0:
     print(f"{x}is divisible by 3")
    else:
     print(f"{x}is not divisible by 3")