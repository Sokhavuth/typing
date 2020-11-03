<div id="main" class="main region">
  <div id="content" class="content">
    <div id="panel">
      <div id='left-panel'>
        <div id="mistake">កំហុសៈ <span>០</span></div>
        <div id='letters'>ចំនួន​អក្សរៈ <span>០</span></div>
        <div id="timelapse">
          រយៈពេលៈ <span class="hour">០</span>:<span class="minute">០</span>:<span class="second">០</span>
        </div>
      </div>
      <div>
        <div id="finger"></div>
        <div id="letter"></div>
      </div>
     
      <div id='right-panel'>
        <div id="user">{{data['user'][0]}}</div>
        <div id='level'>កំរឹតៈ <span>{{data['KhmerNumber'][data['user'][2]]}}</span></div>
      </div>
    </div>
    <div class="keyboard-base">
      <div tabindex="0" data-l="*****`~" class="key">`</div>
      <div tabindex="0" data-l="*****1!" class="key">1</div>
      <div tabindex="0" data-l="*****2@" class="key">2</div>
      <div tabindex="0" data-l="*****3#" class="key">3</div>
      <div tabindex="0" data-l="*****4$" class="key">4</div>
      <div tabindex="0" data-l="*****5%" class="key">5</div>
      <div tabindex="0" data-l="*****6^" class="key">6</div>
      <div tabindex="0" data-l="*****7&" class="key">7</div>
      <div tabindex="0" data-l="*****8*" class="key">8</div>
      <div tabindex="0" data-l="*****9(" class="key">9</div>
      <div tabindex="0" data-l="*****0)" class="key">0</div>
      <div tabindex="0" data-l="*****-_" class="key">-</div>
      <div tabindex="0" data-l="*****=+" class="key">=</div>
      <div tabindex="0" data-l="" class="key delete">Delete</div>
      <div tabindex="0" data-l="" class="key tab">Tab</div>
      <div tabindex="0" data-l="*****qQ" class="key">Q</div>
      <div tabindex="0" data-l="*****wW" class="key">W</div>
      <div tabindex="0" data-l="*****eE" class="key">E</div>
      <div tabindex="0" data-l="*****rR" class="key">R</div>
      <div tabindex="0" data-l="*****tT" class="key">T</div>
      <div tabindex="0" data-l="*****yY" class="key">Y</div>
      <div tabindex="0" data-l="*****uU" class="key">U</div>
      <div tabindex="0" data-l="*****iI" class="key">I</div>
      <div tabindex="0" data-l="*****oO" class="key">O</div>
      <div tabindex="0" data-l="*****pP" class="key">P</div>
      <div tabindex="0" data-l="*****[{" class="key">[</div>
      <div tabindex="0" data-l="*****]}" class="key">]</div>
      <div tabindex="0" data-l="*****\|" class="key backslash">\</div>
      <div tabindex="0" data-l="" class="key capslock">CapsLock</div>
      <div tabindex="0" data-l="*****aA" class="key">A</div>
      <div tabindex="0" data-l="*****sS" class="key">S</div>
      <div tabindex="0" data-l="*****dD" class="key">D</div>
      <div tabindex="0" data-l="*****fF" class="key">F</div>
      <div tabindex="0" data-l="*****gG" class="key">G</div>
      <div tabindex="0" data-l="*****hH" class="key">H</div>
      <div tabindex="0" data-l="*****jJ" class="key">J</div>
      <div tabindex="0" data-l="*****kK" class="key">K</div>
      <div tabindex="0" data-l="*****lL" class="key">L</div>
      <div tabindex="0" data-l="*****;:" class="key">;</div>
      <div tabindex="0" data-l="*****'" class="key">'</div>
      <div tabindex="0" data-l="" class="key return">Return</div>
      <div tabindex="0" data-l="" class="key leftshift">Shift</div>
      <div tabindex="0" data-l="*****zZ" class="key">Z</div>
      <div tabindex="0" data-l="*****xX" class="key">X</div>
      <div tabindex="0" data-l="*****cC" class="key">C</div>
      <div tabindex="0" data-l="*****vV" class="key">V</div>
      <div tabindex="0" data-l="*****bB" class="key">B</div>
      <div tabindex="0" data-l="*****nN" class="key">N</div>
      <div tabindex="0" data-l="*****mM" class="key">M</div>
      <div tabindex="0" data-l="*****,<" class="key">,</div>
      <div tabindex="0" data-l="*****.>" class="key">.</div>
      <div tabindex="0" data-l="*****/?" class="key">/</div>
      <div tabindex="0" data-l="" class="key rightshift">Shift</div>
      <div tabindex="0" data-l="" class="key leftctrl">Ctrl</div>
      <div tabindex="0" data-l="" class="key">Alt</div>
      <div tabindex="0" data-l="" class="key command">Command</div>
      <div tabindex="0" data-l="***** " class="key space">Space</div>
      <div tabindex="0" data-l="" class="key command">command</div>
      <div tabindex="0" data-l="" class="key">Alt</div>
      <div tabindex="0" data-l="" class="key">Ctrl</div>
      <div tabindex="0" data-l="" class="key">Fn</div>
    </div>
  </div>
</div>

<script>
  const typing = new Typing({{!data['lesson']}});
</script>