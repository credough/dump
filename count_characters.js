let phrase = "ang pogi ni aaron"
let count = 0;

for (let i = 0; i < phrase.length; i++){
    if (phrase[i] !== " "){
        count += 1;
    }
}

console.log("Number of Characters:\n", count);