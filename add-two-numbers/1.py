# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1. 결과를 어디에 저장할 것인가?
1-1. 둘 중 긴 리스트에 저장한다 -> 둘중에 누가 긴지 알려면 O(n) 시간 소요 (그래도 전체적인 복잡도에는 영향이 없을 것 같음), 올림으로 인해 결과값의 자릿수가 늘어날 경우 노드를 더해야하는 불편함
1-2(v). 새 리스트를 만든다 -> 로직상으로는 간단해 보이기는한데 공간이 조금 아깝 -> 한쪽이 더 짧아서 >끝나버리면 남은 한쪽만 계속 더하는거니까 둘중에 누가 더 긴지 알 필요도 없을 것이고..
2. 루프의 정지 조건

'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l3_prev = None
        l3_head = l3 
        while l1 != None or l2 != None:
            if (l1 != None):
                l3.val += l1.val

            if (l2 != None):
                l3.val += l2.val

            if ((l1 != None and l1.next != None) or (l2 != None and l2.next != None)) or l3.val >= 10:
                l3.next = ListNode()
                if l3.val >= 10:
                    l3.val -= 10
                    l3.next.val += 1

                l3_prev = l3
                l3 = l3.next

            if l1 != None:
                l1 = l1.next

            if l2 != None:
                l2 = l2.next

        return l3_head 
