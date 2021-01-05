const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, (error, csvData) => {
    if (error) {
      reject(Error('Cannot load the database'));
    }
    if (csvData) {
      const fields = {};
      const data = csvData.toString().split('\n');
      data.shift();
      data.forEach((element) => {
        const row = element.split(',');
        if (row[3] in fields) {
          fields[row[3]].push(row[0]);
        } else {
          fields[row[3]] = [row[0]];
        }
      });
      console.log(`Number of students: ${data.length}`);
      for (const field in fields) {
        if (field) {
          const list = fields[field];
          console.log(`Number of students in ${field}: ${list.length}. List: ${list.toString().replace(/,/g, ', ')}`);
        }
      }
    }
    resolve();
  });
});

module.exports = countStudents;
