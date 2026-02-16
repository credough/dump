let arr = [5, 6, -2, 8, -3, 9];

let positive = 0;
let negative = 0;

for (let i = 0; i < arr.length; i++){
    if (arr[i] > 0){
       positive ++;
    } else if (arr[i] < 0){
        negative ++;
    }
}

console.log("Negative\n", negative);
console.log("Positive:\n", positive);