import os, re, datetime, subprocess
from collections import defaultdict

# ====== Config ======
USERS = ["giyeon", "jieun"]                # 실제 폴더/사용자명과 맞추기
ALLOWED_PLATFORMS = {"leetcode", "baekjoon", "programmers"}
WEEKLY_GOAL = 3
# ====================

ROOT = os.path.dirname(os.path.dirname(__file__))
SOL_DIR = os.path.join(ROOT, "solutions")
README = os.path.join(ROOT, "README.md")

def kst_now():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=9)

def kst_iso_week_folder():
    y, w, _ = kst_now().date().isocalendar()
    return f"{y}-W{w:02d}"

def count_files_for_week(week):
    counts = defaultdict(int); details = defaultdict(list)
    if not os.path.isdir(SOL_DIR): return counts, details
    for user in USERS:
        base = os.path.join(SOL_DIR, user, week)
        if not os.path.isdir(base): continue
        for platform in os.listdir(base):
            if platform not in ALLOWED_PLATFORMS: continue
            pdir = os.path.join(base, platform)
            if not os.path.isdir(pdir): continue
            for f in os.listdir(pdir):
                if f.startswith('.'):  # .keep 등 무시
                    continue
                fp = os.path.join(pdir, f)
                if os.path.isfile(fp):
                    counts[user] += 1
                    details[user].append(f"{platform}/{f}")
    return counts, details

def count_commits_for_week(week):
    counts = defaultdict(int)
    for user in USERS:
        path = f"solutions/{user}/{week}"
        try:
            out = subprocess.check_output(["git", "log", "--oneline", "--", path], cwd=ROOT).decode()
            counts[user] = len([l for l in out.splitlines() if l.strip()])
        except Exception:
            counts[user] = 0
    return counts

def render_table(week, files, details, commits):
    lines = [f"### This Week: `{week}` (Goal: {WEEKLY_GOAL}/person)", "",
             "| User | Solved | Commits | Checklist | Problems |",
             "|---|---:|---:|---|---|"]
    for u in USERS:
        solved = files.get(u, 0)
        chks = "".join("[x]" if i < min(solved, WEEKLY_GOAL) else "[ ]" for i in range(WEEKLY_GOAL))
        plist = ", ".join(sorted(details.get(u, []))) if solved else "—"
        lines.append(f"| {u} | {solved} | {commits.get(u,0)} | {chks} | {plist} |")
    return "\n".join(lines)+"\n"

def update_readme(block):
    with open(README, "r", encoding="utf-8") as f:
        src = f.read()
    pattern = r"(<!-- scoreboard:start -->)(.*?)(<!-- scoreboard:end -->)"
    repl = r"\1\n" + block + r"\n\3"
    dst = re.sub(pattern, repl, src, flags=re.S) if re.search(pattern, src, flags=re.S) else \
          src + "\n\n<!-- scoreboard:start -->\n" + block + "\n<!-- scoreboard:end -->\n"
    with open(README, "w", encoding="utf-8") as f:
        f.write(dst)

if __name__ == "__main__":
    week = kst_iso_week_folder()
    file_counts, details = count_files_for_week(week)
    commit_counts = count_commits_for_week(week)
    block = render_table(week, file_counts, details, commit_counts)
    update_readme(block)
