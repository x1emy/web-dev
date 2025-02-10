let user={
    name:'John',
    surname:'Smith',
}
user.name='Pete';
delete user.name

let schedule={};
function isEmpty(obj){
    for(let key in obj){
        return false;
    }
    return true;
}
alert(isEmpty(schedule))
schedule["8:30"] = "get up";
alert(isEmpty(schedule));

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}
let sum =0;
for(key in obj){
    sum+=salaries[key];
}
alert(sum);

let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };
  
function multiplyNumeric(obj){
    for(key in obj){
        obj[key]*=2;
    }
}
multiplyNumeric(menu);
