const express = require('express')
const fs = require('fs')
const app = express()

app.get('/cat', (req, res) => {
  // Read the contents of the 'static/cats' directory
  fs.readdir('./static/cats', (err, files) => {
    if (err) {
      // If there is an error reading the directory, return a 500 Internal Server Error response
      res.status(500).send(err.message)
      return
    }

    // Select a random file from the directory
    const index = Math.floor(Math.random() * files.length)
    const file = files[index]

    // Create a readable stream from the selected file
    const stream = fs.createReadStream(`./static/cats/${file}`)

    // Set the 'Content-Type' header of the response to 'image/jpeg'
    res.setHeader('Content-Type', 'image/jpeg')

    // Pipe the data from the stream to the response
    stream.pipe(res)
  })
})

app.listen(80, () => {
  console.log('Server listening on port 80')
})
