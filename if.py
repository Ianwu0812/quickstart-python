number = 23
guess = int(input('Enter an integer : '))


if guess == number:
    # 新塊從這裡開始
    print('Congratulaion, you guessd it.')
    print('(but you can not win any prizes!)')
    # 新塊在這裡結束
elif guess < number:
    # 另一個代碼塊
    print ('No, it is a little higher than that')
    # 你可以在此做任何你希望在該代碼塊內進行的事情
else:
    print('No, it is a little lower than that')

print('Done')
# 這最後一句將在
# if 語句執行完畢後執行

if True:
    print('Yes, it is true')

