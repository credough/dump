let word = "heLlo Aaron pOgI"
let new_word = ""

for (let i = 0; i < word.length; i++){
    new_word += word[i].toUpperCase();
}

console.log("Uppercase of", word, ":", new_word)