while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is sufficient length')
    # 自此處起繼續其他任何處理
