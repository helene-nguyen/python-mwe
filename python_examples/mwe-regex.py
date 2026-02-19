import re

test_urls = [
    "https://t.me/username/",
    "https://twitter.com/someuser/",
    "https://t.me/anotheruser/extra",
    "https://twitter.com/anotheruser/extra"
]

pattern_raw = r"(https:\/\/t.me\/.+?(?=\/))|(https:\/\/twitter.com\/.+?(?=\/))"
pattern_normal = "(https:\/\/t.me\/.+?(?=\/))|(https:\/\/twitter.com\/.+?(?=\/))"

# print("Testing with RAW string pattern:")
# for url in test_urls:
#     match = re.search(pattern_raw, url)
#     print(f"URL: {url} | Match: {match.group() if match else None}")
#
# print("\nTesting with NORMAL string pattern:")
# for url in test_urls:
#     match = re.search(pattern_normal, url)
#     print(f"URL: {url} | Match: {match.group() if match else None}")

# Adding the r prefix is the correct way to write this regex in Python.
# It ensures the pattern is interpreted correctly.
# Without it, you risk Python misinterpreting your backslashes, which can lead to bugs or unexpected behavior.
