# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val


class Solution(object):
    def getIntersectionNode2(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa

# only 2 ways to get out of the loop, they meet or the both hit the end=None
# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of th

    @staticmethod
    def getListLength(head):
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        lenA, lenB = self.getListLength(headA), self.getListLength(headB)
        if lenA > lenB:
            for i in xrange(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for i in xrange(lenB - lenA):
                headB = headB.next

        while headA is not headB:
            headA, headB = headA.next, headB.next

        return headA


def check(solver, cases):
    """Performs simple solver check using test cases list
    The main logic is like:
        result = solver(*case.get('args', []), **case.get('kwargs', {})) == case['result']
    :param solver: task solver callable object
    :param cases: iterable object with test cases in dict format.
    Dict keys: args (optional), kwargs (optional), result (mandatory)
    """
    for i, case in enumerate(cases, 1):
        result = solver(*case.get('args', []), **case.get('kwargs', {})) == case['result']
        print "Test {0}: {1}".format(i, "OK" if result else "FAILED")

if __name__ == '__main__':
    a = [ListNode(i) for i in xrange(2)]
    b = [ListNode(i) for i in xrange(3)]
    c = [ListNode(i) for i in xrange(3)]
    headA, headB = a[0], b[0]
    a[0].next = a[1]
    a[1].next = c[0]
    c[0].next = c[1]
    c[1].next = c[2]
    b[0].next = b[1]
    b[1].next = b[2]
    b[2].next = c[0]
    cases = (
        {'args': (headA, headB), 'result': c[0]},
        {'args': (ListNode(0), ListNode(1)), 'result': None},
    )
    check(Solution().getIntersectionNode, cases)

    # a = [ListNode(i) for i in xrange(8)]
    # print [i.val for i in a]
    # headA = a[0]
    # a[0].next = a[1]
    # a[1].next = a[2]
    # a[2].next = a[3]
    # a[3].next = a[4]
    # a[4].next = a[5]
    # a[5].next = a[6]
    # a[6].next = a[7]
    # print Solution().oddEvenList(headA)
    #
    # head = headA
    # while head:
    #     print head.val
    #     head = head.next
