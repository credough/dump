let arr = [1, 2, 2, 3, 4, 4, 5];
let unique = [];

for (let i = 0; i < arr.length; i++){
    if(!unique.includes(arr[i])){
        unique.push(arr[i])
    }
}

console.log(unique);