# Learn GraphQL

by KADIRA

### 1. Introduction to GraphQL

- application layer query language
- you can define your backend as a well-defined graph-based schema, and client applications can query your dataset as they are needed

Different Client Apps --> (GraphQL Queries) --> GraphQL Server --> Data Sources --> (back to) GraphQL Server --> (JSON Payload) --> (back to) Different Client Apps

1. you do not need to change your backend for data requirement changes in client Apps (solves one of problems in managing REST API)
2. allows client applications to batch and fetch data very efficiently

```GraphQL
{
    latestPost {
        _id,
        title,
        content,
        author {
            name
        },
        comments {
            content,
            author {
                name
            }
        }
    }
}
```

a GraphQL query to fetch data for a blog post with comments and author information. Below is the result of the above query

```GraphQL
{
    "data": {
        "latestPost": {
            "_id": "03390abb5570ce03ae524397d215713b",
            "title": "New Feature: Tracking Error Status with Kadira",
            "content": "Here is a common feedback we received from our users ...",
            "author": {
                "name": "Pahan Sarathchandra"
            },
            "comments": [
            {
                "content": "This is a very good blog post",
                "author": {
                "name": "Arunoda Susiripala"
                }
            },
            {
                "content": "Keep up the good work",
                "author": {
                "name": "Kasun Indi"
                }
            }
            ]
        }
    }
}
```

> GraphQL is a specification

- it can be used with any platform and any language
- it has a reference implementation on JS

### 2. Let's Learn GraphQL

Pre-knowledge: JavaScript, NodeJS, Git

GraphQL Sandbox: [GraphiQL](https://sandbox.learngraphql.com)

### 3. Querying GraphQL

GraphQL query language is a major part of GraphQL; learn about how to query against a GraphQLserver, become familiar with the query syntax

do not worry about how the GraphQL server works and how the schema is implemented; just focus on the query syntax and play with item_width

##### Hello GraphQL

to retrieve the title and summary of the latest post in the blog

```GraphQL
{
    latestPost {
        title,
        summary
    }
}
```

ask the server to send the field `latestPost` of the root of the graph (root query fields), and request the `title` and `summary` of the result object

##### Nested querying

we can query in nested fashion. retrieve all the posts and their comments

```GraphQL
{
    posts {
        title,
        summary,
        comments {
            content
        }
    }
}
```

in this way, we can nest fields and go deeper into our graph as needed

```GraphQL
{
    posts {
        title,
        author {
            name
        }
        summary,
        comments {
            content
        }
    }
}
```

##### Arguments

can filter the output by specifying any set of fields; need a way to select a subset of data rather than retrieving the whole dataset for a particular type (with arguments)

```graphql
{
    recentPosts(count:5) {
        title
    }
}
```
retrieve five recent posts from the blog. `count` is a defined argument for the `recentPosts` root query field

##### Multiple fields

can write as many root query fields as we need in a single GraphQL query. in the server, all these fields will be processed in parallel and will give you the result as a whole

```GraphQL
{
    latestPost{
        title
    },
    authors{
        name
    }
}
```

get both authors and the latest post at once

##### Assigning a result to a variable

use the same root query field multiple times in a single query

```GraphQL
{
    latestPost: latestPost{
        title
    },
    authorNames: authors{
        name
    },
    authorIds: authors{
        _id
    }
}
```

### 4. Invoking Mutations

### 5. Fragments

### 6. Query Variables

### 7. Defining Queries

### 8. Defining Mutations

### 9. Executing GraphQL Queries

### 10. Using A Real Data Source

### 11. More on GraphQL
