drive = input('你有沒有開過車? : ')
if drive != 'yes' and drive != 'no':
    print('只能輸入 yes/no')
    raise SystemExit

age = input('請輸入年齡 : ')
age = int(age)

if drive == 'yes':
    if age >= 18:
        print('你很棒')
    else:
        print('你不行開車')
elif drive == 'no':
    if age >= 18:
        print('你要去考駕照')
    else:
        print('很棒，你再過', 18-age, '年，就可以考駕照了')