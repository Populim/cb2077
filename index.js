// FileName: index.js
// Import express
let express = require('express')//Initialize the app
let app = express();// Setup server port
const path = require('path');
var port = process.env.PORT || 8081;// Send message for default URL
app.listen(port, function () {
     console.log("Running cb2077 on port " + port);
});

app.use(express.static(path.join(__dirname + '/public')));
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname+'/public/index.html'));
});