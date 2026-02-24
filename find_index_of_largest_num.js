let arr = [2,1,6,3,7,4]
let larg_index = 0

for(let i = 0; i < arr.length; i++){
    if(arr[larg_index] < arr[i]){
        larg_index = i
    }
}

console.log("Largest:", larg_index)