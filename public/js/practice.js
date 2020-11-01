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
    $('.leftshift').css({'color':'black'});
    $('.rightshift').css({'color':'black'});

    nextKey = nextKey.toUpperCase();
    if(this.pressedKey)
      var pressedKey = (this.pressedKey).toUpperCase();

    var rightShift = {'A':1,'S':1,'D':1,'F':1,'G':1};
    var leftShift = {'H':1,'J':1,'K':1,'L':1,':':1,'"':1};

    var keys = $(".keyboard-base").children();
    for(var index in keys){
      var key = keys[index].innerHTML;

      if(this.nextKey == nextKey){
        if(key == ';'){
          key = ':';
        }else if(key == "'"){
          key = '"';
        }
      }

      if(key == nextKey){
        keys[index].focus();
        $(keys[index]).css({'color':'teal'});

        if(this.nextKey in rightShift){
          $('.rightshift').css({'color':'teal'});
          $('.leftshift').css({'color':'black'});
        }else if(this.nextKey in leftShift){
          $('.leftshift').css({'color':'teal'});
          $('.rightshift').css({'color':'black'});
        }
      }

      if(pressedKey && (key == pressedKey)){
        $(keys[index]).css({'color':'black'});
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
    var minuteTest = 0
    
    setInterval(() => {
      $('#timelapse .second').html(this.toKhNum(++second));
      if(second == 60){
        second = 0;
        $('#timelapse .minute').html(this.toKhNum(++minute));
      }

      if(minute == 60){
        minute = 0;
        ++minuteTest;
        $('#timelapse .hour').html(this.toKhNum(++hour));
      }

      if((minuteTest <= 3) && (this.scoreLetter >= 720) && (this.mistake == 0))
        alert('សូម​អបអរ​សាទ​ដោយ​អ្នក​បាន​​ឆ្លង​ផុត​កំរឹត​នេះ​ហើយ​!!');

    }, 1000);
  }
}//end of class
