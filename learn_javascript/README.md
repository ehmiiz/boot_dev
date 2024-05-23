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