let maxValue = 10;
let result = 1;

debugger;
for (let counter = 0; counter < maxValue; counter++) {
    console.log(result);
    result *= maxValue - counter; 
}

console.log("Final result: ", result);