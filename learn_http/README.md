# Learn HTTP (Hyper Text Transfer Protocol)

A web client makes a response to a web server

Any device (mobile, pc, server) can be a web client

A web server should be listening for inbound request 24/7

## Fetch api

JS env in browser

FrontEnd is everything the user sees
BackEnd is everything else

Fetch get's an array of objects, accessing them requires calling the element of the array

```js
async function fetchIPAddress(domain) {
  const resp = await fetch(`https://cloudflare-dns.com/dns-query?name=${domain}&type=A`, {
    headers: {
      'accept': 'application/dns-json'
    }
  })
  const respObject = await resp.json()
  // displaying how to access the response object
  const ip = respObject.Answer[0].data
  return ip
}
```

```js
// send a request to the given url with the given settings
// store the response in the const response
const response = await fetch(url, settings)
const responseData = await response.json()
```


- `response` is the data that comes back from the server
- `url` is the URL we are making a request to
- `settings` is an object containing some request-specific settings
- The `await` keyword tells JavaScript to wait until the response comes back from`the server before continuing
- `response.json()` converts the response data from the server into a JavaScript object


## URL api

```js
// creates an url object
const urlObj = new URL('https://example.com/example-path')
```

### URI = Uniform Resource Indentifier

A URI is a string that uniquely identifies a resource. It is a broader concept that includes URLs and URNs.

### URL = Uniform Resource Locator

`https://www.example.com/path/to/resource?query=param#fragment`

A URL specifies the location of a resource on the internet and the protocol used to access it.

### URN = Uniform Resource Name

A URN is a type of URI that uses a namespace to uniquely identify a resource by name, rather than location.

`urn:isbn:0451450523`

Any port can only be used by one program at a time

## Sync/Async

Synchronous programming is single threaded

Asynchronous programming is executed in multiple threads, main thread wait's for sub threads

In JS, the most popular asynchronous programming is done via the `Promise` object

The following code displays how a `Promise` object syntax is written, along with a `resolve` and `reject` call

```js
// arrow function that returns a promise object
const applyDamage = (damage, currentHP) => {
  return new Promise((resolve, reject) => {
    // sets timeout for 1000ms
    setTimeout(() => {
      if (currentHP - damage <= 0) {
        const rejectMsg = `The player suffers ${damage} points of damage and has fallen unconscious.`
        reject(rejectMsg)
      }
      else {
        const newHP = currentHP - damage
        const resolveMsg = `The player suffers ${damage} points of damage and has ${newHP} hit points remaining.`
        resolve(resolveMsg)
      }
      
    }, 1000)
  })
}
```

Deciding upon coding something sync or async depends on IO timings

This is a list of I/O operations that should (generally) either be done sync or async

Getting/Setting data from:

1. RAM (nano second) - Synchronously
2. Disk (1ms) - Synchronoulsy or Asynchronously
  If your text editor freeze while getting some files, that's a bad program
3. Network (100ms-2,000ms) - Asynchronously


`Async functions` can use the `fetch` method that returns an `promise` object.

The `await` keyword (that can act as a .then call) is only usable in an async function.

`await` and `async` should be used over `Promise()` and `.then`


## Network tab

Request headers = Sent from browser to the server

Response headers = Sent from the server back to the browser

## Json

JavaScriptObjectNotation


use json.stringify() to make an object a string, good for sending json

```js
 const response = await fetch(path, {
    method: 'PUT',
    mode: 'cors',
    headers: getHeaders(),
    body: JSON.stringify(locationObj) //stringify syntax example
  })
  return response.json()
```

use json.parse() 


## CRUD

```
POST = create
GET = read
PUT = update (should be idempotent)
DELETE = delete
```

### Put example

```js
// update user async function
async function updateUser(baseURL, id, data, apiKey) {
  
  // building the URL that we PUT towards
  const fullURL = `${baseURL}/${id}`
  
  // the following syntax creates a PUT request and stores it in the reponse variable
  // using the x-api and app/json type
  // body is json and is sent as a string
  const response = await fetch(fullURL, {
    method: 'PUT',
    mode: 'cors',
    headers: {
      'X-API-Key': apiKey,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  // returns a promise that resolves to the JSON response body of the fetch() request.
  return response.json()
}


// get's some data using similar syntax as above
async function getUserById(baseURL, id, apiKey) {
  const fullURL = `${baseURL}/${id}`
  const response = await fetch(fullURL, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'X-API-Key': apiKey,
      'Content-Type': 'application/json'
    }
  })
  return response.json()
}
```

## Status Codes

HTTP Status codes are contained in the response

```
100-199: Informational responses
200-299: Successful responses
300-399: Redirection messages
400-499: Client errors
500-599: Server errors
```


## RESTful API's

Representatiobnal State Transfer

Not all HTTP API's are REST

Restful is a common HTTP API convention that enables more reusable API development by having a ruleset

REST has a stateless architect, meaning the server or client does not have to be aware of eachother's states, since the request (GET, PUT, POST, DELETE) is done towards a resource (end of the URL)

URL Example

```
https://api.boot.dev/v1/courses_rest_api/learn-http/locations
https://api.boot.dev/v1/courses_rest_api/learn-http/users
https://api.boot.dev/v1/courses_rest_api/learn-http/items
```