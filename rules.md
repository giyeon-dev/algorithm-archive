# Rules for Algorithm Archive Challenge

## 1) Weekly target
- Each participant solves **3+ problems per week** (Mon–Sun, KST ISO week).

## 2) Submissions = One PR per week
- Batch all problems for the week into **one PR per person**.
- You can push multiple times to the same PR during the week.
- We use **auto-merge or approvals=0** to avoid friction. Peer comments are encouraged but not required.

## 3) Directory structure
solutions/<username>/<YYYY-Www>/<platform>/<problem-id(-slug).ext>

**Example**
solutions/giyeon/2025-W35/leetcode/0001-two-sum.java

Allowed platforms: `leetcode`, `baekjoon`, `programmers` (extend freely).

## 4) Solution header (optional but recommended)
// Problem: <URL>
// Approach: <1–2 lines>
// Complexity: O(... time), O(... space)

## 5) Reviews
- Leave at least one **short comment** per week in your partner's weekly PR or in the retrospective issue (tips, edge cases, refactor suggestions).
- Formal “approval” is optional in this mode.

## 6) Scoreboard
- After a weekly PR is merged into `main`, a GitHub Action updates the scoreboard block in `README.md` for the current KST week.

## 7) Weekly retrospective (auto)
- Every Monday 00:05 KST, an issue named `Weekly Retrospective: YYYY-Www` is auto-created.
- Leave a short note: what I learned, mistakes, next week’s plan.