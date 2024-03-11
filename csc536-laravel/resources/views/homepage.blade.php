<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Homepage</title>
    <!-- Linking to Bootstrap for styling -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css" rel="stylesheet">
    <!-- Linking to Google Fonts for cool font -->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap" rel="stylesheet">
    <style>
        /* Custom styling */
        body {
            font-family: 'Roboto', sans-serif; /* Applying cool font */
            padding-top: 50px;
            margin: 0; /* Remove default margin */
            background-color: #0dcaf0; /* Changed background color to light gray */
        }
        .container {
            max-width: 400px;
            margin: auto;
            text-align: center; /* Center text horizontally */
            padding-top: 50px; /* Add space from the top */
        }
        .btn-login, .btn-register {
            margin-top: 20px; /* Add some space between buttons */
            font-size: 1.5em; /* Adjust font size */
            padding: 15px 30px; /* Adjust button padding */
            background-color: #d63384; /* Blue color */
            color: #fff; /* White text */
            border: none; /* No border */
            border-radius: 10px; /* Rounded corners */
            text-decoration: none; /* Remove underline */
            transition: all 0.3s ease; /* Smooth transition */
        }
        .btn-login:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
        .background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #0dcaf0; /* Changed background color to light gray */
            z-index: -1; /* Send the background behind other content */
        }
        .welcome-text {
            font-size: 3em; /* Larger font size */
            margin-bottom: 150px; /* Add some space below welcome text */
        }
        .register-text {
            margin-top: 60px; /* Add space above registration text */
        }
    </style>
</head>
<body>
    <div class="background"></div>
    <div class="container">
        <h1 class="welcome-text">Welcome to Goalzz!!</h1>
        <a class="btn-login" href="/login">Login</a>
        <p class="register-text">Don't have an account?</p>
        <a class="btn btn-register" href="/register">Sign Up</a>
    </div>
</body>
</html>
