#!/usr/bin/node

const require = require('axios').default;
const path = (require.get(process.argv[2]))
path.then(function (response) {
  let count = 0;
  for (const pelis of response.data.results) {
    for(const actor of list.characters) {
      if (actor.endsWith('18/')) {
        count++;
        break;
    }
  }
}
  console.log(count);
})

.catch(function(err) {
  console.log('code :' + error.response.status);
});
