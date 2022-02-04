public class Solution {
    public int findMaxLength(int[] nums) {
        int n = nums.length;
        int[] posDiff = new int[n + 1];
        int[] negDiff = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            posDiff[i] = -1;
            negDiff[i] = -1;
        }
        int max = 0;
        int diff = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                diff++;
            } else {
                diff--;
            }
            if (diff == 0) {
                max = i + 1;
            } else if (diff > 0) {
                if (posDiff[diff] < 0) {
                    posDiff[diff] = i;
                } else {
                    int length = i - posDiff[diff];
                max = Math.max(length, max);
                }
            } else {
                if (negDiff[-diff] < 0) {
                    negDiff[-diff] = i;
                } else {
                    int length = i - negDiff[-diff];
                max = Math.max(length, max);
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findMaxLength(new int[] {0, 1}));
    }
}
