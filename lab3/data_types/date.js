let d1 = new Date(2012, 1, 20, 3, 12);
alert( d1 );
function getLocalDay(date) {

    let day = date.getDay();
  
    if (day == 0) { // weekday 0 (sunday) is 7 in european
      day = 7;
    }
  
    return day;
  }
function getDateAgo(date, days) {
    date.setDate(date.getDate() - days);
    return date.getDate();
  }