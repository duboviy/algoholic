# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val


class Solution(object):
    def oddEvenList3(self, head):
        if not head or not head.next:
            return head
        odd, even, h, tail = head, head.next, head.next, None
        while odd and even:
            odd.next = even.next
            tail = odd
            odd = odd.next
            even.next = odd.next if odd else None
            even = even.next
        tail = odd if odd else tail
        tail.next = h
        return head

    def oddEvenList2(self, head):
        headOdd = dummyOdd = ListNode(-1)
        headEven = dummyEven = ListNode(-1)
        count = 1
        while head:
            if count % 2 == 0:
                dummyEven.next = head
                dummyEven = dummyEven.next
            else:
                dummyOdd.next = head
                dummyOdd = dummyOdd.next
            head = head.next
            count += 1
        dummyEven.next = None
        dummyOdd.next = headEven.next
        return headOdd.next

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        swap_flag = False
        swap_target = head
        prev_item, item = head, head.next
        while item:
            if swap_flag:
                # Move current item to swap_target
                temp_item = swap_target.next
                swap_target.next = item
                prev_item.next = item.next
                item.next = temp_item
                swap_target = item

                item = prev_item.next
            else:
                item, prev_item = item.next, prev_item.next

            swap_flag = not swap_flag

        return head

# def check(solver, cases):
#     """Performs simple solver check using test cases list
#     The main logic is like:
#         result = solver(*case.get('args', []), **case.get('kwargs', {})) == case['result']
#     :param solver: task solver callable object
#     :param cases: iterable object with test cases in dict format.
#     Dict keys: args (optional), kwargs (optional), result (mandatory)
#     """
#     for i, case in enumerate(cases, 1):
#         result = solver(*case.get('args', []), **case.get('kwargs', {})) == case['result']
#         print "Test {0}: {1}".format(i, "OK" if result else "FAILED")

if __name__ == '__main__':
    # import checker
    # a = [ListNode(i) for i in xrange(2)]
    # b = [ListNode(i) for i in xrange(3)]
    # c = [ListNode(i) for i in xrange(3)]
    # headA, headB = a[0], b[0]
    # a[0].next = a[1]
    # a[1].next = c[0]
    # c[0].next = c[1]
    # c[1].next = c[2]
    # b[0].next = b[1]
    # b[1].next = b[2]
    # b[2].next = c[0]
    # cases = (
    #     {'args': (headA, headB), 'result': c[0]},
    #     {'args': (ListNode(0), ListNode(1)), 'result': None},
    # )
    # checker.check(Solution().getIntersectionNode, cases)

    a = [ListNode(i) for i in xrange(8)]
    print [i.val for i in a]
    headA = a[0]
    a[0].next = a[1]
    a[1].next = a[2]
    a[2].next = a[3]
    a[3].next = a[4]
    a[4].next = a[5]
    a[5].next = a[6]
    a[6].next = a[7]
    print Solution().oddEvenList(headA)

    head = headA
    while head:
        print head.val
        head = head.next
