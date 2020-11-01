//public/js/lesson.js
class Typing{
  constructor(lesson){
    this.letters = lesson
    this.counter = 0;
    this.showFinger = 0;
    this.nextKey = this.letters[0][0];
    this.pressedKey = 0;
    this.mistake = 0;
    this.numLetters = 0;
    this.setColor(this.nextKey);
    this.setClock();
  }

  setColor(nextKey){
    nextKey = nextKey.toUpperCase();
    
    var rightShift = {'A':1,'S':1,'D':1,'F':1,'G':1};
    var leftShift = {'H':1,'J':1,'K':1,'L':1,':':1,'"':1};

    var keys = $(".keyboard-base").children().css({'color':'black'});

    for(var index in keys){
      var key = keys[index].innerHTML;

      if((this.nextKey in rightShift) || (this.nextKey in leftShift)){
        switch(key){
          case ';':
            key = ":";
            break;
          case "'":
            key = '"';
            break;
        }
      }

      if(key == nextKey){
        keys[index].focus();
        $(keys[index]).css({'color':'teal'});

        if(this.nextKey in rightShift){
          $('.rightshift').css({'color':'teal'});
        }else if(this.nextKey in leftShift){
          $('.leftshift').css({'color':'teal'});
        }
      }
    }
    
    if(this.showFinger < 3)
      $('#finger').html(this.letters[this.counter][1]);
    else
      $('#finger').html('');

    $('#letter').html(this.letters[this.counter][2]);
  }

  checkKey(key){
    if(key == this.nextKey){
      if(this.counter < (this.letters).length - 1)
      this.counter += 1;
          
      else if(this.counter == (this.letters).length - 1){
        this.counter = 0;
        this.showFinger += 1
      }

      this.pressedKey = this.nextKey;
      this.nextKey = (this.letters[this.counter][0]);
      this.setColor(this.nextKey);
    }else{
      document.getElementById('beep').play();
      $('#mistake span').html(this.toKhNum(++this.mistake))
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

    setInterval(() => {
      $('#timelapse .second').html(this.toKhNum(++second));

      if(second == 60){
        second = 0;
        $('#timelapse .minute').html(this.toKhNum(++minute));
      }

      if(minute == 60){
        minute = 0;
        $('#timelapse .hour').html(this.toKhNum(++hour));
      }

    }, 1000);
  }
}//end of class
  