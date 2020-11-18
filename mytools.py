def queue_from_txt(filename):
    while True:
        with open(filename, 'r') as r:
            line = r.readline()
            if not line:
                break
            temp = r.read()
        yield line.strip()

        with open(filename, 'w') as w:
            w.write(temp)
