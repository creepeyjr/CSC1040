/*
Recreate sample python script in JavaScript so running node ex1.js
produces identical output.
*/

const subject = "Computer Science";
const year = 2;
const is_enrolled = true;



if (is_enrolled == true) {
    console.log(subject, "- Year", year);
}
else {
    console.log("Not enrolled.");
}

const marks = [62, 45, 78, 91, 55, 83];
let total = 0;

// Gather all marks together
for (let i = 0; i < marks.length; i++) {
    //console.log(marks[i]);
    total += marks[i];
}
// Print out grade average
let averageGrade = total / marks.length;
console.log("Average mark:", averageGrade);

for (let i = 0; i < marks.length; i++) {
    if (marks[i] >= 40) {
        console.log(marks[i],"- Pass")
    }
    else {
        console.log(marks[i],"- Fail")
    }

}