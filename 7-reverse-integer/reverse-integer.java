class Solution {
    public int reverse(int x) {
        int sum = 0;
        
        while (x != 0) {
            int rem = x % 10;          // extract last digit
            x = x / 10;                // reduce number
            
            // check for overflow before multiplying
            if (sum > Integer.MAX_VALUE / 10 || sum < Integer.MIN_VALUE / 10) {
                return 0;
            }
            
            sum = sum * 10 + rem;      // build reversed number
        }
        
        return sum;
    }
}
