def add_everything_up(arg1,arg2):
    try:
        result=arg1+arg2
    except TypeError:
        result=str(arg1)+str(arg2)
    return result
def main():
    print(add_everything_up(123.456,'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456,7))
if __name__ == '__main__':
    main()