with open('prediction AI/blogtext.csv', 'r', encoding='utf-8') as source_file:
    with open('prediction AI/temp.csv', 'w', encoding='utf-8') as destination_file:
        for i in range(10000):
            line = source_file.readline()
            if not line:  # Break the loop if the end of the file is reached
                break
            destination_file.write(line)
