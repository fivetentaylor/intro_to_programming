const fs = require('fs');

fs.readFile('/dev/stdin', 'utf8', function(err, contents) {
  let myobj = JSON.parse(contents);
  myobj['morgan is cool'] = 'testing123';
  console.log(JSON.stringify(myobj));
});
