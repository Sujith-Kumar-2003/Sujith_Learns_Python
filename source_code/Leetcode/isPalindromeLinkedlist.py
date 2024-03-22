class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def is_palindrome_recursive(right):
            nonlocal left
            if not right:
                return True

            if not is_palindrome_recursive(right.next):
                return False

            if left.val != right.val:
                return False
            left = left.next
            return True

        left = head
        return is_palindrome_recursive(head)
