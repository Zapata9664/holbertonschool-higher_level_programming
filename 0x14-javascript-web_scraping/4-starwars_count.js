#!/usr/bin/node

const require = require('axios').default;
require.get(process.argv[2])
  .then(function (response) {
  let count = 0;
  for (const pelis of response.data.results) {
    for (const actor of pelis.characters) {
      if (actor.endsWith('18/')) {
        count++;
        break;
    }
  }
}
  console.log(count);
})

.catch(function(error) {
  console.log('code :' + error.response.status);
});
