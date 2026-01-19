const calculator = {
    num1: 11,
    num2: 20,

    add() {
    return this.num1 + this.num2;
    },

    subtract() {
    return this.num1 - this.num2;
    },

    divide() {
    return this.num1 / this.num2;
    },

    multiply() {
    return this.num1 * this.num2;
    }
};

console.log(calculator.add());
console.log(calculator.subtract())
console.log(calculator.multiply())
console.log(calculator.divide());