public class Solution {
    public String compressedString(String word) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        int count = 0;

        // Loop through the string
        while (i < word.length() - 1) {
            if (word.charAt(i) == word.charAt(i + 1)) {
                count++;
                i++;
                if (count == 9) {
                    result.append(9).append(word.charAt(i));
                    count = 0;
                }
            } else {
                result.append(count + 1).append(word.charAt(i));
                i++;
                count = 0;
            }
        }
        
        // Append the last character and its count
        result.append(count + 1).append(word.charAt(i));

        return result.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String compressed = solution.compressedString("aaabbbccaa");
        System.out.println(compressed);  // Output: "3a3b2c2a"
    }
}
