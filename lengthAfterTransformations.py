class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Initialize count of each letter
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        # Step 2: Perform t transformations
        for _ in range(t):
            new_count = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    # 'z' -> 'a' + 'b'
                    new_count[0] = (new_count[0] + count[25]) % MOD
                    new_count[1] = (new_count[1] + count[25]) % MOD
                else:
                    # other letters -> next letter
                    new_count[i+1] = (new_count[i+1] + count[i]) % MOD
            count = new_count
        
        # Step 3: Compute final length
        return sum(count) % MOD
