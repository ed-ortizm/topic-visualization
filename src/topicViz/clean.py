"""
Functionality for cleaning text data from posts, tweets, etc.
Includes cleaning of punctuation, stopwords, html...
"""

import re
from bs4 import BeautifulSoup


class TextProcessor:
    """
    A class for processing text data by removing punctuation,
    and converting to lowercase.

    Methods:
        replace_newlines(text: str) -> str:

        to_lowercase(text: str) -> str:

        replace_dash_quotes(
            text: str,
            dash_for: str = ' ',
            quote_for: str = ' ',
            quotes_for: str = ' '
        ) -> str:

        replace_marks(
            text: str,
            question_mark_for: str = ' ',
            exclamation_for: str = ' ',
            parenthesis_for: str = ' ',
        ) -> str:

        replace_punctuation(
            text: str,
            dot_for: str = ' ',
            comma_for: str = ' ',
            semicolon_for: str = ' ',
            colon_for: str = ' '
        ) -> str:
    """
    @staticmethod
    def replace_newlines(text: str) -> str:
        """
        Replaces new line characters with a space and replaces
        more than one space with a single space using regex.
        """

        return re.sub(r'\s+', ' ', text.replace('\n', ' '))

    @staticmethod
    def to_lowercase(text: str) -> str:
        """
        Converts all uppercase characters in the text to lowercase.
        """
        return text.lower()

    @staticmethod
    def replace_dash_quotes(
        text: str,
        dash_for: str = ' ',
        quote_for: str = ' ',
        quotes_for: str = ' '
    ) -> str:
        """
        Replaces all occurrences of -,' and " characters with
        empty strings and replaces all colons with spaces.
        """

        replacements = {
            ord('-'): dash_for,
            ord('\''): quote_for,
            ord('\"'): quotes_for,
        }

        return text.translate(replacements)

    @staticmethod
    def replace_marks(
        text: str,
        question_mark_for: str = ' ',
        exclamation_for: str = ' ',
        parenthesis_for: str = ' ',
    ) -> str:
        """
        Replaces all occurrences of (,),.,,,?,and ! with spaces.
        """
        replacements = {
            ord('?'): question_mark_for,
            ord('!'): exclamation_for,
            ord('('): parenthesis_for,
            ord(')'): parenthesis_for,
        }

        return text.translate(replacements)

    @staticmethod
    def replace_punctuation(
        text: str,
        dot_for: str = ' ',
        comma_for: str = ' ',
        semicolon_for: str = ' ',
        colon_for: str = ' '
    ) -> str:
        """
        Replaces commas, semicolons, and colons with specified 
        characters.
        """
        replacements = {
            ord(','): comma_for,
            ord(';'): semicolon_for,
            ord(':'): colon_for,
            ord('.'): dot_for,
        }

        return text.translate(replacements)


class HTMLCleaner:
    """
    A class for cleaning HTML formatted text by removing pre-formatted
    text, code blocks, and hyperlinks.

    Methods:
        remove_preformatted_text(text: str) -> str:
            Removes pre-formatted text from HTML formatted text.

        remove_code_blocks(text: str) -> str:
            Removes code blocks from HTML formatted text.

        remove_hyperlinks(text: str) -> str:
            Removes hyperlinks from HTML formatted text.

        clean_html(text: str) -> str:
            Removes pre-formatted text, code blocks, hyperlinks,
            and any other HTML tags from HTML formatted text.
    """
    def __init__(self):
        pass

    @staticmethod
    def remove_preformatted_text(html_text: str) -> str:
        """
        Removes <pre> and </pre> tags and any content between them
        from the input text. This is useful for removing preformatted
        blocks of code from text data.

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

        processed_html = pattern.sub('', html_text)

        return processed_html

    @staticmethod
    def remove_code_blocks(html_text: str) -> str:
        """
        Removes computer code blocks from a string of HTML text.
        The function searches for code blocks by looking
        for the HTML tag <code> and returns the
        remaining text without these code blocks.

        INPUT
            html_text: The HTML text to be processed.

        OUTPUT
            processed_text: The processed text with code blocks removed.
        """

        pattern = re.compile(r'<code>.*?</code>', re.DOTALL)
        processed_html = pattern.sub('', html_text)

        return processed_html

    @staticmethod
    def remove_hyperlinks(html_text: str) -> str:
        """
        Removes hyperlinks from a string of HTML text.

        INPUTS:
        text: the HTML text to remove hyperlinks from

        OUTPUTS:
        no_hlinks: the processed text with hyperlinks removed
        """

        pattern = re.compile(r'<a.*?</a>')
        processed_html = pattern.sub('', html_text)

        return processed_html

    @staticmethod
    def clean_html(html_text: str) -> str:
        """
        Removes all HTML tags from the input text, leaving only plain text.

        INPUTS:
        html_text: A string of text in HTML format.

        OUTPUT:
        clean_text: The input text with all HTML tags removed.
        """

        soup = BeautifulSoup(html_text, 'html.parser')

        clean_text = soup.get_text()

        return clean_text
