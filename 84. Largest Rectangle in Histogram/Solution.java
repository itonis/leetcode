import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<int[]> stack = new LinkedList<>();
        stack.push(new int[] {0, -1});
        int maxArea = 0;
        int n = heights.length;
        for (int i = 0; i < n; i++) {
            while (stack.peek()[0] > heights[i]) {
                int[] prev = stack.pop();
                int area = prev[0] * (i - stack.peek()[1] - 1);
                maxArea = Math.max(maxArea, area);
            }
            stack.push(new int[] {heights[i], i});
        }
        while (stack.peek()[0] > 0) {
            int[] prev = stack.pop();
            int area = prev[0] * (n - stack.peek()[1] - 1);
            maxArea = Math.max(maxArea, area);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] heights = {2, 1, 5, 6, 2, 3};
        System.out.println(solution.largestRectangleArea(heights));
    }
}
