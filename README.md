<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

  <title>State Of Kiambu</title>

  <style>
    /*FOOTER*/

    footer {
      background: #0eb14d;
      background: -webkit-linear-gradient(59deg, #29b447, #16222A);
      background: linear-gradient(59deg, #199b4f, #16222A);
      color: white;
      margin-top: 100px;
    }

    footer a {
      color: #fff;
      font-size: 14px;
      transition-duration: 0.2s;
    }

    footer a:hover {
      color: #FA944B;
      text-decoration: none;
    }

    .copy {
      font-size: 12px;
      padding: 10px;
      border-top: 1px solid #FFFFFF;
    }

    .footer-middle {
      padding-top: 2em;
      color: white;
    }


    /*SOCİAL İCONS*/

    /* footer social icons */

    ul.social-network {
      list-style: none;
      display: inline;
      margin-left: 0 !important;
      padding: 0;
    }

    ul.social-network li {
      display: inline;
      margin: 0 5px;
    }


    /* footer social icons */

    .social-network a.icoFacebook:hover {
      background-color: #3B5998;
    }

    .social-network a.icoLinkedin:hover {
      background-color: #007bb7;
    }

    .social-network a.icoFacebook:hover i,
    .social-network a.icoLinkedin:hover i {
      color: #fff;
    }

    .social-network a.socialIcon:hover,
    .socialHoverClass {
      color: #44BCDD;
    }

    .social-circle li a {
      display: inline-block;
      position: relative;
      margin: 0 auto 0 auto;
      -moz-border-radius: 50%;
      -webkit-border-radius: 50%;
      border-radius: 50%;
      text-align: center;
      width: 30px;
      height: 30px;
      font-size: 15px;
    }

    .social-circle li i {
      margin: 0;
      line-height: 30px;
      text-align: center;
    }

    .social-circle li a:hover i,
    .triggeredHover {
      -moz-transform: rotate(360deg);
      -webkit-transform: rotate(360deg);
      -ms--transform: rotate(360deg);
      transform: rotate(360deg);
      -webkit-transition: all 0.2s;
      -moz-transition: all 0.2s;
      -o-transition: all 0.2s;
      -ms-transition: all 0.2s;
      transition: all 0.2s;
    }

    .social-circle i {
      color: #595959;
      -webkit-transition: all 0.8s;
      -moz-transition: all 0.8s;
      -o-transition: all 0.8s;
      -ms-transition: all 0.8s;
      transition: all 0.8s;
    }

    .social-network a {
      background-color: #F9F9F9;
    }

    .overlay {
      /* Height & width depends on how you want to reveal the overlay (see JS below) */
      height: 100%;
      width: 0;
      position: fixed;
      /* Stay in place */
      z-index: 1;
      /* Sit on top */
      left: 0;
      top: 0;
      background-color: rgb(0, 0, 0);
      /* Black fallback color */
      background-color: rgba(0, 0, 0, 0.9);
      /* Black w/opacity */
      overflow-x: hidden;
      /* Disable horizontal scroll */
      transition: 0.5s;
      /* 0.5 second transition effect to slide in or slide down the overlay (height or width, depending on reveal) */
    }

    /* Position the content inside the overlay */
    .overlay-content {
      position: relative;
      top: 25%;
      /* 25% from the top */
      width: 100%;
      /* 100% width */
      text-align: center;
      /* Centered text/links */
      margin-top: 30px;
      /* 30px top margin to avoid conflict with the close button on smaller screens */
    }

    /* The navigation links inside the overlay */
    .overlay a {
      padding: 8px;
      text-decoration: none;
      font-size: 36px;
      color: #818181;
      display: block;
      /* Display block instead of inline */
      transition: 0.3s;
      /* Transition effects on hover (color) */
    }

    /* When you mouse over the navigation links, change their color */
    .overlay a:hover,
    .overlay a:focus {
      color: #f1f1f1;
    }

    /* Position the close button (top right corner) */
    .overlay .closebtn {
      position: absolute;
      top: 20px;
      right: 45px;
      font-size: 60px;
    }

    /* When the height of the screen is less than 450 pixels, change the font-size of the links and position the close button again, so they don't overlap */
    @media screen and (max-height: 450px) {
      .overlay a {
        font-size: 20px
      }

      .overlay .closebtn {
        font-size: 40px;
        top: 15px;
        right: 35px;
      }
    }

    h1 {
      font-family: sans-serif;

      color: #228B22;
      text-align: center;
      font-size: 30px;
      max-width: 700px;
      position: relative;
    }

    h1:before {
      content: "";
      display: block;
      width: 25%;
      height: 2px;
      background: #000;
      left: 0;
      top: 50%;
      position: absolute;
    }

    h1:after {
      content: "";
      display: block;
      width: 25%;
      height: 2px;
      background: #000;
      right: 0;
      top: 50%;
      position: absolute;
    }



    h2 {
      font-family: sans-serif;

      color: #228B22;
      text-align: center;
      font-size: 30px;
      max-width: auto;
      position: relative;
      margin-top: 20px;
      margin-bottom: 15px;
    }

    h2:before {
      content: "";
      display: block;
      width: 40%;
      height: 2px;
      background: #000;
      left: 0;
      top: 50%;
      position: absolute;
    }

    h2:after {
      content: "";
      display: block;
      width: 40%;
      height: 2px;
      background: #000;
      right: 0;
      top: 50%;
      position: absolute;
    }

    .col-5 {
      flex: 1 0 60.6 !important;
    }



    @media screen and (max-width: 450px) {



      h2 {
        font-family: sans-serif;

        color: #228B22;
        text-align: center;
        font-size: 30px;
        max-width: auto;
        position: relative;
        margin-top: 20px;
        margin-bottom: 15px;
      }

      h2:before {
        content: "";
        display: block;
        width: 25%;
        height: 2px;
        background: #000;
        left: 0;
        top: 50%;
        position: absolute;
      }

      h2:after {
        content: "";
        display: block;
        width: 25%;
        height: 2px;
        background: #000;
        right: 0;
        top: 50%;
        position: absolute;
      }


    }

        .id  {
      background-image: url("paper.gif");
      background-color: #cccccc;
      height:400px;
    }
  </style>

<script src="https://kit.fontawesome.com/687cfff67f.js" crossorigin="anonymous"></script>
</head>

<body>


  <!--Nav Bar-->


  <nav class="navbar navbar-expand-lg sticky-top navbar-light bg-light shadow" style="margin-bottom: 0px ;">
    <div class="container">

      <a class="navbar-brand" href="#"><b>Kiambu Magazine </b></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02"
        aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">News</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Stocks</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Poetry</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Most read</a>
          </li>

        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
  <!--end of navbar-->
  <br>

  <!--This is the heading landing page -->

  
<div  class=" container "  style="height:600px; margin-bottom: 50px;" >
  <img src="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/rockcms/2022-03/black-lab-favorite-dog-main-220315-e8e0ee.jpg" alt="Norway" style="float:left;width:100%;height:100%;object-fit:cover;">
</div>





 
  <!--The body part of this blog-->

  <div class="container">
    <h3 style="color: rgb(185, 24, 24) "> Uhuru made remarks concerning how Kenya's Debts have helped Increase living
      Standards</h3>
    <p>Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a
      search for 'lorem ipsum' will uncover many web sites still in their infancy when an unknown printer took a galley
      of type and scrambled it to make a type specimen book.Many desktop publishing packages and web page editors now
      use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in
      their infancy when an unknown printer took a galley of type and scrambled it to make a type specimen book.Many
      desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for
      'lorem ipsum' will uncover many web sites still in their infancy when an unknown printer took a galley of type and
      scrambled it to make a type specimen book.Many desktop publishing packages and web page editors now use Lorem
      Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their
      infancy when an unknown printer took a galley of type and scrambled it to make a type specimen book.Many desktop
      publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem
      ipsum' will uncover many web sites still in their infancy when an unknown printer took a galley of type and
      scrambled it to make a type specimen book.
      <br>


      <br>
      Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a
      search for 'lorem ipsum' will uncover many web sites still in their infancy when an unknown printer took a galley
      of type and scrambled it to make a type specimen book.Many desktop publishing packages and web page editors now
      use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in
      their infancy when an unknown printer took a galley of type and scrambled it to make a type specimen book.Many
      desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for
      'lorem ipsum' will uncover many web sites still in their infancy when an unknown printer took a galley of type and
      scrambled it to make a type specimen book.Many desktop publishing packages and web page editors now use Lorem
      Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their
      infancy when an unknown printer took a galley of type and scrambled it to make a type specimen book.Many desktop
      publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem
      ipsum' will uncover many web sites still in their infancy when an unknown printer took a galley of type and
      scrambled it to make a type specimen book.
    </p>
  </div>


  <div class="container">
    <p   style="color: green ;"> Written By</p>
    <i class="fa-solid fa-feather-pointed"></i><hp style="color:red ;"> <span></span>  &nbsp; <b> Liz Wambui </hp>
  </div>


  <!--end-->
<!--Read more-->

<div class="container">
  <h2 class=" text-center  ">More For You</h2>
</div>

  <div class="container  overflow-auto shadow "  >
    
    
    <div class="row flex-row no-gutters w-100 flex-nowrap" style=" margin-bottom:20px; ">
        <div class="col-6 padding-0" >
            <div class="cardi card-block" style="margin-right: 5%;" > <!--=======================================================================SETTING HEIGHT============================-->
              <img src="https://www.monaco.edu/app/uploads/sites/4/2021/07/Sports_Management.jpg" class="img-fluid w-100" alt="...">
              <div class="cardi-body" style="margin-right: 20px ;" >
                <h5 class="card-title" style="color:red ; font-size: 20px; ">If we stack multiple column classes</h5>
                <div class="container " style=" text-align:right; ">
                  <i style='font-size:18px' class='far'>&#xf017;</i> 20 hours ago
                </div>
                
              </div>
            </div>
        </div>
        <div class="col-6 " >
          <div class="cardi card-block"   style="margin-right: 5%;" > <!--=======================================================================SETTING HEIGHT============================-->
            <img src="https://www.monaco.edu/app/uploads/sites/4/2021/07/Sports_Management.jpg" class="img-fluid w-100" alt="...">
            <div class="cardi-body" >
              <h5 class="card-title" style="color:red ; font-size: 20px;  ">collaborating and sharing organizational knowledge.</h5>
              <div class="container " style=" text-align:right; ">
                <i style='font-size:18px' class='far'>&#xf017;</i>20 hours ago
              </div>
              
            </div>
          </div>
      </div>
      <div class="col-6" >
        <div class="cardi card-block"  style="margin-right: 5%;" > <!--=======================================================================SETTING HEIGHT============================-->
          <img src="https://www.monaco.edu/app/uploads/sites/4/2021/07/Sports_Management.jpg" class="img-fluid w-100" alt="...">
          <div class="cardi-body" >
            <h5 class="card-title" style="color:red ; font-size: 20px; ">Businesses Owned by Radio Present.</h5>

            <div class="container " style=" text-align:right; ">
              <i style='font-size:18px' class='far'>&#xf017;</i>     20 hours ago
            </div>
            
          </div>
        </div>
    </div>
       
    </div>
</div>
  
</div>




  <!--footer-->


  <footer class="mainfooter" role="contentinfo">
    <div class="footer-middle">
      <div class="container">
        <div class="row">
          <div class="col-md-3 col-sm-6">
            <!--Column1-->
            <div class="footer-pad">
              <h4>About Us</h4>
              <ul class="list-unstyled">
                <li><a href="#"></a></li>
                <li><a href="#">Payment Center</a></li>
                <li><a href="#">Contact Directory</a></li>
                <li><a href="#">Forms</a></li>
                <li><a href="#">News and Updates</a></li>

              </ul>
            </div>
          </div>
          <div class="col-md-3 col-sm-6">
            <!--Column1-->
            <div class="footer-pad">
              <h4>Our Writers</h4>
              <ul class="list-unstyled">

                <li><a href="#">Accessibility</a></li>
                <li><a href="#">Disclaimer</a></li>
                <li><a href="#">Privacy Policy</a></li>
                <li><a href="#">FAQs</a></li>

              </ul>
            </div>
          </div>
          <div class="col-md-3 col-sm-6">
            <!--Column1-->
            <div class="footer-pad">
              <h4>Products</h4>
              <ul class="list-unstyled">
                <li><a href="#">Parks and Recreation</a></li>
                <li><a href="#">Public Works</a></li>
                <li><a href="#">Police Department</a></li>

                <li>
                  <a href="#"></a>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-md-3">
            <h4>Follow Us</h4>
            <ul class="social-network social-circle">
              <li><a href="#" class="icoFacebook" title="Facebook"><i class="fa fa-facebook"></i></a></li>
              <li><a href="#" class="icoLinkedin" title="Linkedin"><i class="fa fa-instagram"></i></a></li>
            </ul>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12 copy">
            <p class="text-center">&copy; Copyright 2022 - Company Name. All rights reserved.</p>
          </div>
        </div>


      </div>
    </div>
  </footer>

  <!--end footer-->




  <!-- Optional JavaScript; choose one of the two! -->

  <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct"
    crossorigin="anonymous"></script>

  <script>
    function openNav() {
      document.getElementById("myNav").style.width = "100%";
    }

    function closeNav() {
      document.getElementById("myNav").style.width = "0%";
    }
  </script>

  <!-- Option 2: Separate Popper and Bootstrap JS -->
  <!--
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
    -->
</body>

</html>