import numpy as np

def sign_int3(content):
    sample_b = []
    for i in range(len(content)):
        sample_b.append(content[i])
    for i in range(len(sample_b) // 3):
        if sample_b[3 * i + 2] > 127:
            sample_b[3 * i + 2] = sample_b[3 * i + 2] - 255
            sample_b[3 * i + 1] = sample_b[3 * i + 1] - 255
            sample_b[3 * i] = sample_b[3 * i] - 256
    return sample_b

content = [45, 255, 255, 45, 255, 255]
print(sign_int3(content))
