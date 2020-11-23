# this game lets you print out pascal's triangle
def pascal(curr,row,p_list):
    if row == curr:
        print p_list
        return True
    else:
        l_pas = [1]
        if curr == 0:
            p_list.append(l_pas)
            pascal(curr+1,row,p_list)
        elif curr == 1:
            l_pas.append(1)
            p_list.append(l_pas)
            pascal(curr + 1, row, p_list)
        else:
            x = p_list[-1]
            for a in range(0,len(x)-1):
                l_pas.append(p_list[-1][a] + p_list[-1][a+1])
            l_pas.append(1)
            p_list.append(l_pas)
            pascal(curr + 1, row, p_list)

p_list = []
pascal(0,6,p_list)






