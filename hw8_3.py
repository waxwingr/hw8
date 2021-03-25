def hw8_3_function(path):
    import re
    with open("output.txt", "x") as output:
        with open(path, "r") as f:

            for line in f:
                split_line = re.split("(\d+)", line)
                letters = []
                digits = []
                new_list = []

                for symbol in split_line:
                    try:
                        new_list.append(int(symbol))
                    except(ValueError):
                        new_list.append(symbol)

                for item in new_list:
                    if isinstance(item, int):
                        digits.append(item)
                    else:
                        letters.append(item)

                zipped = zip(letters, digits)
                string = ""

                for k, v in zipped:
                    string += (k * v)
                output.write(string + "\n")

