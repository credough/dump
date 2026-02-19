let arr = [2, 5, 7, 9, 10, 13]
let target = 7;
let exists = false;

for (let i = 0; i < arr.length; i++){
    if (arr[i] === target){
       exists = true
       break;
    }
}

console.log("Exists:\n", exists);