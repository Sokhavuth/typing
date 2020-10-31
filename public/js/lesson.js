//public/js/lesson.js
class Typing{
  constructor(lesson){
    this.letters = lesson
    this.counter = 0;
    this.showFinger = 0;
    this.nextKey = this.letters[0][0];
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
      this.nextKey = this.letters[this.counter][0];
      this.setColor(this.nextKey);
    }else
      document.getElementById('beep').play();
  }
}//end of class
  