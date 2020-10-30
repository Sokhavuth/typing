<!--views/index.tpl-->
<!--views/partials/header.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/lesson1.js"></script>
    <link href="/static/styles/main.css" rel="stylesheet"></link>
    <link href="/static/styles/menu.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>
  <body>
    <div id="site">
      <div id="blog-header">
        <div class="blog-title region">
          <a class="logo" href="/"><img src="/static/images/site_logo.png"/></a>
          <span><a href="/">{{data['blogTitle']}}</a></span>
          <nav id="menu">
            <div class="navbar">
              <div class="dropdown">
                <button class="dropbtn">មេរៀន
                  <i class="fa fa-caret-down"></i>
                </button>
                <div class="dropdown-content">
                  <a href="/lesson/1">មេរៀន​ទី ១</a>
                 
                </div>
              </div>

              <div class="dropdown">
                <button class="dropbtn">លំហាត់
                  <i class="fa fa-caret-down"></i>
                </button>
                <div class="dropdown-content">
                  <a href="#">លុះហាត់​ទី ១</a>
                  
                </div>
              </div>
            </div>
          </nav>
          <span class="login"><a href="/login">ចុះ​ឈ្មោះ</a></span>
        </div>
      </div>

<div id="main" class="main region">
  <div id="content" class="content">
    <div id="panel">
     <div id="finger"></div>
     <div id="letter"></div>
    </div>
    <div class="keyboard-base">
      <div tabindex="0" class="key">~</div>
      <div tabindex="0" class="key">1</div>
      <div tabindex="0" class="key">2</div>
      <div tabindex="0" class="key">3</div>
      <div tabindex="0" class="key">4</div>
      <div tabindex="0" class="key">5</div>
      <div tabindex="0" class="key">6</div>
      <div tabindex="0" class="key">7</div>
      <div tabindex="0" class="key">8</div>
      <div tabindex="0" class="key">9</div>
      <div tabindex="0" class="key">0</div>
      <div tabindex="0" class="key">-</div>
      <div tabindex="0" class="key">+</div>
      <div tabindex="0" class="key delete">Delete</div>
      <div tabindex="0" class="key tab">Tab</div>
      <div tabindex="0" class="key">Q</div>
      <div tabindex="0" class="key">W</div>
      <div tabindex="0" class="key">E</div>
      <div tabindex="0" class="key">R</div>
      <div tabindex="0" class="key">T</div>
      <div tabindex="0" class="key">Y</div>
      <div tabindex="0" class="key">U</div>
      <div tabindex="0" class="key">I</div>
      <div tabindex="0" class="key">O</div>
      <div tabindex="0" class="key">P</div>
      <div tabindex="0" class="key">[</div>
      <div tabindex="0" class="key">]</div>
      <div tabindex="0" class="key backslash">\</div>
      <div tabindex="0" class="key capslock">CapsLock</div>
      <div tabindex="0" class="key">A</div>
      <div tabindex="0" class="key">S</div>
      <div tabindex="0" class="key">D</div>
      <div tabindex="0" class="key">F</div>
      <div tabindex="0" class="key">G</div>
      <div tabindex="0" class="key">H</div>
      <div tabindex="0" class="key">J</div>
      <div tabindex="0" class="key">K</div>
      <div tabindex="0" class="key">L</div>
      <div tabindex="0" class="key">;</div>
      <div tabindex="0" class="key">'</div>
      <div tabindex="0" class="key return">Return</div>
      <div tabindex="0" class="key leftshift">Shift</div>
      <div tabindex="0" class="key">Z</div>
      <div tabindex="0" class="key">X</div>
      <div tabindex="0" class="key">C</div>
      <div tabindex="0" class="key">V</div>
      <div tabindex="0" class="key">B</div>
      <div tabindex="0" class="key">N</div>
      <div tabindex="0" class="key">M</div>
      <div tabindex="0" class="key">,</div>
      <div tabindex="0" class="key">.</div>
      <div tabindex="0" class="key">/</div>
      <div tabindex="0" class="key rightshift">Shift</div>
      <div tabindex="0" class="key leftctrl">Ctrl</div>
      <div tabindex="0" class="key">Alt</div>
      <div tabindex="0" class="key command">Command</div>
      <div tabindex="0" class="key space">Space</div>
      <div tabindex="0" class="key command">command</div>
      <div tabindex="0" class="key">Alt</div>
      <div tabindex="0" class="key">Ctrl</div>
      <div tabindex="0" class="key">Fn</div>
    </div>
  </div>
</div>

%include("./partials/footer.tpl")