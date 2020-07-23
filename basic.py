
#a = [  1, 0, 1, 1, 0, 1, 0, 1]
#def ind(lst):
    #position = 0
    #for elements in lst:
        #index_of_list = list(range(0,len(lst)))

        #return index_of_list
#print(ind([ 1, 0, 1, 0, 1, 1, 1, 1, 0,1,3,4,5,6,7,8]))

def subsequence(num1,num2):
    for elements1,elements2 in zip(num1,num2):
        if num1 != num2:
            sum = num1 *num2
            return sum


print(subsequence([2,3,0],[1,4,0]))



