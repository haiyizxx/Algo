package problem;

import java.util.ArrayList;

public class LC392_IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j))
                i++;
            j++;
        }
        return i == s.length();
    }

    public boolean isSubsequenceBinarySearch(String s, String t) {
        int m = s.length(), n = t.length();

        ArrayList<Integer>[] idx = new ArrayList[256];

        for (int i = 0; i < n; i++) {
            char c = t.charAt(i);
            if (idx[c] == null)
                idx[c] = new ArrayList<>();
            idx[c].add(i);
        }

        int j = 0;
        for (int i = 0; i < m; i++) {
            char c = s.charAt(i);
            if (idx[c] == null)
                return false;
            int pos = left_bound(idx[c], j);
            if (pos == idx[c].size())
                return false;
            j = idx[c].get(pos) + 1;
        }
        return true;
    }

    // Left bound binary search
    // [0,1,3,4] target = 2 return 2(index)
    private int left_bound(ArrayList<Integer> arr, int tar) {
        int lo = 0, hi = arr.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (tar > arr.get(mid))
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
}