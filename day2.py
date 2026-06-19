def is_safe(report: list[int]) -> bool:
    diff = [b - a for a, b in zip(report, report[1:])]
    if all(d < 0 for d in diff):
        return all(-3 <= d <= -1 for d in diff)
    if all(d > 0 for d in diff):
        return all(1 <= d <= 3 for d in diff)
    return False


def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe(report):
        return True
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))


def load_reports(path: str) -> list[list[int]]:
    with open(path) as file:
        return [[int(x) for x in line.split()] for line in file]


def count_safe_reports(reports: list[list[int]]) -> int:
    return sum(is_safe_with_dampener(report) for report in reports)


def solve(path: str = "input.txt") -> int:
    return count_safe_reports(load_reports(path))


if __name__ == "__main__":
    print(solve())
