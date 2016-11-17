# Function Score Query

allow to modify the score of documents that are retrieved by a query

to use `function_score`, one needs to define a query and at least 1 functions (compute a new score for each document returned)

`function_score` can be used with only 1 function `{"query": {"function_score": {...}}}`

several functions can be combined `{"query": {"function_score": {"functions": [{...}, {...}], ... }}}`
