const express = require('express');
const fs = require('fs');

const countStudents = async (path) => {
	try {
	  const csvData = await fs.promises.readFile(path, { encoding: 'utf8' });
	  const fields = {};
	  const dataShow = {};
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
	  dataShow.numberStudents = `Number of students: ${data.length}`;
	  dataShow.studentsFields = [];
	  for (const field in fields) {
		if (field) {
		  const list = fields[field];
		  dataShow.studentsFields.push(`Number of students in ${field}: ${list.length}. List: ${list.toString().replace(/,/g, ', ')}`);
		}
	  }
	  return dataShow;
	} catch (err) {
	  throw new Error('Cannot load the database');
	}
  };
const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
	res.write('This is the list of our students\n');
    countStudents(process.argv[2]).then((dataShow) => {
      res.write(`${dataShow.numberStudents}\n`);
      res.write(dataShow.studentsFields.join('\n'));
      res.end();
    }).catch(() => {
      res.end('Error: Cannot load the database');
      throw new Error('Cannot load the database');
    });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
