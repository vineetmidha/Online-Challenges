// https://leetcode.com/problems/rotate-string/

class Solution {
public:
    bool rotateString(string A, string B) {
        if (A.length() != B.length())
            return false;
        
        string big = A + A;
        
        return !(big.find(B) == string::npos);
    }
};

/*

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

*/
