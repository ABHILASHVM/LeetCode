class Solution {
    public boolean rotateString(String s, String goal) {
    
        int len = s.length();
        for (int i = 0; i < len; i++) {
            String rotated = s.substring(i) + s.substring(0, i);
            if (rotated.equals(goal)) {
                return true;
            }
        }
        return false;
}

    }
