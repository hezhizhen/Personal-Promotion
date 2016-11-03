# Docs

## Quick Start

### Installation

[Hello World Example Code](http://codepen.io/gaearon/pen/rrpgNB?editors=0010)

### Hello World

```React
ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);
```

React is a JavaScript library; use ES6 syntax

### Introducing JSX

tag syntax: `const element=<h1>Hello, world!</h1>;` (JSX)

you can embed any JS expression in JSX by wrapping it in curly braces

can use quotes to specify string literals as attributes; can also use curly braces to embed a JS expression in an attribute

### Rendering Elements

### Components and Props

- components let you split the UI into independent, reusable places, and think about each piece in isolation (components are like JS functions)
- they accept arbitrary inputs(called "props") and return React elements describing what should appear on the screen

- the simplest way to define a component is to write a JS function `function Welcome(props) { return ... ; }`
- use an ES6 class to define a component `class Welcome extends React.Component { render() { return ... ; } }`



### State and Lifecycle

### Handling Events

### Conditional Rendering

### Lists and Keys

### Forms

### Lifting State Up

### Composition vs Inheritance

### Thinking In React

## Advanced Guides

## Reference
