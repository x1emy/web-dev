let calculator = new Calculator();
calculator.read();

function Calculator(){
    this.read = function(){
        this.a = prompt=('a?');
        this.b = prompt=('b?');
    }
    this.sum = function(){
        return this.a + this.b;
    }
    this.mul = function(){
        return this.a * this.b;
    }
}
alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );