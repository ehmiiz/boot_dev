# JavaScript notes

// Reminder to move me to /boot_dev/courses/learn_javascript

## Variables

let = mutable

const = immutable


## Operators

and = &&

or = ||

not = !

```js
const isTrue = true
const isFalse = false

isTrue && isFalse // false
isTrue || isFalse // true
isTrue || !isFalse // true
```

## Comparison operators

```js
5 > 4 //true, 5 is gt 4
6 < 5 // true, 6 is lt 5
5 >= 6 // false, 5 is not gt or equal to 6

5 == '5' // true, two '=' is a loose check, does not check type
5 === '5' // false, === is a strict check, checks value and type

5 != 6// true, 5 is not 6
```



## None / Null

$null (powershell)
null (javascript also has `undefined` but should be avoided)
None (python)

## Conditional statements

uses C style syntax
elif is `else if`

Ternary operator, latin root for "3", takes 3 operands:

Should only be used if the code is very simple

- Condition followed by a questionmark
- An expression to execute if true followed by a colon :
- An expression to execute if false

```js
const bobbyAge = 17
const legalAge = 18

// is bobbyAge gt or eq to legalAge? is adult : is not adult
bobbyAge >= legalAge ? 'Bobby is an adult' : 'Bobby is not an adult'
```

## Functions

regular c style syntax

```js
myFunction (param) {
    console.log(`Hello, {param}!`)
}
```

Fat arrow functions / Arrow functions 

```js
// Syntax of a arrow function
const add = (param, param1) => {
    return param + param1
}

```

## Arrays

Arrays in js has the same syntax as in python

```js
const carBrands = ['Tesla', 'BMW', 'Volvo']
```

In JS, to .append() an array in JS, use .push()


```js
// creates empty array
let movies = []

// adds two movies movie
movies.push('the dark knight')
movies.push('the notebook')

// prints the first element of the aray
console.log(movies[0]) 
```

To concatinate arrays, use
```js
arrayOne.concat(arrayTwo)
```

const array's can be modified (add, remove, change elements)
const array's just can't be re-assigned, JS quirk



## Loops

for loop syntax
```js
// A classic for loop.
// create a item variable (i); until i is gt 200; append i and run block
for (let i = 0; i < 200; i++) {
  console.log(i)
}

```

A foreach loop can be achived with int's and array elements

Break to exit early

Use a for-each (for-of in js) loop if

- Iteration over entire array
- Need ascending loop (0, 1, 2, 3)
- Don't need access to index
- Don't need to update the array items

A for loop can be done with newer JS syntax

```js
let fruits = ['apple', 'banana', 'kiwi']

for (fruit of fruits) {
    console.log(fruit)
}

```

## Objects

Objects are similar to hashtables & dictionaries (pwsh, py)

```js
// object example
function getMovieRecord(title, stars, username) {
  const returnObject = {
    title: `${title}`,
    stars: `${stars}`,
    username: `${username}`,
    id: `${title}-${username}`,
  } 
  return returnObject
}
```

To me it seems like an js object is very similar to a PSCUstomObject

"the existing variable name is what I want the key in the object to be, so just use that"

->

```js
const name = 'Apple'
const radius = 2
const color = 'red'

const apple = {
  name,
  radius,
  color,
}

```

Nested objects works as you would imagine

const object = {
    company: wirely,
    employees: {
        ceo: {
            name: luddish,
            salary: 1,
        }
    }
}

object.company.employees.ceo // luddish

### Optional Chaining

New feature that handles accessing nested objects better

```js
// if the author or location property is missing, it returns `undentified`
// otherwise it will return .state
// if the new syntax is not used, a typeerror will occur

return review.author?.location?.state
```


- An object cannot have the same key twice!
- An object can have many nested levels, dot-sourcing the property can be done gracefully with .?

### Object Methods




```js
// using `this` gives the method access to properties outside of its scope
const user = {
    firstname: 'Emil',
    lastname: 'Larsson',
    getFullName() {
        return `$(this.firstname) $(this.lastname)`
    }
}

console.log(user.getFullName())
```

Dynamically access properties using the bracket notation


```js

const desk = {
  wood: 'maple',
  width: 100
}

console.log(desk.wood)
// prints "maple"

console.log(desk['wood'])
// also prints "maple"
// if 'wood' is in a variable, desk[wood]
```

###  Arrow Functions & `this`

Arrow functions perserve the `this` keyword

```js
// this does not work
const obj = {
    name: 'Emil',
    lastname: 'Larsson',
    fullName: () => { // fatarrow function using .this = null
        return `${this.firstname} ${this.lastname}`
    }
}

// use regular function
const user = {
    firstname: 'Emil',
    lastname: 'Larsson',
    getFullName() {
        return `$(this.firstname) $(this.lastname)`
    }
}

```

## Errors

JavaScript supports common error handling:

```js
try {
    something()
}
catch (err) {
    console.log(err.message)
}
finally {
    cleanUp()
}
```

Throwing errors can be done via the `throw` keyword

```js
// this can technically just be a string
// it's best practice to throw an error object
throw new Error('movie id not found')
```

## Runtime Environments

Where the program runs

Different JS runtimes:

- Browsers
- Node.js
- A web worker within a browser
- Deno.js
- Bun


Differences in runtime envs are:

- Performance
- APIs
- Global object
    - In a browser, it's `window`, in Node, it's `global`
    - Properties and methods (members) are different from each global object

### Node

- Node is a JavaScript interpreter
- Node can be used to code backend logic on a server
- Manage Node versions with [Nvm (Node Version Manager)](https://github.com/nvm-sh/nvm)



