contries = input ('請問你的國家: ')
age = input('請問你的年齡')
age = int(age)

if contries == '台灣':
	if age >= 18:   
	    print('你可以開車喔')
	else:
	    print('你還不可以開車喔')
elif contries == '美國':
	if age >= 16:   
	    print('你可以開車喔')
	else:
	    print('你還不可以開車喔')