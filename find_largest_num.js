let arr = [3, 9, 2, 15, 6];

let largest = arr[0];

for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
        largest = arr[i];
    }
}

console.log("Largest:\n", largest)