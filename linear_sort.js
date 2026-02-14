let arr = [10, 4, 7, 2, 9];
let target = 7;

let found = false;

for(let i = 0; i < arr.length; i++){
    if(arr[i] === target) {
        console.log("Found at index:", i)
        found = true;
        break;
    }
}

if(!found) {
    console.log("Not found!")
}