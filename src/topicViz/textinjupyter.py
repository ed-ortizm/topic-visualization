"""
Funtionality to display the text of a post in a Jupyter notebook.
"""

from IPython.display import display, Markdown


def markdown_scape_chars(
    text: str,
) -> None:
    """
    Displays the text of a post in a Jupyter notebook
    as a Markdown cell while preserving the original
    formatting of the text.
    """
    # repr returns a string representation of the object
    # that includes the escape sequences as literals.

    formatted_text = f"```\n{repr(text)}\n```"

    display(Markdown(formatted_text))
