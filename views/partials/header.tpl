<!--views/partials/header.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/main.js"></script>
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
                  <a href="/practice/1">លុះហាត់​ទី ១</a>
                  
                </div>
              </div>
            </div>
          </nav>
          <span class="login"><a href="/login">ចុះ​ឈ្មោះ</a></span>
        </div>
      </div>
      