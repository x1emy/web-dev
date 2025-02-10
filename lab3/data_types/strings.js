function letter(str){
    if(!str) return str;
    return str[0].toUpperCase() + str.slice(1);
}
alert(letter('john'));

function checkSpam(str){
    let lower=str.toLowerCase();
    return lower.includes('viagra') || lower.includes('xxx');

}
alert( checkSpam('buy ViAgRA now') );
alert( checkSpam('free xxxxx') );
alert( checkSpam("innocent rabbit") );