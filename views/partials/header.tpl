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
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <div id="site">
      <div id="blog-header">
        <div class="blog-title region">
          <a class="logo" href="/"><img src="/static/images/site_logo.png"/></a>
          <span><a href="/"> {{data['blogTitle']}}</a></span>
          <nav id="menu">
            <ul>
              <li><a href="/lesson">មេរៀន</a></li>
              <li><a href="/practice">លំហាត់</a></li>
            </ul>
          </nav>
          <span class="login"><a href="/login">ចុះ​ឈ្មោះ</a></span>
        </div>
      </div>
      