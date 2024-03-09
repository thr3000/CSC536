const mix = require('laravel-mix');
require('postcss-import');

mix.js('resources/js/app.js', 'public/js')
   .sass('node_modules/bootstrap/scss/bootstrap.scss', 'public/css')
   .postCss('resources/css/app.css', 'public/css');