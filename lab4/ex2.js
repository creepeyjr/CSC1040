const students = [
    { name: "Alice", grade: 72 },
    { name: "Bob",   grade: 45 },
    { name: "Carol", grade: 88 },
    { name: "Dan",   grade: 55 },
    { name: "Eve",   grade: 91 },
];

// custom function
function passCheck(student) {
    /*
    console.log(student);
    console.log(student["name"]);
    console.log(student["grade"]);
    */
    if (student["grade"] >= 60) {
        return student
    }
}

function gradeStrip(student) {
    return student["name"];
}

// loop through array, annouce every student's name and grade
for (let i = 0; i < students.length; i++) {
    console.log(students[i]["name"],":", students[i]["grade"]);
}

// Call function
let passes = students.filter(passCheck);
//console.log("passes :", passes);

let nameOnly = passes.map(gradeStrip);
console.log("Passing students :",nameOnly.length);
console.log("Passing names :", nameOnly);

// Reduce function

// Calculate the class average
const total = students.reduce((sum, s) => sum + s.grade, 0);
console.log("Class average :", total / students.length );