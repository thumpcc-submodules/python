# Snippets

## Nested dict comprehension

``````python
{tk: {v: k for k, v in tv.items()} for tk, tv in t.items()}
``````
