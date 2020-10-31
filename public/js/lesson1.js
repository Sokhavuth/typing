//public/js/lesson1.js
class Typing{
  constructor(){
    $(".keyboard-base .key").on({
      keypress: function(event){
        if(event.which != 32)
          var key = String.fromCharCode(event.which).toUpperCase();
        else if(event.which == 32){
          event.preventDefault();
          var key = "Space";
        }
        typing.checkKey(key)
      } 
    });

    this.letters = [['A','កូន​ដៃ','ា'],['S','នាង​ដៃ','ស'],['D','ចង្អុលកណ្តាល','ដ'],['F','ចង្អុលដៃ','ថ'],['G','ចង្អុលដៃ','ង'],
    ['H','ចង្អុល​ដៃ​ស្តាំ','ហ'],['J','ចង្អុល​ដៃ​ស្តាំ','្'],['K','ចង្អុលកណ្តាល','ក'],['L','នាងដៃ','ល'],[';','កូនដៃ','ើ'],
    ["'",'កូនដៃ','់'],['Space','មេដៃស្តាំ','']];
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
    if(this.showFinger < 2)
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
  