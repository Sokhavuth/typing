<!--views/login.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/login.js"></script>
    <link href="/static/styles/login.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <div id="site">
      <form id="login" action='/login/user' method='post'>
        <div  id='info'>ទំរង់បែបបទ​ចុះ​ឈ្មោះ</div>
        <div class="wrapper">
          <a></a><div style='text-align:center;'><dv class='message'>{{data['message']}}</dv></div>
          <a>អ្នក​ប្រើប្រាស់ៈ</a><input class='username' type='text' name='fusername' required />
          <a>ពាក្យ​សំងាត់ៈ</a><input class='password' type='password' name='fpassword' required />
          <a>Email:​</a><input type="email" name="femail" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" required />
          <a></a><input type='submit' value='បញ្ជូន' />
        </div>
        %data['message'] = ''
      </form>
    </div><!--sites-->
  </body>
</html>