import re

DATETIME_ISO8601 = re.compile(
    r"^([0-9]{4})"
    r"-"
    r"([0-9]{1,2})"
    r"-"
    r"([0-9]{1,2})"  # date
    r"([T\s][0-9]{1,2}:[0-9]{1,2}:?[0-9]{1,2}(\.[0-9]{1,6})?)?"  # time
    r"((\+[0-9]{2}:[0-9]{2})| UTC| utc)?"  # zone
)


def datetime_iso(string):
    """verify rule
    Mandatory is: 'yyyy-(m)m-(d)dT(h)h:(m)m'
    """
    string = string.strip()
    return not bool(re.fullmatch(DATETIME_ISO8601, string))


def truncate(f, n):
    """Truncates/pads a float f to n decimal places without rounding"""
    s = "{}".format(f)
    if "e" in s or "E" in s:
        return "{0:.{1}f}".format(f, n)
    i, p, d = s.partition(".")
    return ".".join([i, (d + "0" * n)[:n]])
