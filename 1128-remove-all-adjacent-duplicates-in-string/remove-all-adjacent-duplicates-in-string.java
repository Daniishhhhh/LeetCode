class Solution {
    public String removeDuplicates(String s) {
        StringBuilder sb = new StringBuilder();   // acts like a stack
        for (char c : s.toCharArray()) {          // iterate through each character
            int len = sb.length();                // current stack size
            if (len > 0 && sb.charAt(len - 1) == c){
                sb.deleteCharAt(len - 1);         // pop if duplicate
            }else{
                sb.append(c);                     // push otherwise
            }
        }
        return sb.toString();                     // final reduced string
    }
}
