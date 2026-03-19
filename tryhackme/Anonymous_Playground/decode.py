str_input = "hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN"
password = ""

# Loop through the string in steps of 2
for i in range(0, len(str_input), 2):
    val1 = ord(str_input[i]) - 96
    val2 = ord(str_input[i + 1]) - 64

    t = (val1 + val2 - 1) % 26 + 1

    password += chr(t + 96)

print(password)
