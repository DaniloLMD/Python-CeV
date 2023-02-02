def leiadin(x):
    while True:
        c = 0
        res = input(x).strip().replace(',','.')
        if '-' in res and res.count('-') == 1 and res.count('.') <= 1:
            for v in res:
                if v in '-.0123456789':
                    c += 1
            if len(res) == c:
                return float(res)
            else:
                print('O valor digitado não é aceito!')

        elif res.count('.') <= 1:
            for v in res:
                if v in '.0123456789':
                    c += 1
            if c == len(res):
                return float(res)
            else:
                print('O valor digitado não é aceito!')
        else:
            print('O valor digitado não é aceito!')