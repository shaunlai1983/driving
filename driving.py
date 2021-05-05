contries = input ('請問你的國家: ')
age = input('請問你的年齡')
age = int(age)

if contries == '台灣':    #
	if age >= 18:   
	    print('你可以開車喔')
	else:
	    print('你還不可以開車喔')
elif contries == '美國':  #I條件沒符合上面的If 需求就檢查是否符合這一行
	if age >= 16:   
	    print('你可以開車喔')
	else:
	    print('你還不可以開車喔')
else :                   #if and elif 都沒有符合條件的話就執行的話就這一行
	print('只能輸入台灣或者美國喔!')

#使用If , elif , else 檢查Contries 的條件 
#Line 5 第一關 Line 10第二關 Line 15第一跟二關沒執行就直接執行此行結果

