// https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440/


class Solution {
    
    public void reverseString(char[] s) {
        if (s.length > 1)  
            helper(s, 0, s.length-1);
    }
    
    static void helper(char[] s, int left, int right){
        if (left >= right)
            return;
        
        char t = s[left];
        s[left] = s[right];
        s[right] = t;
        
        helper(s, left+1, right-1);
    }
}
