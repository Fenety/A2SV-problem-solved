# A2SV Problem Solved

A personal workspace for practicing programming problems and saving solutions from multiple platforms (LeetCode, CodeForces, GeeksForGeeks, HackerRank, etc.). This repo is organized by platform and contains small, runnable solutions (mostly Python) used for learning and keeping a searchable record of problem solving.

## Purpose

- Practice problem-solving regularly.
- Keep solutions organized by platform and problem id.
- Record short notes (approach, complexity) alongside solutions.

## Repository layout

- `CodeForces/` — Solutions for CodeForces problems.
- `GeeksForGeeks/` — Solutions for GeeksForGeeks problems.
- `HackerRank/` — Solutions for HackerRank problems.
- `LeetCode/` — Solutions for LeetCode problems.

Each folder contains solution files, typically Python scripts. Example filenames in this repo use a convention like:

```
<index>_<short-title>(<problem-id>).py
```

Examples:
- `3_Convert-the-Temperature(2469).py`
- `13_check-if-all-the-integers-in-a-range-are-covered(1893).py`

## File naming & headers (recommended)

- Use a short, descriptive filename with an optional problem id in parentheses.
- At the top of each solution file include a small header comment with:
  - Problem title and platform
  - Problem URL
  - Brief approach and complexity (time/space)

Example header:

```
# Problem: Convert the Temperature (LeetCode)
# URL: https://leetcode.com/problems/convert-the-temperature/ (2469)
# Approach: direct formula conversion
# Complexity: O(1) time, O(1) space
```

## How to add a new solution

1. Pick the correct platform folder (or create one if missing).
2. Add a new file following the naming convention above.
3. Add a header with the problem link and a short explanation.
4. Ensure the script is runnable (if applicable) and prints or asserts expected results.

## Running a solution (Python)

From the repository root you can run any Python solution:

```bash
python3 LeetCode/3_Convert-the-Temperature(2469).py
```

or (for an absolute path):

```bash
python3 /home/fenety/Documents/my_projects/A2SV-problem-solved/LeetCode/3_Convert-the-Temperature(2469).py
```

If a solution requires input from STDIN, either provide it interactively or modify the file temporarily to include test cases.

## Suggested workflow

- Keep commits small and focused (one problem per commit).
- For longer solutions, include a small `if __name__ == "__main__":` test harness at the bottom of the file.
- Use clear commit messages like: `LeetCode: add 2469 Convert the Temperature`.

## Testing recommendations

- You can create a `tests/` folder per platform or a global `tests/` to collect small unit tests (pytest-friendly). Keep tests small and focused.

## Contributing (for personal use)

- Stick to the naming convention and header format.
- Keep code readable and include complexity notes where helpful.

## License

This is a personal practice repository. Add a license file if you plan to share it publicly (e.g., MIT).

## Contact / Notes

This repo is intended as a learning aid. If you want any additional features (templated solution files, CI for tests, or a script to run all solutions), tell me and I can add them.
