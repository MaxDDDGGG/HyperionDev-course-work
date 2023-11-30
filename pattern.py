row_number = 5
# Created a range from 1 to 2 * row number (up to but not inlcuding 10)
for i in range(1, 2 * row_number):

    # If i is less than or equal to the row number print '*' for the row number where the maximum row number is 5.
    if i <= row_number:
        print('*' * i)

    # If i is not less than or equal to the row number, print 2 * row number (5) - i
    else:
        print('*' * (2 * row_number - i))

'''
Helper Trace table:
i = 1 -- 1≤51≤5 (True), Output: Print 1 * '*'
i = 1 -- 2≤52≤5 (True), Output: Print 2 * '*'
i = 1 -- 3≤53≤5 (True), Output: Print 3 * '*'
i = 1 -- 4≤54≤5 (True), Output: Print 4 * '*'
i = 1 -- 5≤55≤5 (True), Output: Print 5 * '*'
i = 1 -- 6≤56≤5 (False), Output: Print 2 * 5 - 6 = 4 * '*'
i = 1 -- 7≤57≤5 (False), Output: Print 2 * 5 - 7 = 3 * '*'
i = 1 -- 8≤58≤5 (False), Output: Print 2 * 5 - 8 = 2 * '*'
i = 1 -- 9≤59≤5 (False), Output: Print 2 * 5 - 9 = 1 * '*'
'''