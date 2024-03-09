<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="{{ mix('css/app.css') }}" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <title>Login</title>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <main role="main" class="col-md-9 ml-sm-auto col-lg-10 bg-light" style="height: 100vh; width: 100vw;">
                <div class="w-50 p-2">
                    <h1>Login</h1>
                    <form id="loginForm">
                        <div class="form-group">
                            <label for="emailInput">Email address</label>
                            <input type="email" class="form-control" id="emailInput" placeholder="Enter Email">
                        </div>
                        <div class="form-group">
                            <label for="passwordInput">Password</label>
                            <input type="password" class="form-control" id="passwordInput" placeholder="Enter Password">
                            <a href="/user_reset" style="text-decoration:underline; float:right">Forgot password</a>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="rememberCheck">
                            <label class="form-check-label" for="rememberCheck">Remember me</label>
                        </div>
                        <button type="submit" class="btn btn-secondary mt-3 w-100">Login</button>
                    </form>
                    <br>
                    <a href="/register">No Account? Sign-up today!</a>
                </div>
            </main>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var loginForm = document.getElementById('loginForm');

            loginForm.addEventListener('submit', function (e) {
                e.preventDefault();

                var email = document.getElementById('emailInput').value;
                var password = document.getElementById('passwordInput').value;
                console.log(email)
                console.log(password)

                if (!email || !password) {
                        Swal.fire('Validation error', 'Email and password are required', 'error');
                        return;
                    }

                axios.post('/login', {
                    email: email,
                    password: password
                })
                .then(function (response) {
                    window.location.href = '/dashboard';
                })
                .catch(function (error) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Invalid Email or password!'
                    });
                });
            });
        });
    </script>
</body>
</html>