car = {
    brand: "Toyota",
    model: "Hi-ace",
    speed: 0,

    acceleration(amount) {
        this.speed += amount;
        console.log(`Current speed: ${this.speed} km/h`)
    },

    break(amount) {
        this.speed -= amount;
        if(amount < 0) this.speed = 0;
        console.log(`Current speed: ${this.speed} km/h`)
    }
}

console.log(car.brand);
console.log(car.model);
console.log(car.acceleration(100));
console.log(car.break(-50));