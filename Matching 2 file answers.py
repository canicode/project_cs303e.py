def readline():
    with open("TriviaQuestions.txt") as f, open ("TriviaAnswers.txt") as f2:
        d1_lines = {}
        for line in f:
            d1_lines[line.strip()] = 0

        st = set(map(str.rstrip,f))
        for line in f2:
            first = line.split(("|")[0].strip())
            if first in d1_lines:
                print("line.strip()")

        '''for line in f2:
            spl = line.split(None, 1)[0]
            if spl in st:
                print(line.rstrip())'''

readline()