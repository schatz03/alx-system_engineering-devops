#!/usr/bin/python3
"""
    Query the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
"""

import requests


def convert_lower(w, i, len_w):
    """Convert strings to lowercase"""
    if i >= len_w:
        return None

    w[i] = w[i].lower()
    convert_lower(w, i + 1, len_w)

    return None


def count_word_title(title, i, len_t, dict_words_unique):
    """Store repeating string in hash table"""
    if i >= len_t:
        return None

    if title[i] in dict_words_unique:
        dict_words_unique[title[i]] += 1

    count_word_title(title, i + 1, len_t, dict_words_unique)

    return None


def store_title_word_hash(list_title, i, len_l, dict_words_unique):
    """Run trough a list of hot titles"""
    if i >= len_l:
        return None

    title = list_title[i]["data"]["title"].lower().split(" ")

    count_word_title(title, 0, len(title), dict_words_unique)

    store_title_word_hash(list_title, i + 1, len_l, dict_words_unique)

