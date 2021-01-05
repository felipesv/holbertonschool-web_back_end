const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, 'utf8').split('\n');
    const fields = {};
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
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
