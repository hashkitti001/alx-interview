#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieID = process.argv[2];
  request(`${API_URL}/films/${movieID}/`, (err, _, body) => {
    if (err) {
      console.error(err);
    }
    const characterURLs = JSON.parse(body).characters;
    const characterNames = characterURLs.map(url =>
      new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charReqBody).name);
        });
      })
    );
    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErrs => console.error(allErrs));
  });
}
