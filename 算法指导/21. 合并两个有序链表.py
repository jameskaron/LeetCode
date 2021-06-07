# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]

#定义节点
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
#将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵节点
        prehead = ListNode(-1)

        # 头指针指向哨兵节点
        prev = prehead

        while l1 and l2:
            # 判断l1 l2大小, 小的被连接
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

            # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
            prev.next = l1 if l1 is not None else l2
            return prehead.next


if __name__ == '__main__':
    head1 = create_linked_list([1, 2, 4])
    head2 = create_linked_list([1, 3, 4])
    solution = Solution()
    sorted_lists = solution.mergeTwoLists(head1, head2)
    print(print_linked_list(sorted_lists))
