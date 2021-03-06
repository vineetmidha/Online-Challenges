class Solution {
	static Boolean isVowel (char ch) {
		String s = "aeiouAEIOU";
		
		for (char c: s.toCharArray()) {
			if (c == ch) return true;
		}
		
		return false;
	}
	
    public static String reverseVowels(String s) {
       	char[] charArray = s.toCharArray();
        
    	int left = 0;
    	int right = s.length() - 1;
    	
    	while (left < right) {
    		
    		// First loop from left side of string 
    		// till we find a vowel
    		
    		while (left < right && !isVowel(charArray[left]))
				left++;

    		// Second loop from right side of string 
    		// till we find a vowel
    		
    		while (left < right && !isVowel(charArray[right]))
				right--;
			
			// swap
			
    		char t = charArray[left];
    		charArray[left] = charArray[right];
    		charArray[right] = t;
							
    		left++;
    		right--;    		
    	}

    	return String.valueOf(charArray);
    }
}
