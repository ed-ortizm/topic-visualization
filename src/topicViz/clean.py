"""
Functionality for cleaning text data from posts, tweets, etc.
Includes cleaning of punctuation, stopwords, html...
"""

import re


def remove_pre_tags(text: str) -> str:
    """
    Removes <pre> and </pre> tags and any content between them
    from the input text.

    INPUTS:
        text: The text containing the <pre> and </pre> tags to remove.

    OUTPUTS:
        no_pre_text: The text with the <pre> and </pre> tags and
        their content removed.
    """
    # .*? (lazy match)
    # match any character (.) zero or more times (*),
    # but as few times as possible (?) to still allow
    # the whole pattern to match.
    # This is to avoid matching multiple <pre>...</pre> blocks
    # in the same text.
    # The flag re.DOTAL matches any character, including newline.

    pattern = re.compile(pattern=r'<pre>.*?</pre>', flags=re.DOTALL)

    no_pre_text = pattern.sub('', text)

    return no_pre_text
