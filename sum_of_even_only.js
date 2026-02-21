let num = [1,2,3,4,5,6,7,8,9,10,11,12]
let sum = 0;

for(let i = 0; i < num.length; i++){
    if(num[i] % 2 === 0){
        sum += num[i]
    }
}

console.log("Sum of even numbers:\n", sum);