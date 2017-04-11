<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', 'HomeController@index');

Auth::routes();

Route::get('/home', 'HomeController@index');


Route::get('/logout', function (){

	Auth::logout();
	return view('/login');
});


Route::get('/Usuarios', 'HomeController@usuarios');
Route::post('/modify_user/{id}','UsuarioController@modify_user');
Route::post('/delete_user/{id}','UsuarioController@delete_user');
Route::post('/create_user','UsuarioController@create_user');

Route::get('/Tarjetas', 'TarjetaController@tarjetas');
Route::post('/create_card','TarjetaController@create_card');
Route::post('/delete_card/{id}','TarjetaController@delete_card');
Route::post('/modify_card/{id}','TarjetaController@modify_card');

Route::get('/Logs', 'LogController@logs');