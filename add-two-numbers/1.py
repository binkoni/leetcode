# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1. 결과를 어디에 저장할 것인가?
1-1. 둘 중 긴 리스트에 저장한다 -> 둘중에 누가 긴지 알려면 O(n) 시간 소요 (그래도 전체적인 복잡도에는 영향이 없을 것 같음), 올림으로 인해 결과값의 자릿수가 늘어날 경우 노드를 더해야하는 불편함
1-2(선택). 새 리스트를 만든다 -> 로직상으로는 간단해 보이기는한데 공간이 조금 아깝 -> 한쪽이 더 짧아서 >끝나버리면 남은 한쪽만 계속 더하는거니까 둘중에 누가 더 긴지 알 필요도 없을 것이고..
2. 루프의 정지 조건
l1나 l2가 모두 끝나야 정지
'''
'''
# 첫번째 시도
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
'''

'''
# https://leetcode.com/problems/add-two-numbers/solutions/1835217/python3-dummy-carry-explained/?languageTags=python3
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            
            val = carry + v1 + v2
            res.next = ListNode(val%10)
            res, carry = res.next, val//10
            
        if carry:
            res.next = ListNode(carry)
        return
'''
# 세 번째 시도, 루프 정지 조건 단순화
# 두 번째 솔루션보다는 복잡하다, carry 변수를 쓰지 않아서 그런듯
# carry 를 쓰지 않으면 현재 단방향 링크드 리스트이기 때문에 prev의 값을 참조할 수 없어 다음 노드에 캐리를 더해주는 방식을 써야하는데 이것이 코드가 더 지저분해지게 만드는 원인이다
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = head = ListNode()
        while l1 or l2:
            l3.next = ListNode()
            if l1:
                l3.next.val += l1.val
                l1 = l1.next
            if l2:
                l3.next.val += l2.val
                l2 = l2.next
            if l3.val >= 10:
                l3.val -= 10
                l3.next.val += 1
            l3 = l3.next
        if l3.val >= 10:
            l3.val -= 10
            l3.next = ListNode()
            l3.next.val += 1
        return head.next
