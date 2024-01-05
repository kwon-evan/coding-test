impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let (mut i, mut j) = (0, 0);
        while i < s.len() && j < t.len() {
            if s.chars().nth(i).unwrap() == t.chars().nth(j).unwrap() {
                i += 1;
            }
            j += 1;
        }
        i == s.len()
    }
}
