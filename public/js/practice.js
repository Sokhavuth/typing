//public/js/practice.js
class Typing{
  constructor(practice){
    this.letters = practice;
    this.counter = Math.floor(Math.random() * (this.letters).length);
    this.usedCounter = this.counter;
    this.nextKey = this.letters[this.counter][0];
    this.setColor(this.nextKey);
  }

  setColor(nextKey){
    var keys = $(".keyboard-base").children();
    for(var index in keys){
      if(keys[index].innerHTML == nextKey){
        keys[index].focus();
        $(keys[index]).css({'color':'teal'});
      }

      if(this.pressedKey && (keys[index].innerHTML == this.pressedKey)){
        $(keys[index]).css({'color':'black'});
      }
    }
    
    $('#letter').html(this.letters[this.counter][2]);
  }

  checkKey(key){
    if(key == this.nextKey){
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
    }else
      document.getElementById('beep').play();
  }
}//end of class
