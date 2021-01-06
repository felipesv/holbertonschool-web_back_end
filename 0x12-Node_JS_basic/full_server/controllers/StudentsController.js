const readDatabase = require('../utils')

class StudentsController {
	static getAllStudents(request, response) {
		readDatabase(process.argv[2])
		.then((data) => {
			const printData = []
			printData.push('This is the list of our students');
			for (const field in data) {
				printData.push(`Number of students in ${field}: ${data[field].number}. ${data[field].list}`);
			}
			response.send(printData.join('\n'));
		})
		.catch((err) => { throw err;});
	}

	static getAllStudentsByMajor(request, response) {
		if (!["SWE", "CS"].includes(request.params['major']))
			response.status(500).send('Major parameter must be CS or SWE');
		else
			readDatabase(process.argv[2])
			.then((data) => {
				response.send(data[request.params['major']].list);
			})
			.catch((err) => { throw err;});
	}
}

module.exports = StudentsController