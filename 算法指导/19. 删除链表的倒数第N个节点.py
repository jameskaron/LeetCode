# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

# 哨兵节点，其实就是一个附加在原链表最前面用来简化边界条件的附加节点，它的值域不存储任何东西，只是为了操作方便而引入。
# 用于头节点被删除的情况
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/dong-hua-tu-jie-leetcode-di-19-hao-wen-ti-shan-chu/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 插入哨兵节点
        dummy = ListNode(0, head)
        # 快慢指针
        first = head
        second = dummy
        # 快指针向前移动n位
        for i in range(n):
            first = first.next
        # 移动快慢指针直到快指针到达null
        while first:
            first = first.next
            second = second.next
        # 删掉目标指针
        second.next = second.next.next
        # 返回链表的头节点
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    # for i in range(5):
    #     node_1 = ListNode(i + 1)
    #     if i + 2 <= 5:
    #         node_2 = ListNode(i + 2)
    #         node_1.next = node_2
    #     else:
    #         node_1.next = None
    for i in range(4):
        node = ListNode(i, ListNode(i+1))

    # assert s.removeNthFromEnd(node, n=2) == [1, 2, 3, 5]
