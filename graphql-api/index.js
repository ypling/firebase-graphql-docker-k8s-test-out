const express = require("express")
const {createHandler} = require("graphql-http/lib/use/express")
const {buildSchema} = require("graphql")
const {ruruHTML} = require("ruru/server")
// const loggingMiddleware =require("./middlewares/authenticate.js")

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    message: String
  }
`)

// The root provides a resolver function for each API endpoint
const root = {
    message() {
        return "Hello world!!!"
    },
}

const app = express()
// app.use(loggingMiddleware)
// Create and use the GraphQL handler.
app.all(
    "/graphql",
    createHandler({
        schema: schema,
        rootValue: root,
    })
)

// Serve the GraphiQL IDE.
app.get("/", (_req, res) => {
    res.type("html")
    res.end(ruruHTML({endpoint: "/graphql"}))
})

// Start the server at port
app.listen(3000)
console.log("Running a GraphQL API server at http://localhost:30080/graphql")