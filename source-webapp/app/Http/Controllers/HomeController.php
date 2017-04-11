<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

use Illuminate\Support\Facades\DB;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $users = DB::table('usuarios')->get();
        return view('/home',compact('users'));
    }

     public function usuarios()
    {
        
       $users = DB::table('usuarios')->get();
        return view('/usuarios',compact('users'));
    }

    public function tarjetas()
    {
        
        return view('/tarjetas');
    }

    public function logs()
    {
        
        return view('/logs');
    }
}
