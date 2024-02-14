//1
function camelize(str) {
    return str
      .split('-')
      .map(
        (word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1)
      )
      .join('');
  }
  
  //2
  function filterRange(arr, a, b) {
    return arr.filter(item => (a <= item && item <= b));
  }
  
  arr = [5, 3, 8, 1];
  
  let filtered = filterRange(arr, 1, 4);
  
  alert( filtered ); 
  
  alert( arr );
  
  //3
  
  function filterRangeInPlace(arr, a, b) {
  
    for (let i = 0; i < arr.length; i++) {
      let val = arr[i];
      if (val < a || val > b) {
        arr.splice(i, 1);
        i--;
      }
    }
  
  }
  
  arr = [5, 3, 8, 1];
  
  filterRangeInPlace(arr, 1, 4); 
  
  alert( arr );
  
  //4
  
  arr = [5, 2, 1, -10, 8];
  
  arr.sort((a, b) => b - a);
  
  alert( arr );
  
  //5
  function copySorted(arr) {
    return arr.slice().sort();
  }
  
  arr = ["HTML", "JavaScript", "CSS"];
  
  let sorted = copySorted(arr);
  
  alert( sorted );
  alert( arr );
  
  //6
  
  function Calculator() {
  
    this.methods = {
      "-": (a, b) => a - b,
      "+": (a, b) => a + b
    };
  
    this.calculate = function(str) {
  
      let split = str.split(' '),
        a = +split[0],
        op = split[1],
        b = +split[2]
  
      if (!this.methods[op] || isNaN(a) || isNaN(b)) {
        return NaN;
      }
  
      return this.methods[op](a, b);
    }
  
    this.addMethod = function(name, func) {
      this.methods[name] = func;
    };
  }
  
  
  //7
  let vasya = { name: "Вася", age: 25 };
  let petya = { name: "Петя", age: 30 };
  let masha = { name: "Маша", age: 28 };
  
  let users = [ vasya, petya, masha ];
  
  let names = users.map(item => item.name);
  
  alert( names ); // Вася, Петя, Маша
  
  
  //8
  vasya = { name: "Вася", surname: "Пупкин", id: 1 };
  petya = { name: "Петя", surname: "Иванов", id: 2 };
  masha = { name: "Маша", surname: "Петрова", id: 3 };
  
  users = [ vasya, petya, masha ];
  
  let usersMapped = users.map(user => ({
    fullName: `${user.name} ${user.surname}`,
    id: user.id
  }));
  
  /*
  usersMapped = [
    { fullName: "Вася Пупкин", id: 1 },
    { fullName: "Петя Иванов", id: 2 },
    { fullName: "Маша Петрова", id: 3 }
  ]
  */
  
  alert( usersMapped[0].id ); // 1
  alert( usersMapped[0].fullName ); // Вася Пупкин
  
  //9
  function sortByAge(arr) {
    arr.sort((a, b) => a.age > b.age ? 1 : -1);
  }
  
  vasya = { name: "Вася", age: 25 };
  petya = { name: "Петя", age: 30 };
  masha = { name: "Маша", age: 28 };
  
  arr = [ vasya, petya, masha ];
  
  sortByAge(arr);
  
  // теперь отсортировано: [vasya, masha, petya]
  alert(arr[0].name); // Вася
  alert(arr[1].name); // Маша
  alert(arr[2].name); // Петя
  
  
  //10
  function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
  }
  
  arr = [1, 2, 3];
  shuffle(arr);
  alert(arr);
  
  
  //11
  
  function getAverageAge(users) {
    return users.reduce((prev, user) => prev + user.age, 0) / users.length;
  }
  
  vasya = { name: "Вася", age: 25 };
  petya = { name: "Петя", age: 30 };
  masha = { name: "Маша", age: 29 };
  
  arr = [ vasya, petya, masha ];
  
  alert( getAverageAge(arr) ); // 28
  
  
  //12
  function unique(arr) {
    let result = [];
  
    for (let str of arr) {
      if (!result.includes(str)) {
        result.push(str);
      }
    }
  
    return result;
  }
  
  let strings = ["кришна", "кришна", "харе", "харе",
    "харе", "харе", "кришна", "кришна", ":-O"
  ];
  
  alert( unique(strings) ); // кришна, харе, :-O
  
  
  
  //13
  function groupById(array) {
    return array.reduce((obj, value) => {
      obj[value.id] = value;
      return obj;
    }, {})
  }