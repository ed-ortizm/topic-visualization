"""
Functionality to perform common NLP tasks on text data such as
tokenization and stopword removal.
"""
import nltk
import numpy as np
from sklearn.decomposition import PCA


def perform_pca(
    data: np.array,
    num_components=None,
    explained_variance_ratio=None
) -> tuple[np.array, PCA]:
    """
    Performs PCA on the data and returns the reduced representation
    of the data.

    INPUTS:
    data: The data to perform PCA on.
    num_components: The number of components to keep.
    explained_variance_ratio: The minimum amount of variance to keep.

    OUTPUTS:
    reduced_data: The reduced representation of the data.
    """

    pca = PCA()
    transformed_data = pca.fit_transform(data)

    cumulative_variance_ratio = np.cumsum(
        pca.explained_variance_ratio_
    )

    if num_components is None and explained_variance_ratio is not None:

        num_components = np.argmax(
            cumulative_variance_ratio >= explained_variance_ratio
        ) + 1

    reduced_data = transformed_data[:, :num_components]

    return reduced_data, pca


class NLPProcessor:

    """
    A class for performing common NLP tasks on text data such as
    tokenization and stopword removal.

    Methods:
    """

    @staticmethod
    def tokenize(text: str) -> list:
        """
        Tokenizes the text using the nltk library.
        """

        tokenized_text = nltk.word_tokenize(text)

        return tokenized_text

    @staticmethod
    def remove_stopwords(
        tokenized_text: list,
        stopwords: list
    ) -> list:
        """
        Removes stopwords from the tokenized text.

        INPUTS:
        tokenized_text: A list of tokens.
        stopwords: A list of stopwords to remove from the tokenized text.

        OUTPUT:
        tokens_without_stopwords: A list of tokens without stopwords.
        """

        tokens_without_stopwords = [
            token for token in tokenized_text
            if token not in stopwords
        ]

        return tokens_without_stopwords

    @staticmethod
    def vectorize(
        tokenized_text: list,
        vectorizer
    ) -> np.array:
        """
        Vectorizes the tokenized text.
        vectorizer is an NLP model that implements the
        get_mean_vector method.

        INPUTS:
        tokenized_text: A list of tokens.
        vectorizer: An NLP model that implements the
        get_mean_vector method.

        OUTPUT:
        vectorized_text: A vectorized version of the input text.

        """

        vectorized_text = vectorizer.get_mean_vector(
            tokenized_text
        )

        return vectorized_text
