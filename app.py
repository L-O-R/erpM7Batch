with open('text.txt','r') as f:
    for line in f:
        line = line.strip()
        data = line.split('|')
        print(data)