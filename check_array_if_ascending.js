let array = [2,1,4,5,6,7]
let sorted = true

for(let i = 0; i < array.length; i++){
    if(array[i + 1] < array[i]){
        sorted = false;
        break;
    }
}

console.log("Sorted:", sorted)