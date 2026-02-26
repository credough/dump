let arr = [1,2,3,4,5,6,7]
let c = 0;

for(let i = 0; i < arr.length; i++){
    if(arr[i] % 2 !== 0){
        c++;
    }
}

console.log("Odds:", c)