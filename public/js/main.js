//public/js/main.js
class Typing{
  constructor(){
    $(".keyboard-base .key").on({
      keypress: function(event){
        if(event.which != 32)
          var key = String.fromCharCode(event.which).toUpperCase();
        else if(event.which == 32)
          var key = "Space";
        
        typing.checkKey(key)
      } 
    });

    this.letters = [['A','កូន​ដៃ','ា'],['S','នាង​ដៃ','ស'],['D','ចង្អុលកណ្តាល','ដ'],['F','ចង្អុលដៃ','ថ'],['G','ចង្អុលដៃ','ង'],
    ['H','ចង្អុល​ដៃ​ស្តាំ','ហ'],['J','ចង្អុល​ដៃ​ស្តាំ','ដាក់ជើង'],['K','ចង្អុលកណ្តាល','ក'],['L','នាងដៃ','ល'],[';','កូនដៃ','ើ'],
    ["'",'កូនដៃ','់'],['Space','មេដៃស្តាំ','ដកឃ្លា​មើល​មិន​ឃើញ']];
    this.counter = 0;
    this.nextKey = this.letters[0][0];
    this.setBackground(this.nextKey);
  }

  setBackground(nextKey){
    var keys = $(".keyboard-base").children();
    for(var index in keys){
      if(keys[index].innerHTML == nextKey){
        keys[index].focus();
        $(keys[index]).css({'background':'teal'});
      }

      if(this.pressedKey && (keys[index].innerHTML == this.pressedKey)){
        $(keys[index]).css({'background':'rgb(243, 243, 243)'});
      }
    }

    $('#finger').html(this.letters[this.counter][1]);
    $('#letter').html(this.letters[this.counter][2]);
  }

  checkKey(key){
    if(key == this.nextKey){
      if(this.counter < (this.letters).length - 1)
        this.counter += 1;
      else if(this.counter == (this.letters).length - 1)
        this.counter = 0;

      this.pressedKey = this.nextKey;
      this.nextKey = this.letters[this.counter][0];
      this.setBackground(this.nextKey);
    }
  }
}//end of class