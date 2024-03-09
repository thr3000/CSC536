<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="{{ mix('css/app.css') }}" rel="stylesheet">
        <title>Register</title>

        <!-- Styles -->
        <style>
            
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <main role="main" class="col-md-9 ml-sm-auto col-lg-10 bg-light" style="height: 100vh; width: 100vw;">
                    <div class="d-none d-sm-flex d-md-flex d-lg-flex d-xl-flex flex-row">
                        <div class="w-50 p-2">
                            <h1>Register</h1>
                        <div>
                        <div class="form-group">
                            <label for="exampleInputEmail1">Username</label>
                            <input class="form-control"
                                placeholder="3 to 16 characthers(only alphabets, numbers, and underscores are allowed)">
                        </div>
                        <div class="form-group">
                            <label for="exampleInputEmail1">Email</label>
                            <input type="email" class="form-control" placeholder="Enter Email">
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">Password</label>
                            <input type="password" class="form-control"
                                placeholder="Must include at least: 8 characters, one uppercase letter, one number, one special character">
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">Re-enter Password</label>
                            <input type="password" class="form-control" placeholder="Re-enter Password">
                        </div>
                        <button type="submit" class="btn btn-secondary mt-3 w-100">Register</button>
                        <br>
                        <a href="/login">Already have an account?</a>
                    </div>
                </main>
            </div>
        </div>
    </body>
    <script>
    </script>
</html>
