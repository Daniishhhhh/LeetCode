class Solution {
    public int secondHighest(String s) {
        int largest = -1;
        int secondLargest = -1;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                int num = ch - '0';
                if (num > largest) {
                    secondLargest = largest;
                    largest = num;
                } else if (num > secondLargest && num < largest) {
                    secondLargest = num;
                }
            }
        }
        return secondLargest;
    }
}
