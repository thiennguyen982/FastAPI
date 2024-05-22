def find_min(input_list : list[int]) -> (int, int):
    min_val = input_list[0]
    index = 0
    for i in range(1, len(input_list)):
        if min_val > input_list[i]:
            min_val = input_list[i]
            index = i
    return (min_val, index)

def merged_sorted_list(input_list : list[list[int]]) -> list[int]:
    result = []
    while (len(input_list) > 1):
        first_queue = []
        for i in range(0, len(input_list)):
            first_queue.append(input_list[i][0])
        temp_res = find_min(first_queue)
        result.append(temp_res[0])
        input_list[temp_res[1]] = input_list[temp_res[1]][1:]
        if (len(input_list[temp_res[1]]) == 0):
            input_list = [sub_list for sub_list in input_list if sub_list]
    if input_list:
        result.extend(input_list[0])
    return result

#For ListNode
# class Solution:
#     def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         current = dummy
        
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
        
#         current.next = list1 if list1 else list2
        
#         return dummy.next


if __name__ == "__main__":
    L1 = [1, 2, 3, 4, 5]
    L2 = [6, 7, 8, 9, 10]
    L3 = [11, 13, 15, 17, 19]
    L4 = [21, 23, 25, 27, 29]
    L5 = [31, 33, 35, 37, 39]
    L6 = [1, 2, 3, 4, 51, 63, 75, 87]
    print(merged_sorted_list([L1, L3, L5, L2, L4, L6]))