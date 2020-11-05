//public/js/practice.js
class Typing{
  constructor(practice){
    this.letters = practice;
    this.counter = Math.floor(Math.random() * (this.letters).length);
    this.usedCounter = this.counter;
    this.nextKey = this.letters[this.counter][0];
    this.pressedKey = 0;
    this.mistake = 0;
    this.scoreLetter = 0;
    this.numLetters = 0;
    this.setClock();
    this.setColor(this.nextKey);
  }

  setColor(nextKey){
    var rightShift = {'A':1,'S':1,'D':1,'F':1,'G':1,'Z':1,'X':1,'C':1,'V':1,'B':1,'Q':1,'W':1,'E':1,'R':1,'T':1,
                      '~':1,'!':1,'@':1,'#':1,'$':1,'%':1};
    var leftShift = {'H':1,'J':1,'K':1,'L':1,':':1,'"':1,'N':1,'M':1,'<':1,'>':1,'?':1,'Y':1,'U':1,'I':1,'O':1,'P':1,
                    '{':1,'}':1,'|':1,'^':1,'&':1,'*':1,'(':1,')':1,'_':1,'+':1};

    var keys = $(".keyboard-base").children().css({'color':'black'});
    
    for(var index in keys){
      var key = keys[index].innerHTML;

      if(key){
        var data = keys[index].getAttribute("data-l");
        if(key == "'"){
          data += '"';
        }

        if((nextKey == data[5]) || (nextKey == data[6])){
          keys[index].focus();
          $(keys[index]).css({'color':'teal'});

          if(this.nextKey in rightShift){
            $('.rightshift').css({'color':'teal'});
          }else if(this.nextKey in leftShift){
            $('.leftshift').css({'color':'teal'});
          }

          break;
        }
      }
    }
    
    $('#letter').html(this.letters[this.counter][2]);
  }

  checkKey(key){
    if(key == this.nextKey){
      this.scoreLetter += 1;
      while(true){
        this.counter = Math.floor(Math.random() * (this.letters).length);
        if(this.counter != this.usedCounter){
          this.usedCounter = this.counter
          break;
        }
      }

      this.pressedKey = this.nextKey;
      this.nextKey = this.letters[this.counter][0];
      this.setColor(this.nextKey);
    }else{
      document.getElementById('beep').play();
      $('#mistake span').html(this.toKhNum(++this.mistake));
    }

    $('#letters span').html(this.toKhNum(++this.numLetters))
  }

  toKhNum(number){
    const khNum = {'0':'០', '1':'១', '2':'២', '3':'៣', '4':'៤', '5':'៥', '6':'៦', '7':'៧', '8':'៨', '9':'៩'};
    var stringNum = number.toString();
    var khNumString = '';
   
    for(var i in stringNum){
      khNumString += khNum[stringNum[i]];
    }
   
    return khNumString;
  }

  setClock(){
    var second = 0;
    var minute = 0;
    var hour = 0;
    this.minuteTest = 0;
    
    this.clock = setInterval(() => {
      $('#timelapse .second').html(this.toKhNum(++second));
      if(second == 60){
        second = 0;
        $('#timelapse .minute').html(this.toKhNum(++minute));
      }

      if(minute == 60){
        minute = 0;
        ++this.minuteTest;
        $('#timelapse .hour').html(this.toKhNum(++hour));
      }

      if((this.minuteTest <= 2) && (this.scoreLetter >= 5) && (this.mistake <= 10))
        this.updateLevel();
    }, 1000);
  }

  updateLevel(){
    clearInterval(this.clock)
    $.get("login/update",
      function(data, status){
        if(status == "success"){
          var grade = typing.toKhNum(data.grade);
          $('#info').html(`សូម​អបអរ​សាទ​ដោយ​អ្នក​បាន​​ឆ្លង​ចូល​កំរឹត​ទី ${grade} ហើយ!!`);
          $('#level span').html(grade);
          document.getElementById('level').children[0].innerHTML = grade;
        }
     });
  }
}//end of class
