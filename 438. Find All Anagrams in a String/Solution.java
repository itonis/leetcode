import java.util.ArrayList;
import java.util.List;

public class Solution {

    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> results = new ArrayList<>();
        int[] counts = new int[26];
        boolean[] exists = new boolean[26];
        int n = p.length();
        for (char c: p.toCharArray()) {
            counts[c - 'a']++;
            exists[c - 'a'] = true;
        }
        int l = 0;
        int m = s.length();
        int[] copy = new int[26];
        int limit = m - n;
        outer:
        while (l <= limit) {
            int r = l;
            System.arraycopy(counts, 0, copy, 0, 26);
            while (r < m) {
                int idx = charIdx(s, r);
                if (!exists[idx]) {
                    l = r + 1;
                    continue outer;
                }
                while (copy[idx] == 0) {
                    copy[charIdx(s, l)]++;
                    l++;
                }
                copy[idx]--;
                r++;
                if (r - l == n) {
                    results.add(l);
                }
            }
            if (r == m) {
                break;
            }
        }
        return results;
    }

    private int charIdx(String s, int pos) {
        return (int) s.charAt(pos) - 'a';
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findAnagrams("cbaebabacd", "abc"));
    }
}
