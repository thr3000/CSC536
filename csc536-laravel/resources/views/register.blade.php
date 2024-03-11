<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="{{ mix('css/app.css') }}" rel="stylesheet">
    <title>Register</title>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <main role="main" class="col-md-9 ml-sm-auto col-lg-10 bg-light" style="height: 100vh; width: 100vw;">
                <div class="d-none d-sm-flex d-md-flex d-lg-flex d-xl-flex flex-row">
                    <div class="w-50 p-2">
                        <h1>Register</h1>
                        <form id="registerForm">
                            <div class="form-group">
                                <label for="usernameInput">Username</label>
                                <input type="text" class="form-control" id="usernameInput" placeholder="3 to 16 characters (only alphabets, numbers, and underscores are allowed)">
                            </div>
                            <div class="form-group">
                                <label for="emailInput">Email</label>
                                <input type="email" class="form-control" id="emailInput" placeholder="Enter Email">
                            </div>
                            <div class="form-group">
                                <label for="passwordInput">Password</label>
                                <input type="password" class="form-control" id="passwordInput" placeholder="Must include at least: 8 characters, one uppercase letter, one number, one special character">
                            </div>
                            <div class="form-group">
                                <label for="confirmPasswordInput">Re-enter Password</label>
                                <input type="password" class="form-control" id="confirmPasswordInput" placeholder="Re-enter Password">
                            </div>
                            <button type="submit" class="btn btn-secondary mt-3 w-100">Register</button>
                            <br>
                            <a href="/login">Already have an account?</a>
                        </form>
                    </div>
                </div>
            </main>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var registerForm = document.getElementById('registerForm');

            registerForm.addEventListener('submit', function (e) {
                e.preventDefault();

                var username = document.getElementById('usernameInput').value;
                var email = document.getElementById('emailInput').value;
                var password = document.getElementById('passwordInput').value;
                var confirmPassword = document.getElementById('confirmPasswordInput').value;
                console.log(username)
                console.log(email)
                console.log(password)
                console.log(confirmPassword)


                if (!username || !email || !password || !confirmPassword) {
                    Swal.fire('Validation error', 'All fields are required', 'error');
                    return;
                }

                if (password !== confirmPassword) {
                    Swal.fire('Validation error', 'Passwords do not match', 'error');
                    return;
                }

                axios.post('/register', {
                    username: username,
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
                        text: 'Registration failed!'
                    });
                });
            });
        });
    </script>
</body>
</html>
