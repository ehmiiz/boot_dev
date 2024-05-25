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