# loops
# for loop
# while loop

# break statement
# pass statement
# continue statement
# match case

browser = input('Enter the browser name :')
match browser.casefold():
    case 'Chrome':
        print('Chrome is working')
    case 'Firefox':
        print('executing firefox')

    case _:
        print('No browser found')


