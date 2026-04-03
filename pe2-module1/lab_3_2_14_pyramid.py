blocks = int(input("Please enter the number of block:"))
block_required = 1
layer = 0

while blocks >= block_required:
    blocks -= block_required
    layer += 1
    block_required += 1
print(layer)