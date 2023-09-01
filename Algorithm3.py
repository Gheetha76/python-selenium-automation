

# def find_missing_element(arr1:list, arr2:list):
#     arr1.sort()
#     arr2.sort()
#     print(arr1)
#     print(arr2)
#
#
#     for i in range(len(arr2) -1):
#         if arr1[i] != arr2[i]:
#             print(str(arr1[i]) + " is the missing element")
#             return
#     print(str(arr1[-1]) + " is the missing element")
#
# testlist1 = [1, 4, 6, 8, 9, 2]
# testlist2 = [3, 2, 1, 4, 6, 8, 9]
# find_missing_element(testlist1, testlist2)

def is_mountain_array(arr: list):
    i = 1
    
