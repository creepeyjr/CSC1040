/*
Recreate sample python script in JavaScript so running node ex1.js
produces identical output.
*/

const subject = "Computer Science";
const year = 2;
const is_enrolled = true;



if (is_enrolled == true) {
    console.log(subject, "- Year ", year);
}
else {
    console.log("Not enrolled.");
}

const marks = [62, 45, 78, 91, 55, 83];
let total = 0;
for (let i = 0; i < marks.length; i++) {
    console.log(marks[i]);
}